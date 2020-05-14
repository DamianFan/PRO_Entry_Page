from .models import *
from database.sparql import SparqlSearch
from database.fetch import *
from .collect import *
import urllib
from itertools import chain
import json



# get direct parent: done
# get children: need to fix xref
# get terms : should be done
# get short label
# get sites
# get xrefs
# get enzymes
# get mod residues
# get xrefs
# get seqs
# get seqs external

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
            print('get xref from query')
            uniprotkb[xref['PRO_ID']]  = xref['UNIPROTKB_ID']
        else:
            print('query has no uniprotkb xref')
            # search uniprotkb id in definition
            defurl = "https://research.bioinformatics.udel.edu/PRO_API/V1/pros/" + xref['PRO_ID'] + "?showPROName=true&showPROTermDefinition=true&showCategory=true&showParent=true&showAnnotation=false&showAnyRelationship=false&showChild=false&showComment=false&showEcoCycID=false&showGeneName=false&showHGNCID=false&showMGIID=false&showOrthoIsoform=false&showOrthoModifiedForm=false&showPANTHERID=false&showPIRSFID=false&showPMID=false&showReactomeID=false&showSynonym=true&showUniProtKBID=false"
            infoset = requests.get(defurl)
            jinfoset = infoset.json()
            info = jinfoset[0]
            tar = info['termDef']
            if tar.find('UniProtKB') != -1:
                pos = tar.find('UniProtKB')
                tar = tar[pos:tar.find(',')]
                uniprotid = tar

                uniprotkb[xref['PRO_ID']] = uniprotid



    return uniprotkb


# done
def get_xrefs(ids):

    """this is update"""

    x1 = []
    x2 = []


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
#         unid = ids[id]
#         # p = unid.find(':')
#         # funid = unid[(p + 1):]
#         raw = (urllib.urlopen('http://www.uniprot.org/uniprot/' + unid + '.fasta?include=yes')).readlines()
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
    seqs = []
    for id in ids:
        robj = Sequence()
        unid = ids[id]
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


def check_uni(ids):
    query_id = pass_ids_for_query(ids)
    query = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
    SELECT ?PRO_ID ?UNIPROTKB_ID
    WHERE
    {
      values ?PRO_term {"""+query_id+"""
    } .
      ?PRO_term oboInOwl:id ?PRO_ID .
      ?PRO_term  oboInOwl:hasDbXref ?UNIPROTKB_ID .
    }
    
    """
    sparqlSearch = SparqlSearch()
    resultss, error = sparqlSearch.executeQuery(query)

    return resultss