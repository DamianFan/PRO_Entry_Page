import requests
import json
import re
import urllib

from msa.models import *

ROOT=["PR:000000001","PR:000018264","GO:0043234","PR:000037070","PR:000036194", "PR:000029067"]
DELROOT = ["PR:000018263","GO:0032991","CHEBI:23367"]


class DAO:

    def __init__(self, proId):
        self.proId = proId

        url = "https://research.bioinformatics.udel.edu/PRO_API/V1/dag/hierarchy/" + proId + "?showPROName=true&showPROTermDefinition=true&showCategory=true&showAnnotation=true&showAnyRelationship=true&showComment=true&showEcoCycID=true&showGeneName=true&showHGNCID=true&showMGIID=true&showOrthoIsoform=true&showOrthoModifiedForm=true&showPANTHERID=true&showPIRSFID=true&showPMID=true&showReactomeID=true&showSynonym=true&showTaxonID=true&showUniProtKBID=true"
        response = requests.get(url)
        self.data = json.loads(response.text)
        # print(self.data[0]['pro']['category'])
        self.parent = {}
        for data in self.data:
            pro = data['pro']['id']
            pro_parent = data['pro_parent']['id']
            self.parent[pro] = pro_parent

    def get_dao(self):
        return self.data

    def get_terms(self, ids):
        #print("get_terms: "+str(ids))
        # subject, name, definition, category
        # result = pass_node_info_by_ids(ids)
        terms = []
        for data in self.data:
            pro = data['pro']
            if pro['id'] in ids:
                oboTerm = MvOboTerm()
                oboTerm.subject = pro['id']
                oboTerm.name = pro['name']
                oboTerm.definition = pro['termDef']
                oboTerm.category = pro['category']
                terms.append(oboTerm)
        return terms

    def get_direct_parent(self, id):
        parents = []
        for data in self.data:
            pro = data['pro']
            if pro['id'] == id:
                if data['pro_parent']['id'] not in ROOT:
                    parent = data['pro_parent']['id']
                    parents.append(parent)
                else:
                    continue
        return parents

    def get_taxon(self, id):
        #print("get_taxon: "+ id)
        for data in self.data:
            pro = data['pro']
            if pro['id'] == id:
                #print(id)
                if 'taxonID' in pro.keys():
                    #print(pro['taxonID'].replace("NCBITaxon:", ""))
                    return pro['taxonID'].replace("NCBITaxon:", "")
            #taxon = MvTaxonomy.objects.filter(subject=id)
            #     return taxon[0].taxonomy if taxon else None
        return None

    # def find_children(pro, pro_parent):
    #     if self.parent[pro] == pro_parent or self.parent[pro] == "PR:000018263":
    #         return pro_parent
    #     else:
    #         pro = self.parent[pro]
    #         return self.find_children(pro, pro_parent)

    # def get_children(self, id, sameTaxon, taxon):
    #     children = []
    #     for data in self.data:
    #         pro = data['pro']['id']
    #         child = self.find_children(pro, id)
    #         children.append(child)
    def get_children1(self, id, sameTaxon, taxon):
        children = []
        for data in self.data:
            if data['pro_parent']['id'] == id:
                children.append(data['pro']['id'])
        children = list(set(children))
        #print(children)
        return children

    def get_children(self, id, sameTaxon, taxon):
        ids = (' ').join(id)
        url = "https://research.bioinformatics.udel.edu/PRO_API/V1/dag/descendant/"+id+"?showTaxonID=true"
        #url = "https://research.bioinformatics.udel.edu/PRO_API/V1/dag/children/"+ids+"?showTaxonID=true"
        #print(url)
        # print(url)
        response = requests.get(url)
        data = json.loads(response.text)
        if data == []:
            children = []
        else:
            children = [id]
        for child in data:
            # print('this is child in dao.children',child)
            pro_taxon = None
            pro_descendant_taxon = None
            pro = child['pro']['id']
            if  child['pro'].has_key("taxonID"):
                pro_taxon  = child['pro']['taxonID'].replace('NCBITaxon:','')
            pro_descendant = child['pro_descendant']['id']
            if child['pro_descendant'].has_key("taxonID"):
                pro_descendant_taxon = child['pro_descendant']['taxonID'].replace('NCBITaxon:','')
            if sameTaxon:
                if taxon is not None:
                    if pro_descendant_taxon == taxon:
                        if pro_descendant not in children:
                            children.append(pro_descendant)
                else:
                    if pro_descendant not in children:
                        children.append(pro_descendant)
            else:
                if pro_descendant not in children:
                    children.append(pro_descendant)
        children = list(set(children))
        #print(children)
        return children

    def get_short_label(self, ids):

        # print("short label "+str(ids))
        short_labels = []
        for data in self.data:
            pro = data['pro']
            if pro['id'] in ids:
                synonym = pro['synonym']
                # print(type(synonym))
                for syn in synonym.replace("'", "").split("; "):
                    syn = syn.replace('[', '').replace(']', '').replace('"', '')
                    if " EXACT PRO-short-label" in syn:
                        #print(syn)
                        oboSynonym = MvOboSynonym()
                        oboSynonym.subject = pro['id']
                        oboSynonym.synonym_field = syn.split(' EXACT PRO-short-label', 1)[0]
                        short_labels.append(oboSynonym)
        #print(short_labels)
        return short_labels

    def get_sites(self, ids):
        # print(ids)
        sites = []
        for data in self.data:
            pro = data['pro']
            if pro['id'] in ids:
                synonym = pro['synonym']
                # print(type(synonym))
                for syn in synonym.replace("'", "").split("; "):
                    if (" MOD:" in syn): #or (" CHEBI:" in syn):
                        # print(syn)
                        oboModResidue = MvOboModResidueCompress()
                        oboModResidue.subject = pro['id']
                        residue = syn.split('" ', 1)[0].replace("'", "").replace('"', '').replace('[', '')
                        residue = ', '.join(word for word in residue.split(', ') if not word.startswith('UniProtKB:'))
                        oboModResidue.residue = residue
                        # print(residue)
                        sites.append(oboModResidue)
        sites = list(dict.fromkeys(sites))
        return sites


#     return MvOboModResidueCompress.objects.filter(subject__in=ids)

    def get_xrefs(self, ids):
        #print(ids)
        xrefs = []

        for data in self.data:
            pro = data['pro']
            if pro['id'] in ids:
                uniprots = []
                if 'uniprotKBID' in pro.keys():
                    uniprotIds = data['pro']['uniprotKBID']
                    for uniprot in uniprotIds:
                        if len(uniprot) > 0:
                            uniprots.append(uniprot)
                termDef = pro['termDef']
                for word in termDef.split(' '):
                    if word.startswith('UniProtKB:'):
                        uniprots.append(word.replace(',','').replace('.','').replace(']',''))
                if len(uniprots) == 0:
                    pro_parent = data['pro_parent']
                    if pro_parent['id'] in ids:
                        if 'uniprotKBID' in pro_parent.keys():
                            uniprotIds = data['pro_parent']['uniprotKBID']
                            for uniprot in uniprotIds:
                                if uniprot is not None:
                                    uniprots.append(uniprot)
                    termDef = pro_parent['termDef']
                    for word in termDef.split(' '):
                        if word.startswith('UniProtKB:'):
                            uniprot = word.replace(',','').replace('.','').replace(']','')
                            if len(uniprot) > 0:
                                uniprots.append(uniprot)
                uniprots = list(set(uniprots))
                for uniprot in uniprots:
                    #if len(uniprot) > 0:
                    oboUniProt = MvOboUniprotXref()
                    oboUniProt.subject = pro['id']
                    oboUniProt.object = uniprot
                    #print("??? "+pro['id']+ "|"+ uniprot)
                    xrefs.append(oboUniProt)
        xrefs = list(dict.fromkeys(xrefs))
        return xrefs


    def get_xrefs1(self, ids):
        # x1 = MvOboRelationship.objects.filter(
        #     Q(subject__in=ids) & Q(predicate='term_xref') & Q(object__startswith='UniProtKB'))
        # x2 = MvOboUniprotXref.objects.filter(subject__in=ids)
        # return list(chain(x1, x2))
        #print("get_xrefs:")
        #print(str(ids))
        xrefs = []
        for data in self.data:
            pro = data['pro']

            if pro['id'] in ids:
                #print(pro)
                if 'uniprotKBID' in pro.keys():
                    uniprotIds = data['pro']['uniprotKBID']
                    #print("len1: "+ str(len(uniprotIds)))
                    for uniprot in uniprotIds:
                        if len(uniprot) > 0:
                            oboUniProt = MvOboUniprotXref()
                            oboUniProt.subject = pro['id']
                            oboUniProt.object = uniprot
                            xrefs.append(oboUniProt)
                if len(xrefs) == 0:
                    pro_parent = data['pro_parent']
                    #print(pro_parent)
                    if 'uniprotKBID' in pro_parent.keys():
                        #print(type(uniprot))
                        uniprotIds = data['pro_parent']['uniprotKBID']
                        #print("len2: " + str(len(uniprotIds)))
                        for uniprot in uniprotIds:
                            if len(uniprot) > 0:
                                oboUniProt = MvOboUniprotXref()
                                oboUniProt.subject = pro['id']
                                oboUniProt.object = uniprot
                                #print(oboUniProt.object)
                                xrefs.append(oboUniProt)
        #xrefs = list(dict.fromkeys(xrefs))
        return xrefs

    def get_mod_residues(self, ids):
        #print(ids)
        #return MvOboModResidue.objects.filter(subject__in=ids)
        mod_residues = []
        for data in self.data:
            pro = data['pro']
            if pro['id'] in ids:
                synonym = pro['synonym']
                #print("original synoym: " + synonym)
                synonym = synonym.replace("[", "").replace("]", "")
                #print(pro['id'] + " original synoym cleaned: " + synonym)
                for syn in synonym.split("; "):
                    if ("MOD:" in syn): #or ("CHEBI:" in syn):
                        #print("synonym: " + syn)
                        residue = syn.split('" ', 1)[0].replace("'", "").replace('"', '').replace('[', '')
                        residue = ', '.join(word for word in residue.split(', ') if not word.startswith('UniProtKB:'))
                        #UniProtKB:O43521-2, Ser-44/Ser-58, MOD:00046|Thr-56, MOD:00047.
                        #oboModResidue.residue = residue
                        #Ser-44/Ser-58, MOD:00046|Thr-56, MOD:00047
                        #print("residue: "+ residue)

                        for res in residue.split("|"):
                            #print("res: "+res)
                            if ", " in res:
                                if "-" in res:
                                    mod_res = res.split(', ')[0]
                                    mod_id = res.split(', ')[1]
                                    for abbrev in mod_res.split('/'):
                                        if "-" in abbrev:
                                            #print("abbrev: "+abbrev)
                                            abbrev3 = abbrev.split('-')[0]
                                            position = abbrev.split('-')[1]
                                            oboModResidue = MvOboModResidue()
                                            oboModResidue.subject = pro['id']
                                            oboModResidue.abbrev3 = abbrev3
                                            oboModResidue.position = int(position)
                                            oboModResidue.mod_id = mod_id
                                            mod_residues.append(oboModResidue)
        mod_residues = list(dict.fromkeys(mod_residues))
        #print(mod_residues)
        return mod_residues

    def get_enzymes(self, ids):
        enzymes = []
        for data in self.data:
            pro = data['pro']
            if pro['id'] in ids:
                comment = pro['comment']

                regex = r"(Kinase|Acetylase|UbLigase)=\(\"([a-zA-Z0-9\: ]+)\"; (PR\:\w+)(; (\w+)\-(\d+)(\/(\w+)\-(\d+))*)*\)"
                matches = re.findall(regex, comment)
                for match in matches:
                    oboEnzyme = MvOboEnzyme()
                    oboEnzyme.subject = pro['id']
                    oboEnzyme.type = match[0]
                    oboEnzyme.obo_dbxref_description = match[1]
                    oboEnzyme.aggkey = match[2]
                    if len(match) > 3:
                        sites = match[3].replace('; ', '')
                        for site in sites.split('/'):
                            oboEnzyme.abbrev3 = site.split('-')[0]
                            oboEnzyme.position = site.split('-')[1]
                    enzymes.append(oboEnzyme)
                    #     print(sites)
                    # print(comment)
                    # print("0:" + match[0])
                    # print("1:" + match[1])
                    # print("2:" + match[2])
                    # print("3:" + match[3])
                #Category=organism-modification. Kinase=("BAK1"; PR:Q94F62; Thr-1180). Kinase=("BRI1"; PR:O22476; Thr-1180). Evidence=(ECO:0000181, for kinase information).
            #Kinase=\(\"(\w+)\"; (PR\:\w+)(; (\w+)\-(\d+)(\/(\w+)\-(\d+))*)*\)
        #enzymes = list(dict.fromkeys(enzymes))
        #print(enzymes)
        return enzymes
        #return MvOboEnzyme.objects.filter(subject__in=ids)

    def get_def_xref(self, ids):
        xrefs = []
        relation ={}
        for data in self.data:
            pro = data['pro']
            if pro['id'] in ids:
                #print(pro['id'])
                termDef = pro['termDef']
               # print(termDef)
                regex = r"\[(.*?)\]"
                matches = re.findall(regex, termDef)
                for match in matches:
                    #print(match)
                    for dbref in match.split('; '):
                        #print(dbref)
                        if pro['id'] in relation:
                            if dbref not in relation[pro['id']]:
                                relation[pro['id']].append(dbref)
                        else:
                            relation[pro['id']] = []
                            relation[pro['id']].append(dbref)
                        # oboRelationship = MvOboRelationship()
                        # oboRelationship.subject = pro['id']
                        # oboRelationship.object = dbref
        for proId in relation:
            for ref in relation[proId]:
                oboRelationship = MvOboRelationship()
                oboRelationship.subject = proId
                oboRelationship.object = ref
                xrefs.append(oboRelationship)
        #print(relation)
        #xrefs = list(dict.fromkeys(xrefs))
        #print(xrefs)
        return xrefs
        #return MvOboRelationship.objects.filter(Q(subject__in=ids) & Q(predicate='def_xref')).only('subject', 'object')

    def get_seqs(self, ids):
        #return Sequence.objects.filter(subject__in=ids)
        return None

    def get_seq_external(self, id):
        raw = (urllib.urlopen('http://www.uniprot.org/uniprot/' + id + '.fasta')).readlines()
        seq = ''.join(raw[1:]).replace('\n', '')
        #print(id)
        #print(seq)
        return seq
