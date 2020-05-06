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
              entries[cid].dbxrefs.append(uni)
              residues = definition[p:]
              residues = residues.replace(uni,'')
              if residues[0] == ',':
                  residues = residues[1:]
              if residues[0] == ' ':
                  residues = residues[1:]
              entries[cid].description = residues

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

            # batch seq
      entries = ENTRY.batch_seq(entries)
      return entries.values()


  @staticmethod
  def batch_seq(entries):
    # collect all xref:
    xrefList = []
    for e in entries.values():
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
    for ac in acMap.values():
      if ac not in seq:
        seq[ac] = Seq(get_seq_external(ac), IUPAC.protein)
    # add sequence to entry
    for e in entries.values():
      if len(e.dbxrefs) > 0:
        e.seq = seq[acMap[e.dbxrefs[0]]]
    return entries