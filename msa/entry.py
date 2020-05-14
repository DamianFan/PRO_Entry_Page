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
from msa.msa_data import *
from itertools import chain
import urllib

# from entrypage.entry import get_xref
# mod = {}
# with open(os.path.join(os.path.dirname(__file__), 'mod.txt'), 'r') as csvfile:
#   f = list(csv.reader(csvfile, delimiter='\t'))
#   for l in f:
#     mod[l[0]] = l[1]

# mod = {}
# class ENTRY(object):
#   r"""
#   Define ENTRY object for MSA.
#   All related information will be saved in seqRecord object.
#   http://biopython.org/DIST/docs/api/Bio.SeqRecord.SeqRecord-class.html
#   """
#
#   def __init__(self, id):
#     r"""
#     Attributes:
#     id -- PRO id
#     seq -- protein sequence, in IUPAC.protein
#            http://biopython.org/DIST/docs/api/Bio.Alphabet.IUPAC-module.html
#     name --  PRO short label
#     definition -- PRO definition
#     description -- entry sites summary
#     dbxrefs --  corresponded UniProt AC list
#     Cat -- entry's category
#     Group -- possible value: "msa-request", "msa-orthoform", "msa-isoform",
#     "msa-ptmform"
#     modification -- a dictionary keeps all PTM objects. key is the modified
#     position,
#                     value is a list of PTM objects. e.g.: modification[465]=[
#                     PTMobj1,PTMobj2]
#     enzyme -- a list of PTM enzyme id
#     pmid -- a list of pmid from OBO stanza
#     """
#
#     self.id = id
#     self.seq = ''
#     self.name = ''
#     self.definition = ''
#     self.description = ''
#     self.dbxrefs = []
#     self.Cat = ''
#     self.Group = ''
#     self.modification = defaultdict(list)
#     self.enzyme = []
#     self.pmid = []
#
#   # def initial(self, full=True):
#   #     pass
#   # def init_seq(self, type):
#   #     pass
#   # def init_mod(self):
#   #     pass
#
#   def generate_seqrecords(self):
#     """
#     Create seqRecords object for each entry. Return seqRecord object.
#     annotations: a dict with two keys:
#         1 "relationship": store Group attribute, a string
#         2 "modification": store modification attribute, a dict
#         3."definition": store PRO def
#     """
#
#     record = SeqRecord(self.seq, id=self.id, name=self.name,
#                        description=self.description, dbxrefs=self.dbxrefs,
#                        annotations={"relationship": self.Group,
#                                     "modification": self.modification,
#                                     "definition": self.definition})
#     return record
#
#
#   @staticmethod
#   def batch_initial(ids, full=True):
#       """
#        if full==True: collect entry, sequence and all modification data
#        if full==False: only collect entry data
#        """
#       entries = {}
#       residues = ''
#       enzymesit = []
#       info = pass_node_info_by_ids(ids)
#       for case in info:
#           cid = case['id']
#           entries[cid] = ENTRY(cid)
#           # if case['?synonym']
#           # entries[cid].name = case['name']
#           if 'synonym' in case:
#               if case['name'].find('complex') > -1 or cid.find('CHEBI') > -1:
#                   # print('from frist if')
#                   entries[cid].name = case['name']
#               else:
#                   synonym = case['synonym'].split(';')
#                   for syns in synonym:
#                       # print(syns)
#                       if syns.find('EXACT PRO-short-label') != -1:
#                           # print('exact')
#                           j = syns.split(' ')
#                           entries[cid].name = j[1].replace('"', '')
#                       elif syns.find('UniProtKB') == -1 and syns.find('(') == -1:
#                           # print('from unip')
#                           entries[cid].name = syns
#                           if syns.find('/')!=-1:
#                               ls = syns.split('/')
#                               entries[cid].name = ls[0]
#           else:
#               entries[cid].name = case['name']
#           definition = case['PRO_termDef']
#           entries[cid].definition = definition
#           scategory = case['Category'].split('.')
#           for i in scategory:
#               if i.find('Category=') != -1:
#                   category = i.replace('Category=', '')
#                   entries[cid].Cat = category
#               else:
#                   enzymesit.append(i)
#           if definition.find('UniProtKB') != -1:
#               p = definition.find('UniProtKB')
#               tar = definition[p:]
#               ed = tar.find(',')
#               if ed != -1:
#                 uni = tar[:ed]
#               else:
#                 ed = len(tar)
#                 uni = tar[:ed]
#               if uni != []:
#                   unilist = uni.split('.')
#                   funid = unilist[0]
#               else:
#                   funid = ''
#               entries[cid].dbxrefs.append(funid)
#               residues = definition[p:]
#               residues = residues.replace(funid,'')
#               print('aftercase', residues)
#
#               if residues != '':
#                   if residues[0] == ',':
#                       residues = residues[1:]
#                   if residues[0] == ' ':
#                       residues = residues[1:]
#               entries[cid].description = residues
#           else:
#               xrefs_set = get_xref_for_msa(cid)
#               for xr in xrefs_set:
#                   if xr.find('UniProtKB')!=-1:
#                       tart = xr.replace(' ','')
#                       entries[cid].dbxrefs.append(tart)
#
#           if full:
#             #batch_mod
#             batchmod = modify_residues(cid,residues)
#             # print('batchmod',batchmod)
#
#             for r in batchmod:
#                 P = PTM()
#                 P.substrate = r.subject
#                 P.enzyme = ''
#                 if r.mod_id.find(':') > -1:
#                     P.modType = 'MOD'
#                 P.seqPos = r.position
#                 P.aa = r.abbrev3
#                 P.source = 'pro'
#                 P.note = ''
#                 P.pmid = ''
#                 entries[r.subject].modification[P.seqPos].append(P)
#
#             # for batch in batchmod:
#             #     P = PTM()
#             #     P.substrate = cid
#             #     P.enzyme = ''
#             #     mod_id = batch[0]
#             #     if mod_id.find(':') > -1:
#             #         P.modType = mod_id.split(':')[1]
#             #     P.seqPos = batch[2]
#             #     P.aa = batch[1]
#             #     P.source = 'pro'
#             #     P.note = ''
#             #     P.pmid = ''
#             #     entries[cid].modification[P.seqPos].append(P)
#
#             if enzymesit != []:
#                 for i in enzymesit:
#                     if i != '':
#                         e_set = modify_enzymes(cid,i)
#                         for r in e_set:
#                             for ptm in entries[r.subject].modification[r.position]:
#                                 ptm.enzyme = {r.aggkey: r.obo_dbxref_description}
#                             entries[cid].enzyme.append(r.aggkey)
#             for id in entries.keys():
#                     entries[id].enzyme = list(set(entries[id].enzyme))
#
#             # print('modification',entries[cid].modification)
#             evidence = defaultdict(list)
#             for r in modify_xref(definition):
#                 evidence[cid].append(r)
#             for id in entries.keys():
#                 for pos in entries[id].modification.keys():
#                     for ptm in entries[id].modification[pos]:
#                         ptm.pmid = evidence[id]
#             print('evidence',evidence[cid])
#       # print('*********',entries['PR:000025934'].description,entries['PR:000025934'].dbxrefs)
#             # batch seq
#             entries = ENTRY.batch_seq(entries)
#       # print('entries.values()',entries.values())
#       # for i in entries.values():
#       #     print('test id',i.id, i.seq)
#       #     if i.seq == '':
#       #         print('none: ',i.id)
#
#       # print('entriesid',entries['PR:000025934'].seq)
#       return entries.values()
#
#   # @staticmethod
#   # def batch_mod(ids, entries):
#   #     # get ptms from definition modified residue list.
#   #     for r in modify_residues(ids):
#   #         P = PTM()
#   #         P.substrate = r.subject
#   #         P.enzyme = ''
#   #         if r.mod_id.find(':') > -1:
#   #             P.modType = mod[r.mod_id.split(':')[1]]
#   #         P.seqPos = r.position
#   #         P.aa = r.abbrev3
#   #         P.source = 'pro'
#   #         P.note = ''
#   #         P.pmid = ''
#   #
#   #         entries[r.subject].modification[P.seqPos].append(P)
#   #
#   #     # update the ptm with kinase/acetylase/... from comment
#   #     for r in get_enzymes(ids):
#   #         # assert entries[r.subject].modification.has_key(r.position)
#   #         for ptm in entries[r.subject].modification[r.position]:
#   #             ptm.enzyme = {r.aggkey: r.obo_dbxref_description}
#   #         entries[r.subject].enzyme.append(r.aggkey)
#   #     # update the enzyme symbol list
#   #     for id in entries.keys():
#   #         entries[id].enzyme = list(set(entries[id].enzyme))
#   #
#   #     # add pmids for each ptm
#   #     evidence = defaultdict(list)
#   #     for r in get_def_xref(ids):
#   #         evidence[r.subject].append(r.object)
#   #
#   #     for id in entries.keys():
#   #         for pos in entries[id].modification.keys():
#   #             for ptm in entries[id].modification[pos]:
#   #                 ptm.pmid = evidence[id]
#   #
#   #     return entries
#
#
#   @staticmethod
#   def batch_seq(entries):
#     # collect all xref:
#     xrefList = []
#     for e in entries.values():
#       # print('check xrefs: ',e.id,e.dbxrefs)
#       xrefList.extend(e.dbxrefs)
#     # create a mapping between "UniProtKB:Q15796-2": "Q15796-2"
#     acMap = {}
#     for x in list(set(xrefList[:])):
#       d = x.split(':')
#       if d[0] == 'UniProtKB':
#         acMap[x] = d[1] if not d[1].endswith('-1') else d[1][:-2]
#     # acMap example result:  {u'UniProtKB:P26367-3': u'P26367-3', 'UniProtKB:P26367-2': 'P26367-2', 'UniProtKB:P26367': 'P26367', 'UniProtKB:P26367-1': 'P26367'}
#     # load sequences
#     # this is test
#
#     seq = {}
#     for r in get_seqs(acMap):
#       seq[r.subject] = Seq(r.sequence, IUPAC.protein)
#       # print('input r for get_seqs:',r.subject)
#       # print('ordinary seq: ',r.sequence)
#       # print('seq[r.subject]',seq[r.subject])
#     for ac in acMap.values():
#       if ac not in seq:
#         # print('ac: ',ac)
#         # print(get_seq_external(ac))
#         # print('\n')
#         seq[ac] = Seq(get_seq_external(ac), IUPAC.protein)
#     # add sequence to entry
#     for e in entries.values():
#       # print(e)
#       if len(e.dbxrefs) > 0:
#         e.seq = seq[acMap[e.dbxrefs[0]]]
#       print('e.seq:',e.id,e.seq,e.dbxrefs)
#     return entries


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
    print('input ids for batch_initial: ',ids)
    # build entries object
    for id in ids:
      entries[id] = ENTRY(id)

    for r in get_short_label(ids):
      entries[r.subject].name = r.synonym_field
      print('check short label: ',r.synonym_field)
    for r in get_terms(ids):
      if entries[r.subject].name == '':
        entries[r.subject].name = r.name
      entries[r.subject].definition = r.definition
      entries[r.subject].Cat = r.category

    for r in get_sites(ids):
      entries[r.subject].description = r.residue

    for r in get_xrefs(ids):
      if r.object.startswith('UniProtKB:'):
        entries[r.subject].dbxrefs.append(r.object)
        print('check get_xrefs: ',r.object)
    if full:
      entries = ENTRY.batch_mod(ids, entries)
      entries = ENTRY.batch_seq(entries)

    return entries.values()

  @staticmethod
  def batch_mod(ids, entries):
    # get ptms from definition modified residue list.
    for r in get_mod_residues(ids):
      P = PTM()
      P.substrate = r.subject
      P.enzyme = ''
      if r.mod_id.find(':') > -1:
        P.modType = 'MOD' # need to be fix later
      P.seqPos = r.position
      P.aa = r.abbrev3
      P.source = 'pro'
      P.note = ''
      P.pmid = ''

      entries[r.subject].modification[P.seqPos].append(P)

    # update the ptm with kinase/acetylase/... from comment
    for r in get_enzymes(ids):
      # assert entries[r.subject].modification.has_key(r.position)
      for ptm in entries[r.subject].modification[r.position]:
        ptm.enzyme = {r.aggkey: r.obo_dbxref_description}
      entries[r.subject].enzyme.append(r.aggkey)
    # update the enzyme symbol list
    for id in entries.keys():
      entries[id].enzyme = list(set(entries[id].enzyme))

    # add pmids for each ptm
    evidence = defaultdict(list)
    for r in get_def_xref(ids):
      evidence[r.subject].append(r.object)

    for id in entries.keys():
      for pos in entries[id].modification.keys():
        for ptm in entries[id].modification[pos]:
          ptm.pmid = evidence[id]

    return entries

  @staticmethod
  def batch_seq(entries):
    # collect all xref:
    xrefList = []
    for e in entries.values():
      xrefList.extend(e.dbxrefs)
      print('xrefList in batch_seq: ',xrefList)
    # create a mapping between "UniProtKB:Q15796-2": "Q15796-2"
    acMap = {}
    for x in list(set(xrefList[:])):
      d = x.split(':')
      if d[0] == 'UniProtKB':
        acMap[x] = d[1] if not d[1].endswith('-1') else d[1][:-2]
    # load sequences
    seq = {}
    for r in get_seqs(acMap.values()):
      seq[r.subject] = Seq(r.sequence, IUPAC.protein)
    for ac in acMap.values():
      if ac not in seq:
        seq[ac] = Seq(get_seq_external(ac), IUPAC.protein)

    # add sequence to entry
    for e in entries.values():
      if len(e.dbxrefs) > 0:
        e.seq = seq[acMap[e.dbxrefs[0]]]

    return entries

#
# def check_fasta(seqRecord):
#   """Debug Func: print seqRecord's sequence in fasta format."""
#   print seqRecord.format("fasta")

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

def call_id_and_def(ids):
    query_id = pass_ids_for_query(ids)
    query = """
        PREFIX obo: <http://purl.obolibrary.org/obo/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        PREFIX has_gene_template: <http://purl.obolibrary.org/obo/pr#has_gene_template>
        PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
        PREFIX PR: <http://purl.obolibrary.org/obo/PR_>
        Select distinct *
         where {
            values ?PRO_term {
            """ + query_id + """
            }
            ?PRO_term oboInOwl:id ?id .
            ?PRO_term obo:IAO_0000115 ?PRO_termDef .
            }
        """
    sparqlSearch = SparqlSearch()
    IdAndDef, error = sparqlSearch.executeQuery(query)
    return IdAndDef

# done
def get_terms(ids):
    # subject, name, definition, category
    result = pass_node_info_by_ids(ids)
    term_list = []
    for case in result:
        robj = MvOboTerm()
        robj.subject = case['id']
        robj.name = case['name']
        robj.definition = case['PRO_termDef']
        CategoryAndComment = case['Category'].split('.')
        for cat in CategoryAndComment:
            if cat.find('Category=') != -1:
                category = cat.replace('Category=','')
                robj.category = category
                break
        term_list.append(robj)
    return term_list


def orgsyn(synonym):
    syndic = {}
    syn = ''
    std = ''
    for x in synonym:
        a = x.find('EXACT PRO-short-label')
        b = x.find('EXACT PRO-proteoform-std')
        if a >= 0:
            syn = x[2:(a - 2)]
        if b >= 0:
            std = x[1:(b - 2)]
    syndic['syn'] = syn
    syndic['std'] = std
    return syndic


# done
def get_short_label(ids):
    results = []
    robj = MvOboSynonym()
    for i in ids:
        robj.subject = i
        # nameset = []
        urlpatterns = "https://research.bioinformatics.udel.edu/PRO_API/V1/pros/" + i + "?showPROName=false&showPROTermDefinition=false&showCategory=false&showParent=false&showAnnotation=false&showAnyRelationship=false&showChild=false&showComment=false&showEcoCycID=false&showGeneName=false&showHGNCID=false&showMGIID=false&showOrthoIsoform=false&showOrthoModifiedForm=false&showPANTHERID=false&showPIRSFID=false&showPMID=false&showReactomeID=false&showSynonym=true&showUniProtKBID=false"
        infoset = requests.get(urlpatterns)
        jinfoset = infoset.json()
        info = jinfoset[0]
        # print('getshortlabel_jinfoset', jinfoset)
        # print('getshortlabel_info', info)
        syno = info['synonym']
        strt = ','.join(syno)
        strt = strt.split(';')
        synset = orgsyn(strt)
        shortname = synset['syn']
        p = shortname.find('/')
        shortname = shortname[:p]
        # nameset.append(shortname)
        robj.synonym_field = shortname
        results.append(robj)
    return results


# direct parent: get_all_direct_parent()

def get_direct_parent(id):
    parent = get_all_direct_parent(id)
    return parent

def get_children_and_taxon(id):
    childrenlist = []
    return childrenlist


# done
def get_sites(ids):
    IdAndDef = call_id_and_def(ids)
    results = []
    for i in IdAndDef:
        robj = MvOboModResidueCompress()
        id = i['id']
        tar = i['PRO_termDef']
        x = tar.find('Uni')
        tar = tar[x:]
        uni = tar.find(',')
        tar = tar[uni + 1:]
        p = tar.find('.')
        tar = tar[:p]
        robj.subject = id
        robj.residue = tar
        results.append(robj)

    return results
    # return MvOboModResidueCompress.objects.filter(subject__in=ids)


# done
def get_UniprotKB_ids(ids):

    id_set = ''
    for i in ids:
        i = i.replace(':', '_')
        id_set += 'obo:' + i + ' '

    query_prefix = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX obo: <http://purl.obolibrary.org/obo/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
            SELECT ?PRO_ID ?UNIPROTKB_ID
            WHERE
            {
              values ?PRO_term {"""

    query_tail = """} .
              ?PRO_term oboInOwl:id ?PRO_ID .
              ?PRO_term  oboInOwl:hasDbXref ?UNIPROTKB_ID .
            }"""

    query = query_prefix + id_set + query_tail
    sparqlSearch = SparqlSearch()
    resultss, error = sparqlSearch.executeQuery(query)



    uniprotkb = {}
    for xref in resultss:
        # search unirprotkb id by query
        if xref['UNIPROTKB_ID'].find("UniProtKB") != -1:
            uniprotkb[xref['PRO_ID']]  = xref['UNIPROTKB_ID']
        else:
            # search uniprotkb id in definition
            defurl = "https://research.bioinformatics.udel.edu/PRO_API/V1/pros/" + xref['PRO_ID'] + "?showPROName=true&showPROTermDefinition=true&showCategory=true&showParent=true&showAnnotation=false&showAnyRelationship=false&showChild=false&showComment=false&showEcoCycID=false&showGeneName=false&showHGNCID=false&showMGIID=false&showOrthoIsoform=false&showOrthoModifiedForm=false&showPANTHERID=false&showPIRSFID=false&showPMID=false&showReactomeID=false&showSynonym=true&showUniProtKBID=false"
            infoset = requests.get(defurl)
            jinfoset = infoset.json()
            info = jinfoset[0]
            tar = info['termDef']
            checklist = tar.split(' ')
            for i in checklist:
                if i.find('UniProtKB') != -1:
                    unid = i.replace('.','')
                    unid = unid.replace(',','')
                    uniprotkb[xref['PRO_ID']] = unid
                    break

    return uniprotkb


# done
def get_xrefs(ids):

    """this is update"""
    # id_set = ''
    # for i in ids:
    #     i = i.replace(':', '_')
    #     id_set += 'obo:' + i + ' '
    #
    # query_prefix = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
    # PREFIX obo: <http://purl.obolibrary.org/obo/>
    # PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    # PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    # PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
    # SELECT ?PRO_ID ?UNIPROTKB_ID
    # WHERE
    # {
    #   values ?PRO_term {"""
    #
    # query_tail = """} .
    #   ?PRO_term oboInOwl:id ?PRO_ID .
    #   ?PRO_term  oboInOwl:hasDbXref ?UNIPROTKB_ID .
    # }"""
    #
    # query = query_prefix + id_set + query_tail
    x1 = []
    x2 = []
    # sparqlSearch = SparqlSearch()
    # resultss, error = sparqlSearch.executeQuery(query)

    unids = get_UniprotKB_ids(ids)

    for id in ids:
        robj1 = MvOboRelationship()
        robj2 = MvOboUniprotXref()
        robj1.subject = id
        robj1.predicate = 'term_xref'
        robj1.object = 'UniProtKB'
        x1.append(robj1)
        if id in unids and unids[id] != '':
            robj2.subject = id
            robj2.object = unids[id]
            x2.append(robj2)

    return list(chain(x1,x2))


# done
def get_enzymes(ids):
    reuslts = []
    query_id = pass_ids_for_query(ids)
    query = """
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX has_gene_template: <http://purl.obolibrary.org/obo/pr#has_gene_template>
    PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
    PREFIX PR: <http://purl.obolibrary.org/obo/PR_>
    Select distinct *
     where {
        values ?PRO_term {
        """ + query_id + """
        }
        ?PRO_term oboInOwl:id ?id .
        ?PRO_term rdfs:comment ?Category .
        }
    """
    sparqlSearch = SparqlSearch()
    IdAndComment, error = sparqlSearch.executeQuery(query)

    for i in IdAndComment:
        enzymeString = i['Category']
        id = i['id']
        enzymes = None
        if enzymeString != '' and len(enzymeString) > 0:
            enzymes = re.findall(r'''
                                    ([a-zA-Z]*)=\(   #first group is type
                                    "([^"]*)"        #second group is name
                                    (?:;\ *
                                        ( [^\)\.\ ;]+:[^\)\.\ ;]+(?:;\ *[^\)\.\ ;]+:[^\)\.\ ;]+)*)   #third group is ; sep id list (requires:) (optional)
                                    )?
                                    (?:;\ *
                                        ([^;\)\.]*)     #fourth group is rest (optional)
                                    )?
                                    \)\.?
                                ''', enzymeString, re.VERBOSE | re.IGNORECASE)
        for x in enzymes:
            robj = MvOboEnzyme()
            site_num = x[3].count('/')
            sites = x[3]
            # print('enzyme check')
            for i in range(0, site_num + 1):
                robj.subject = id
                # print(id)
                robj.type = x[0]
                # print(x[0])
                robj.obo_dbxref_description = x[1]
                # print(x[1])
                robj.aggkey = x[2]
                # print('aggkey: ', x[2])
                po = sites.find('/')
                if po != -1:
                    tem = sites[:po]
                    sap = tem.index('-')
                    name = tem[:sap]
                    location = tem[sap + 1:]
                    # print('name: ',name)
                    robj.abbrev3 = name
                    # print('location: ', location)
                    robj.position = location
                    sites = sites[po + 1:]
                else:
                    tem = sites
                    sap = tem.index('-')
                    name = tem[:sap]
                    location = tem[sap + 1:]
                    # print('name: ', name)
                    robj.abbrev3 = name
                    robj.position = location
                    # print('location: ',location)
            reuslts.append(robj)

    # return MvOboEnzyme.objects.filter(subject__in=ids)
    return reuslts

def get_mod_residues(ids):
    results = []
    sitesset = []

    IdAndDef = call_id_and_def(ids)
    for i in IdAndDef:
        id = i['id']
        tar = i['PRO_termDef']
        x = tar.find('Uni')
        tar = tar[x:]
        uni = tar.find(',')
        uniprotid = tar[:uni]  # UniprotKB ID
        tar = tar[uni + 1:]
        sit = tar.find(',')
        sites = tar[:sit]
        p_mods = tar.find('MOD')
        if p_mods != -1:
            mods = tar[p_mods:p_mods+9]
        else:
            mods = ''

        for w in range(0, len(sites)):
            # for site in sites.split('/'):
            #     sitesset
            num = sites.find('/')
            if w == num:
                sitesset.append(sites[:w])
                sites = sites[w + 1:]
            elif num == -1:
                sitesset.append(sites)
                break
        # print('sitesset: ', sitesset)
        # sitesset is sites
    for x in sitesset:
        robj = MvOboModResidue()
        if x.find('UniProt') != -1:
            print('continue for current sites')
            continue
        else:
            print('excuate for current sites: ', x)
            saparator = x.find('-')
            if saparator != -1:
                name = x[:saparator]
                position = x[saparator + 1:]
                robj.subject = id
                print('find_position_id: ', id)
                print(('find_position_resources'), x)
                robj.abbrev3 = name
                print('position is :', position)
                if position.find('.')!= -1:
                    rest = position.find('.')
                    position = position[:rest]
                    print('after position is :', position)
                robj.position = int(position)
            #print(x + " | " +position)
                robj.mod_id = mods
                print('fetch.py get_mod_residues, ', id, name, int(position), mods)
            #print(x + " || "+robj.position)
                results.append(robj)
            else:
                continue
        #print(check)
        #print(testresults)
    # print('get_siteshahaha')
    # for r in results:
    #     print(r.subject+" "+r.abbrev3+ " "+r.position+"\n")
    #print([r.position for r in results])
    return results

    # return MvOboModResidue.objects.filter(subject__in=ids)



def get_def_xref(ids):
    results = []
    IdAndXref = get_xref_by_ids(ids)
    for i in IdAndXref:
        robj = MvOboRelationship()
        id = i['id']
        tar = i['DbRef']
        robj.subject = id
        robj.object = tar
        results.append(robj)
    return results
    # return MvOboRelationship.objects.filter(Q(subject__in=ids) & Q(predicate='def_xref')).only('subject', 'object')




# def get_seqs(ids):
#     # input ids is a dictionary
#     print('input ids for get_seqs', ids)
#     # newids = []
#     # for id in ids:
#     #     id = 'PR:' + id
#     #     newids.append(id)
#     # uniprotset = ids
#     seqs = []
#     for id in ids:
#         robj = Sequence()
#         unid = id
#         # p = unid.find(':')
#         # funid = unid[(p + 1):]
#         raw = (urllib.urlopen('http://www.uniprot.org/uniprot/' + unid + '.fasta?')).readlines()
#         print('sequence_source: ', raw)
#         # for seq in raw:
#         #     if seq != '':
#         #         print('seqid: ', unid)
#         #         print(seq)
#         seq = ''.join(raw[1:]).replace('\n', '')
#         robj.subject = id
#         robj.sequence = seq
#         seqs.append(robj)
#
#     return seqs
#     # return Sequence.objects.filter(subject__in=ids)
#
#
# def get_seq_external(id):
#     print('input ids for get_seqs_external', id)
#     raw = (urllib.urlopen('http://www.uniprot.org/uniprot/' + id + '.fasta')).readlines()
#     seq = ''.join(raw[1:]).replace('\n', '')
#     return seq
def get_seqs(ids):
    # input ids is a dictionary
    # newids = []
    # for id in ids:
    #     id = 'PR:' + id
    #     newids.append(id)
    # uniprotset = ids
    print('input for get_Seqs: ',ids)
    seqs = []
    for id in ids:
        robj = Sequence()
        unid = id
        result = requests.get('http://www.uniprot.org/uniprot/' + unid + '.fasta').text
        raw = result.split('\n')
        seq = ''.join(raw[1:])
        if seq.find('>')>0:
            seq = seq[:seq.find('>')]
        robj.subject = id

        robj.sequence = seq
        seqs.append(robj)
        # print(id,seq)
    return seqs

def get_seq_external(id):
    print('input for get_seq_external: ', id)
    result = requests.get('http://www.uniprot.org/uniprot/' + id + '.fasta').text
    raw = result.split('\n')
    seq = ''.join(raw[1:])

    return seq


def query_taxon_forone(id):
    oboid = id.replace(':', '_')
    oboid = "obo:" + oboid
    query = """PREFIX obo: <http://purl.obolibrary.org/obo/>  
    PREFIX paf: <http://pir.georgetown.edu/pro/paf#>  
    PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> 

    SELECT  *
    from <http://purl.obolibrary.org/obo/pr>
    where {
      values ?PRO_term {""" + oboid + """} .
      ?PRO_term rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty obo:RO_0002160 ;
    owl:someValuesFrom ?ncbi] .
    ?ncbi
    oboInOwl:id ?NCBITaxon_ID .
    }"""
    TaxonID = ''
    sparqlSearch = SparqlSearch()
    resultss, error = sparqlSearch.executeQuery(query)
    for i in resultss:
        # print(i['NCBITaxon_ID'])
        NCBITaxon_ID = i['NCBITaxon_ID']
        p = NCBITaxon_ID.index(':')
        TaxonID = NCBITaxon_ID[p + 1:]
    return TaxonID


def get_taxon(id):
    TaxonID = query_taxon_forone(id)
    robj = MvTaxonomy()
    robj.subject = id
    # taxon = MvTaxonomy.objects.filter(subject=id)
    robj.taxonomy = TaxonID
    return robj.taxonomy