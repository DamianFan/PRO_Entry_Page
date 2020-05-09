from database.fetch import *
from .event_ptm import *
from .models import *
import os
import csv
from collections import defaultdict
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from .utils import *
# from entrypage.entry import get_xref
# mod = {}
# with open(os.path.join(os.path.dirname(__file__), 'mod.txt'), 'r') as csvfile:
#   f = list(csv.reader(csvfile, delimiter='\t'))
#   for l in f:
#     mod[l[0]] = l[1]


class ENTRY(object):
  r"""
  Define ENTRY object for MSA.
  All related information will be saved in seqRecord object.
  http://biopython.org/DIST/docs/api/Bio.SeqRecord.SeqRecord-class.html
  """

  def __init__(self, id):
    r"""
    Attributes:
    id -- PRO id
    seq -- protein sequence, in IUPAC.protein
           http://biopython.org/DIST/docs/api/Bio.Alphabet.IUPAC-module.html
    name --  PRO short label
    definition -- PRO definition
    description -- entry sites summary
    dbxrefs --  corresponded UniProt AC list
    Cat -- entry's category
    Group -- possible value: "msa-request", "msa-orthoform", "msa-isoform",
    "msa-ptmform"
    modification -- a dictionary keeps all PTM objects. key is the modified
    position,
                    value is a list of PTM objects. e.g.: modification[465]=[
                    PTMobj1,PTMobj2]
    enzyme -- a list of PTM enzyme id
    pmid -- a list of pmid from OBO stanza
    """

    self.id = id
    self.seq = ''
    self.name = ''
    self.definition = ''
    self.description = ''
    self.dbxrefs = []
    self.Cat = ''
    self.Group = ''
    self.modification = defaultdict(list)
    self.enzyme = []
    self.pmid = []

  # def initial(self, full=True):
  #     pass
  # def init_seq(self, type):
  #     pass
  # def init_mod(self):
  #     pass

  def generate_seqrecords(self):
    """
    Create seqRecords object for each entry. Return seqRecord object.
    annotations: a dict with two keys:
        1 "relationship": store Group attribute, a string
        2 "modification": store modification attribute, a dict
        3."definition": store PRO def
    """

    record = SeqRecord(self.seq, id=self.id, name=self.name,
                       description=self.description, dbxrefs=self.dbxrefs,
                       annotations={"relationship": self.Group,
                                    "modification": self.modification,
                                    "definition": self.definition})
    return record


  @staticmethod
  def batch_initial(ids, full=True):
      """
       if full==True: collect entry, sequence and all modification data
       if full==False: only collect entry data
       """
      entries = {}
      residues = ''
      enzymesit = []
      info = pass_node_info_by_ids(ids)
      for case in info:
          cid = case['id']
          entries[cid] = ENTRY(cid)
          # if case['?synonym']
          # entries[cid].name = case['name']
          if 'synonym' in case:
              if case['name'].find('complex') > -1 or cid.find('CHEBI') > -1:
                  # print('from frist if')
                  entries[cid].name = case['name']
              else:
                  synonym = case['synonym'].split(';')
                  for syns in synonym:
                      # print(syns)
                      if syns.find('EXACT PRO-short-label') != -1:
                          # print('exact')
                          j = syns.split(' ')
                          entries[cid].name = j[1].replace('"', '')
                      elif syns.find('UniProtKB') == -1 and syns.find('(') == -1:
                          # print('from unip')
                          entries[cid].name = syns
                          if syns.find('/')!=-1:
                              ls = syns.split('/')
                              entries[cid].name = ls[0]
          else:
              entries[cid].name = case['name']
          definition = case['PRO_termDef']
          entries[cid].definition = definition
          scategory = case['Category'].split('.')
          for i in scategory:
              if i.find('Category=') != -1:
                  category = i.replace('Category=', '')
                  entries[cid].Cat = category
              else:
                  enzymesit.append(i)
          if definition.find('UniProtKB') != -1:
              p = definition.find('UniProtKB')
              tar = definition[p:]
              ed = tar.find(',')
              if ed != -1:
                uni = tar[:ed]
              else:
                ed = len(tar)
                uni = tar[:ed]
              if uni != []:
                  unilist = uni.split('.')
                  funid = unilist[0]
              else:
                  funid = ''
              entries[cid].dbxrefs.append(funid)
              residues = definition[p:]
              residues = residues.replace(funid,'')
              # print('aftercase', residues)

              if residues != '':
                  if residues[0] == ',':
                      residues = residues[1:]
                  if residues[0] == ' ':
                      residues = residues[1:]
              entries[cid].description = residues
          else:
              xrefs_set = get_xref_for_msa(cid)
              for xr in xrefs_set:
                  if xr.find('UniProtKB')!=-1:
                      tart = xr.replace(' ','')
                      entries[cid].dbxrefs.append(tart)

          if full:
            #batch_mod
            batchmod = modify_residues(residues)
            for batch in batchmod:
                P = PTM()
                P.substrate = cid
                P.enzyme = ''
                mod_id = batch[0]
                if mod_id.find(':') > -1:
                    P.modType = mod_id.split(':')[1]
                P.seqPos = batch[2]
                P.aa = batch[1]
                P.source = 'pro'
                P.note = ''
                P.pmid = ''
                entries[cid].modification[P.seqPos].append(P)
            if enzymesit != []:
                for i in enzymesit:
                    if i != '':
                        e_set = modify_enzymes(i)
                        for j in e_set:
                            for ptm in entries[cid].modification[j[3]]:
                                ptm.enzyme = {j[2]:j[1]}
                            entries[cid].enzyme.append(j[2])
                    for id in entries.keys():
                        entries[id].enzyme = list(set(entries[id].enzyme))
            evidence = defaultdict(list)
            for r in modify_xref(definition):
                evidence[cid].append(r)
            for id in entries.keys():
                for pos in entries[id].modification.keys():
                    for ptm in entries[id].modification[pos]:
                        ptm.pmid = evidence[id]
      # print('*********',entries['PR:000025934'].description,entries['PR:000025934'].dbxrefs)
            # batch seq
      entries = ENTRY.batch_seq(entries)
      # print('entries.values()',entries.values())
      # for i in entries.values():
      #     print('test id',i.id, i.seq)
      #     if i.seq == '':
      #         print('none: ',i.id)

      # print('entriesid',entries['PR:000025934'].seq)
      return entries.values()


  @staticmethod
  def batch_seq(entries):
    # collect all xref:
    xrefList = []
    for e in entries.values():
      # print('check xrefs: ',e.id,e.dbxrefs)
      xrefList.extend(e.dbxrefs)
    # create a mapping between "UniProtKB:Q15796-2": "Q15796-2"
    acMap = {}
    for x in list(set(xrefList[:])):
      d = x.split(':')
      if d[0] == 'UniProtKB':
        acMap[x] = d[1] if not d[1].endswith('-1') else d[1][:-2]
    # acMap example result:  {u'UniProtKB:P26367-3': u'P26367-3', 'UniProtKB:P26367-2': 'P26367-2', 'UniProtKB:P26367': 'P26367', 'UniProtKB:P26367-1': 'P26367'}
    # load sequences
    # this is test

    seq = {}
    for r in get_seqs(acMap):
      seq[r.subject] = Seq(r.sequence, IUPAC.protein)
      # print('input r for get_seqs:',r.subject)
      # print('ordinary seq: ',r.sequence)
      # print('seq[r.subject]',seq[r.subject])
    for ac in acMap.values():
      if ac not in seq:
        # print('ac: ',ac)
        # print(get_seq_external(ac))
        # print('\n')
        seq[ac] = Seq(get_seq_external(ac), IUPAC.protein)
    # add sequence to entry
    for e in entries.values():
      # print(e)
      if len(e.dbxrefs) > 0:
        e.seq = seq[acMap[e.dbxrefs[0]]]
      print('e.seq:',e.id,e.seq,e.dbxrefs)
    return entries

def get_xref_for_msa(id):
    query_id = pass_ids_for_query([id])
    query = """
    PREFIX obo: <http://purl.obolibrary.org/obo/> 
    PREFIX paf: <http://pir.georgetown.edu/pro/paf#> 
    PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
    SELECT * 
    where
    {
    values ?PRO_term{"""+query_id+"""}
    ?PRO_term  oboInOwl:hasDbXref ?DbRef .
    }
    """
    sparqlSearch = SparqlSearch()
    xrefs, error = sparqlSearch.executeQuery(query)
    xrefslist = []
    for i in xrefs:
        if 'DbRef' in i:
            xrefslist.append(i['DbRef'])
    return xrefslist