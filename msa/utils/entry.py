from msa.utils.fetch import *
from msa.utils.event_ptm import PTM

import os
import csv
from collections import defaultdict
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC

mod = {}
with open(os.path.join(os.path.dirname(__file__), 'mod.txt'), 'r') as csvfile:
  f = list(csv.reader(csvfile, delimiter='\t'))
  for l in f:
    mod[l[0]] = l[1]


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

  def __str__(self):
    str = "["
    str += "id: "+self.id +"; "
    str += "seq: "+self.seq +"; "
    str += "name: "+self.name + "; "
    str += "definition: "+self.definition+ "; "
    str += "description: "+self.description+"; "
    #str += "dbxrefs: "+str(self.dbxrefs)+"; "
    str += "Cat: "+ self.Cat + "; "
    str += "Group: "+ self.Group+"; "
    str += "modification: ["
    for mod in self.modification:
      str += self.modification[mod]+"; "
    str += "]"
    str += "enzyme: "+ str(self.enzyme)+"; "
    str += "pmid: "+ str(self.pmid)+"; "
    str += "]"

  def generate_seqrecords(self):
    """
    Create seqRecords object for each entry. Return seqRecord object.
    annotations: a dict with two keys:
        1 "relationship": store Group attribute, a string
        2 "modification": store modification attribute, a dict
        3."definition": store PRO def
    """

    #print(self.__unicode__())
    record = SeqRecord(self.seq, id=self.id, name=self.name,
                       description=self.description, dbxrefs=self.dbxrefs,
                       annotations={"relationship": self.Group,
                                    "modification": self.modification,
                                    "definition": self.definition})
    return record

  @staticmethod
  def batch_initial(dao, ids, full=True):
    #print("batch_initial:")
    #print(str(ids))
    #print(full)

    """
     if full==True: collect entry, sequence and all modification data
     if full==False: only collect entry data
     """
    entries = {}
    # build entries object
    for id in ids:
      #entries[id] = ENTRY(id)
      #print("batch initial: ", type(id), " ", id)
      if type(id) is list:
        for pro_id in id:
          #print(pro_id)
          entries[pro_id] = ENTRY(pro_id)
      else:
        entries[id] = ENTRY(id)

    for r in dao.get_short_label(ids):
      entries[r.subject].name = r.synonym_field

    for r in dao.get_terms(ids):
      if entries[r.subject].name == '':
        entries[r.subject].name = r.name
      entries[r.subject].definition = r.definition
      entries[r.subject].Cat = r.category

    for r in dao.get_sites(ids):
      entries[r.subject].description = r.residue

    for r in dao.get_xrefs(ids):
      #print("get_xref: "+r.subject+ " | "+r.object)
      if r.object.startswith('UniProtKB:'):
        entries[r.subject].dbxrefs.append(r.object)

    if full:
      entries = ENTRY.batch_mod(dao, ids, entries)
      entries = ENTRY.batch_seq(dao, entries)

    #print(type(entries.values()))
    return entries.values()

  @staticmethod
  def batch_mod(dao, ids, entries):
    # get ptms from definition modified residue list. 
    for r in dao.get_mod_residues(ids):
      P = PTM()
      P.substrate = r.subject
      P.enzyme = ''
      if r.mod_id.find(':') > -1:
        #print(r.mod_id)
        P.modType = mod[r.mod_id.split(':')[1]]
      P.seqPos = r.position
      P.aa = r.abbrev3
      P.source = 'pro'
      P.note = ''
      P.pmid = ''
      #print(P)
      entries[r.subject].modification[P.seqPos].append(P)

    # update the ptm with kinase/acetylase/... from comment
    for r in dao.get_enzymes(ids):
      # assert entries[r.subject].modification.has_key(r.position)
      for ptm in entries[r.subject].modification[r.position]:
        ptm.enzyme = {r.aggkey: r.obo_dbxref_description}
      entries[r.subject].enzyme.append(r.aggkey)
    # update the enzyme symbol list
    for id in entries.keys():
      entries[id].enzyme = list(set(entries[id].enzyme))

    # add pmids for each ptm
    evidence = defaultdict(list)
    for r in dao.get_def_xref(ids):
      #print("entry get_def_xref: "+ r.subject+ " | "+ r.object)
        if not r.object in evidence[r.subject]:
          evidence[r.subject].append(r.object)

    for id in entries.keys():
      for pos in entries[id].modification.keys():
        for ptm in entries[id].modification[pos]:
          ptm.pmid = evidence[id]

    return entries

  @staticmethod
  def batch_seq(dao, entries):
    # collect all xref: 
    xrefList = []
    for e in entries.values():
      #print("dbxref: " + e.id + " | " + str(e.dbxrefs))
      xrefList.extend(e.dbxrefs)
    # create a mapping between "UniProtKB:Q15796-2": "Q15796-2"
    acMap = {}
    for x in list(set(xrefList[:])):
      d = x.split(':')
      if d[0] == 'UniProtKB':
        acMap[x] = d[1] if not d[1].endswith('-1') else d[1][:-2]
    # for x in acMap:
    #   print(x + " <|> "+acMap[x])
    # load sequences 
    seq = {}
    # for r in dao.get_seqs(acMap.values()):
    #   seq[r.subject] = Seq(r.sequence, IUPAC.protein)
    for ac in acMap.values():
      if not seq.has_key(ac):
        #print(ac)
        seq[ac] = Seq(dao.get_seq_external(ac), IUPAC.protein)
        #print(ac + " | " + dao.get_seq_external(ac))

    # add sequence to entry
    for e in entries.values():
      #print(e)
      if len(e.dbxrefs) > 0:
        e.seq = seq[acMap[e.dbxrefs[0]]]
        #print(e.id + " | seq: " + e.seq)

    return entries


def check_fasta(seqRecord):
  """Debug Func: print seqRecord's sequence in fasta format."""
  print seqRecord.format("fasta")
