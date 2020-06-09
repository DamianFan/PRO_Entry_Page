import time
import csv
import database.root_setting as g
from database.sparql import SparqlSearch
import request
import requests
import re
import msa.models as ma
hierarchy_root = g.ROOT+g.DELROOT
import os

mod = {}
with open(os.path.join(os.path.dirname(__file__), 'mod.txt'), 'r') as csvfile:
  f = list(csv.reader(csvfile, delimiter='\t'))
  for l in f:
    mod[l[0]] = l[1]


aminodict = {'Ala':'A','Arg':'R','Asn':'N','Asp':'D','Cys':'C','Gln':'Q','Glu':'E','Gly':'G','His':'H','Ile':'I','Leu':'L','Lys':'K','Met':'M','Phe':'F','Pro':'P','Pyl':'O','Ser':'S','Sec':'U','Thr':'T','Trp':'W','Tyr':'Y','Val':'V','Asx':'B','Glx':'Z','Xaa':'X','Xle':'J'}

"""General Utilities"""

def time_check():
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    return ''

def check_ids(ids):
    set = []
    for i in ids:
        if i != '':
            id = i.replace(' ','')
            set.append(id)
    return set

def modify_sparql_id(id):
    # change PRO URL into PRO ID, start with 'PR:'
    id = id.replace(' ','')
    target = id[31:]
    proid = target.replace('_', ':')
    return proid

def change_idlist_into_queryid(ids):
    query_id = ''
    ids = check_ids(ids)
    for i in ids:
        if i in hierarchy_root:continue
        else:
            i = i.replace(':','_')
            query_id += ('obo:' + i + ' ')
    return query_id

def seperate_ids_for_api(ids):
    urlset = []
    query_id = ''
    # check numbers
    if len(ids) <= 30:
        for i in ids:
            query_id += i + ' '
        urlset.append(query_id)
    else:
        query_ids = []
        for i in range(0, len(ids), 30):
            query_ids.append(ids[i:i + 30])
        for i in query_ids:
            query_id = ''
            for j in i:
                query_id += j + ' '
            urlset.append(query_id)
    return urlset

def pass_ids_for_query(ids):
    query_id = ''
    for i in ids:
        id = i.replace(':','_')
        id = id.replace(' ','')
        curid = 'obo:' + id + ' '
        query_id += curid
    return query_id

"""Term Information"""

def get_node_info_by_ids(ids):
    # return node info for max 30 ids by api
    # ids is a list
    # check numbers
    results = []
    information = pass_node_info_by_ids(ids)
    for info in information:
        results.append(pass_pro_term(info))
    return results

def get_url(ids, type):
    """
    Generate URL for PRO batch retrival.
    Type could be 'OBOEXACT' or 'PAFEXACT'. URL define in setting.py
    """

    if type in g.URL:
        url = g.URL[type]
    else:
        return
    for id in ids:
        url += '&idlist=' + id
    return url

def get_level(ids, nodes):
  """Collect all Level attribute in 'ids', return a sorted integer list of the Level value."""
  return sorted(map(int,set([nodes[id].Level for id in ids])))

def get_children_menu(lst,requestIds, nodes):
  """
  Return a Level list containing integer bigger than requestIds' Level.
  In protein hierarchy, the returned Levels belongs to more specific terms.
  """
  return [l for l in get_level(lst, nodes) if l>=max(get_level(requestIds, nodes)) and not (l==0 or l==1)]


def get_cate_by_id(id):
    # return category of one id
    category = ''
    query_id = 'obo:' + id.replace(':', '_')
    query = """
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX obo: <http://purl.obolibrary.org/obo/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
            SELECT ?Category
            WHERE
            {
                values ?PRO_term {""" + query_id + """} .
                ?PRO_term rdfs:comment ?_Category .
                FILTER (regex(?_Category,"Category=.*"))
                BIND(strafter(strbefore(str(?_Category), "."), "=") as ?Category) .
            }
            """
    sparqlSearch = SparqlSearch()
    result, error = sparqlSearch.executeQuery(query)
    for i in result:
        category = i['Category']
    return category

def get_category_by_ids(ids):
    # return a dict of categories by a list of id
    queryid = pass_ids_for_query(ids)
    query = """
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX obo: <http://purl.obolibrary.org/obo/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
        SELECT ?id ?Category
        WHERE
        {
            values ?PRO_term {""" + queryid + """} .
            ?PRO_term oboInOwl:id ?id .
            ?PRO_term rdfs:comment ?_Category .
            FILTER (regex(?_Category,"Category=.*"))
            BIND(strafter(strbefore(str(?_Category), "."), "=") as ?Category) .
        }
        """

    sparqlSearch = SparqlSearch()
    IdAndCategory, error = sparqlSearch.executeQuery(query)
    return IdAndCategory



def pass_pro_term(jsondata):
    # PROTerm: 0 id  1 Name  2 Def  3 Category  4 Label  5 Mapping  6 Shape  7 ptm 8(add by zida) Group
    # 0 id  1 Name  2 Def  3 Category  4 Label  5 Sites  6 Mapping  7 Shape  8 ptm 9	evidence
    # jsonexample {u'category': u'organism-gene', u'comment': u'Category=organism-gene.', u'termDef': u'A smad2 that is encoded in the genome of mouse. [UniProtKB:Q62432]', u'id': u'PR:Q62432', u'name': u'mothers against decapentaplegic homolog 2 (mouse)'}
    id = ''
    Name = ''
    Def = ''
    Category = ''
    Label = ''
    Mapping = ''
    Sites = ''
    Shape = ''
    ptm = ''
    # Group = ''
    evidence = ''  # this column exits in SQLite table, but hasn't been used at this function
    site = ''
    if 'id' in jsondata:
        id = jsondata['id']
        if id.startswith(r'CHEBI'):
            Shape = 'CHEBI'
    if 'name' in jsondata:
        Name = jsondata['name']
        Label = Name
    if 'PRO_termDef' in jsondata:
        Def = jsondata['PRO_termDef']
        defset = Def.split('|')
        for d in defset:
            dd = d.split('.')
            for modresidue in dd:
                if modresidue.find('MOD:') != -1:
                    submod = modresidue.split(',')
                    modtype = ''
                    sitelist = []
                    for subsubmod in submod:
                        if subsubmod.find('UniProtKB:') == -1:
                            # modtype = ''
                            # sitelist = []
                            if subsubmod.find('MOD:') !=-1:
                                # print('check subsubmod in fetch', subsubmod)
                                if subsubmod.find('or') != -1:
                                    locateminusone = subsubmod.find('or')
                                    subsubmod = subsubmod[:locateminusone]
                                subsubmod = subsubmod.replace(')','')
                                # print('check subsubmod in fetch',subsubmod)
                                modid = subsubmod.replace('MOD:','')
                                modid = modid.replace(' ','')
                                modtype = mod[modid]
                            else:
                                sitelist = subsubmod.split('/')
                            if modtype != '' and sitelist != []:
                                for outputsite in sitelist:
                                    site += modtype + outputsite.replace(' ','') + ','
                                    # else:
                                    #     site += modtype + outputsite.replace(' ','') + ','
    if 'Category' in jsondata:
        Category = ''
        tem_category = jsondata['Category']
        match = re.search(r'Category=((organism-)?(.*?))\.', tem_category)
        if match:
            Category = match.group(1)
        if Category.find('complex') > -1: Shape = 'complex'
    if 'synonym' in jsondata:
        if Name.find('complex') > -1 or Category.find('complex') > -1 or id.find('CHEBI') > -1:
            Label = Name
        else:
            synonym = jsondata['synonym'].split(';')
            for syns in synonym:
                if syns.find('PRO') != -1: continue
                # if syns.find('EXACT PRO-short-label') != -1:
                #     j = syns.split(' ')
                #     Label = j[1].replace('"', '')
                # elif syns.find('UniProtKB') == -1 and syns.find('(') == -1:
                #     Label = syns
                if len(syns) < len(Label):
                    Label = syns
    if Label == '':
        Label = Name
    if site != '':
        Label = Label + '(' + site + ')'
    result_list = [id,Name,Def,Category,Label,Sites,Mapping,Shape,ptm,evidence]
    return result_list

def get_name_by_ids(ids):
    namedict = {}
    query_id = pass_ids_for_query(ids)
    query = """
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX has_gene_template: <http://purl.obolibrary.org/obo/pr#has_gene_template>
    PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
    PREFIX PR: <http://purl.obolibrary.org/obo/PR_>
    Select distinct ?id ?name 
    where {
    values ?PRO_term {
    """ + query_id + """
    }
    ?PRO_term oboInOwl:id ?id .
    ?PRO_term rdfs:label ?name .
    }
    """
    sparqlSearch = SparqlSearch()
    information, error = sparqlSearch.executeQuery(query)
    for i in information:
        tid = i['id']
        tname = i['name']
        namedict[tid] = tname
    return namedict

def process_addition(ids,relations):
    get_compoment = []
    get_complex = []
    get_parent = []
    complex = []
    component = []
    IdAndCategory = get_category_by_ids(ids)

    for i in IdAndCategory:
        if i['id'] in g.DELROOT: continue
        if i['Category'] != 'complex' and i['Category'] != 'organism-complex':
            if i['id'] not in get_complex:
                get_complex.append(i['id'])
        else:
            if i['id'] not in get_compoment:
                get_compoment.append(i['id'])
    get_complex = check_ids(get_complex)
    c = find_complex_by_ids(get_complex)

    l = []
    for colx in c:
        if 'Complex' in colx:
            if colx['Complex'] != '':
                colx_id = modify_sparql_id(colx['Complex'])
                pid = modify_sparql_id(colx['PRO_term'])
                l.append(colx_id)
                if [colx_id, 'has_component', pid, 'OBO', ''] not in relations:
                    relations.append([colx_id, 'has_component', pid, 'OBO', ''])

    for j in l:
        if j not in complex:
            complex.append(j)
    get_pro = complex + get_compoment
    get_pro = check_ids(get_pro)
    tem_component = find_component_by_ids(get_pro)
    l2 = []
    for comp in tem_component:
        if 'Component' in comp: # 'Component' in comp
            if comp['Component'] != '':
                comp_id = modify_sparql_id(comp['Component'])
                pid = modify_sparql_id(comp['PRO_term'])
                l2.append(comp_id)
                if [pid, 'has_component', comp_id, 'OBO', ''] not in relations:
                    relations.append([pid, 'has_component', comp_id, 'OBO', ''])

    for j in l2:
        if j not in component:
            component.append(j)
        if j not in get_parent:
            get_parent.append(j)
    pp_set = []
    get_parent = check_ids(get_parent)
    if get_parent != []:
        pp_set,relations = get_ancestors_by_ids(get_parent,relations)
    addition = pp_set+complex+component
    addition = list(set(addition))
    addition = check_ids(addition)
    for i in addition:
        if i not in ids:
            ids.append(i)
    return ids,relations


def pass_node_info_by_ids_with_taxon(ids):
    query_id = pass_ids_for_query(ids)
    query = """
        PREFIX obo: <http://purl.obolibrary.org/obo/>  
        PREFIX paf: <http://pir.georgetown.edu/pro/paf#>  
        PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> 
        SELECT  *
        from <http://purl.obolibrary.org/obo/pr>
        where {
              values ?PRO_term {"""+query_id+"""} .
              ?PRO_term rdfs:subClassOf [
            a owl:Restriction ;
            owl:onProperty obo:RO_0002160 ;
            owl:someValuesFrom ?ncbi] .
            ?ncbi oboInOwl:id ?NCBITaxon_ID .
            optional {?PRO_term oboInOwl:id ?id .}
            optional {?PRO_term rdfs:label ?name .}
            optional {?PRO_term obo:IAO_0000115 ?PRO_termDef .}
            optional {?PRO_term rdfs:comment ?Category .}
        }
        """
    sparqlSearch = SparqlSearch()
    information, error = sparqlSearch.executeQuery(query)
    return information



def pass_node_info_by_ids(ids):
    query_id = pass_ids_for_query(ids)
    query = """
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX has_gene_template: <http://purl.obolibrary.org/obo/pr#has_gene_template>
    PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
    PREFIX PR: <http://purl.obolibrary.org/obo/PR_>
    Select distinct ?PRO_term ?id ?name ?PRO_termDef ?Category GROUP_CONCAT(DISTINCT ?synonym; separator='; ') as ?synonym
    where {
    values ?PRO_term {
    """ + query_id + """
    }
    optional {?PRO_term oboInOwl:id ?id .}
    optional {?PRO_term rdfs:label ?name .}
    optional {?PRO_term obo:IAO_0000115 ?PRO_termDef .}
    optional {?PRO_term rdfs:comment ?Category .}
    OPTIONAL {?PRO_term oboInOwl:hasExactSynonym ?synonym .}
    }
    """
    sparqlSearch = SparqlSearch()
    information, error = sparqlSearch.executeQuery(query)
    return information


"""Hierarchy"""


def get_children_by_query(id):
  children = []
  query_id = id.replace(':', '_')
  query_id = query_id.replace(' ','')
  childquery = """
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX obo: <http://purl.obolibrary.org/obo/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
      SELECT distinct ?children
      WHERE
      {
      values ?PRO_term {obo:""" + query_id + """} .
      ?children rdfs:subClassOf* ?PRO_term .
      }
        """
  sparqlSearch = SparqlSearch()
  childs, error = sparqlSearch.executeQuery(childquery)
  for case in childs:
    temchild = case['children']
    if temchild != '':
        child = temchild[31:].replace('_', ':')
        if child != id and child not in children:
          children.append(child)
  return children


def get_ancestors_by_ids(ids,relations):
    ancestors = []
    query_id = pass_ids_for_query(ids)
    query = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
    SELECT distinct ?ancestor as ?PRO ?PRO_name ?directParent as ?Parent ?Parent_name
    WHERE
    {
       {
           SELECT distinct ?ancestor
           WHERE
           {
               values ?PRO_term {"""+query_id+"""}
               ?PRO_term rdfs:subClassOf ?parent .
               ?parent rdfs:subClassOf* ?ancestor .
           }
            }
            UNION {
                values ?ancestor {"""+query_id+"""}
                    ?ancestor oboInOwl:id ?ancestor_id .
            }
       ?ancestor rdfs:subClassOf ?directParent .
       ?directParent oboInOwl:id ?directParent_id .
       ?ancestor oboInOwl:id ?ancestor_id .
       ?ancestor rdfs:label ?ancestor_label .
       ?directParent rdfs:label ?directParent_label .
       FILTER(STRSTARTS(?directParent_id, 'PR:')|| STRSTARTS(?directParent_id, 'GO:'))
       FILTER (!isBlank(?directParent))
       FILTER(STRSTARTS(?ancestor_id, 'PR:')|| STRSTARTS(?ancestor_id, 'GO:'))
       FILTER (!isBlank(?ancestor))
       BIND(str(?ancestor_label) as ?PRO_name) .
       BIND(str(?directParent_label) as ?Parent_name) .
    }
    """
    sparqlSearch = SparqlSearch()
    response, error = sparqlSearch.executeQuery(query)
    for case in response:
        pid = modify_sparql_id(case['Parent'])
        oid = modify_sparql_id(case['PRO'])
        if pid not in ancestors: ancestors.append(pid)
        if oid not in ancestors: ancestors.append(oid)
        if [oid,'is_a',pid,'OBO',''] not in relations:
            relations.append([oid,'is_a',pid,'OBO',''])
    return ancestors,relations

def get_siblings(id,parent_set):
    parent_set = check_ids(parent_set)
    term_cate = get_cate_by_id(id)
    siblings = []
    sibling_set = []
    for el in parent_set:
        if el in hierarchy_root:
            continue
        cl = get_children_by_query(el)
        if len(cl)>=30:
            continue
        for c in cl:
            if c not in sibling_set:
                sibling_set.append(c)
    sib_cate = get_category_by_ids(sibling_set)
    for i in sib_cate:
        if i['Category'] == term_cate and not i['id'] == id:
            siblings.append(i['id'])
    return siblings

def get_all_direct_parent(id):
    """return all direct parents"""
    query_id = id.replace(':', '_')
    direct_parent = []
    query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX obo: <http://purl.obolibrary.org/obo/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
        SELECT distinct ?Parent ?name
        WHERE
        {
            values ?PRO_term {obo:""" + query_id + """} .
            ?PRO_term rdfs:subClassOf ?_Parent .
            ?_Parent rdfs:label ?name .
            ?_Parent oboInOwl:id ?Parent .
        }"""
    sparqlSearch = SparqlSearch()
    dir_parents, error = sparqlSearch.executeQuery(query)
    for dp in dir_parents:
        pid = dp['Parent']
        pidname = dp['name']
        direct_parent.append([pid,pidname])
    return direct_parent


def get_compoment_by_obo(id):
    # find compoment from obo
    # compoment has been marked as "has_compoment" in 'relationship'
    query_id = id.replace(':', '_')
    compoment_list = []
    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    SELECT ?Component
    FROM <http://purl.obolibrary.org/obo/pr>
    WHERE
    {{
       optional {  obo:""" + query_id + """
            rdfs:subClassOf           [ a                         owl:Restriction ;
                                        owl:onClass               ?Component ;
                                        owl:onProperty            obo:RO_0002180 ;
                                        owl:qualifiedCardinality  ?cardinality
        ] .}}
        union{
      optional {  obo:""" + query_id + """
            rdfs:subClassOf           [ a                   owl:Restriction ;
                                        owl:onProperty      obo:RO_0002180 ;
                                        owl:someValuesFrom  ?Component
        ] .}}

    }
    """
    sparqlSearch = SparqlSearch()
    compoments, error = sparqlSearch.executeQuery(query)
    for compoment in compoments:
        if compoment['Component'] != '':
            target = compoment['Component']
            target = target[31:]
            target = target.replace('_', ':')
            compoment_list.append(target)
    return compoment_list

def find_complex_by_compoment(id):
    query_id = id.replace(':', '_')
    complex_list = []
    query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX obo: <http://purl.obolibrary.org/obo/>
        SELECT ?PRO_term
        FROM <http://purl.obolibrary.org/obo/pr>
        WHERE
        {{
           optional {  ?PRO_term
                rdfs:subClassOf           [ a                         owl:Restriction ;
                                            owl:onClass               obo:""" + query_id + """ ;
                                            owl:onProperty            obo:RO_0002180 ;
                                            owl:qualifiedCardinality  ?cardinality
            ] .}}
            union{
          optional {  ?PRO_term
                rdfs:subClassOf           [ a                   owl:Restriction ;
                                            owl:onProperty      obo:RO_0002180 ;
                                            owl:someValuesFrom  obo:""" + query_id + """
            ] .}
            }

        }
        """
    sparqlSearch = SparqlSearch()
    complexs, error = sparqlSearch.executeQuery(query)
    for complex in complexs:
        if complex['PRO_term'] != '':
            target = complex['PRO_term']
            target = target[31:]
            target = target.replace('_', ':')
            complex_list.append(target)
    return complex_list


def get_all_direct_parent_by_ids(ids):
    """return all direct parents"""
    id_set = seperate_ids_for_api(ids)
    dir_parents = []
    for i in id_set:
        i = i.split(' ')
        query_id = ''
        for id in i:
            if id != '':
                id = 'obo:' + id.replace(':', '_')
                query_id += id + ' '
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX obo: <http://purl.obolibrary.org/obo/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
            SELECT distinct ?PRO_term ?Parent
            WHERE
            {
                values ?PRO_term {""" + query_id + """} .
                ?PRO_term rdfs:subClassOf ?_Parent .
                ?_Parent oboInOwl:id ?Parent

            }"""
        sparqlSearch = SparqlSearch()
        dir_parents, error = sparqlSearch.executeQuery(query)

    return dir_parents


def find_component_by_ids(ids):
    # find component by a list of ids
    component = []
    id_set = seperate_ids_for_api(ids)
    for i in id_set:
        i = i.split(' ')
        query_id = ''
        for id in i:
            if id != '':
                id = 'obo:' + id.replace(':', '_')
                query_id += id + ' '
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX obo: <http://purl.obolibrary.org/obo/>
        SELECT ?PRO_term ?Component
        FROM <http://purl.obolibrary.org/obo/pr>
        WHERE
        {
        values ?PRO_term {""" + query_id + """}
        {
           optional {  ?PRO_term
                rdfs:subClassOf           [ a                         owl:Restriction ;
                                            owl:onClass               ?Component ;
                                            owl:onProperty            obo:RO_0002180 ;
                                            owl:qualifiedCardinality  ?cardinality
            ] .}}
            union{
          optional {  ?PRO_term
                rdfs:subClassOf           [ a                   owl:Restriction ;
                                            owl:onProperty      obo:RO_0002180 ;
                                            owl:someValuesFrom  ?Component
            ] .}}

        }
        """
        sparqlSearch = SparqlSearch()
        component, error = sparqlSearch.executeQuery(query)
    return component


def find_complex_by_ids(ids):
    complex = []
    id_set = seperate_ids_for_api(ids)
    for i in id_set:
        i = i.split(' ')
        query_id = ''
        for id in i:
            if id != '':
                id = 'obo:' + id.replace(':', '_')
                query_id += id + ' '
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX obo: <http://purl.obolibrary.org/obo/>
        SELECT ?PRO_term ?Complex
        FROM <http://purl.obolibrary.org/obo/pr>
        WHERE
                {
                 values ?PRO_term {""" + query_id + """}

        {
                   optional {  ?Complex
                        rdfs:subClassOf           [ a                         owl:Restriction ;
                                                    owl:onClass               ?PRO_term ;
                                                    owl:onProperty            obo:RO_0002180 ;
                                                    owl:qualifiedCardinality  ?cardinality
                    ] .}}
                    union{
                  optional {  ?Complex
                        rdfs:subClassOf           [ a                   owl:Restriction ;
                                                    owl:onProperty      obo:RO_0002180 ;
                                                    owl:someValuesFrom  ?PRO_term
                    ] .}
                    }

        }
        """
        sparqlSearch = SparqlSearch()
        complex, error = sparqlSearch.executeQuery(query)
    return complex


def get_hierarchy_by_id(id):
    # return hierarhcy for one PRO ID
    # hierarchy: 0 parents, 1 children,2 complex,3 component,4 siblings
    query_id = 'obo:' + id.replace(':', '_')
    dir_parents = []
    children = []
    complex = []
    component = []
    parents = []
    query = """
            PREFIX obo: <http://purl.obolibrary.org/obo/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#> 
            PREFIX has_gene_template: <http://purl.obolibrary.org/obo/pr#has_gene_template>
            PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
            PREFIX PR: <http://purl.obolibrary.org/obo/PR_>
            Select  
            ?PRO_term
            group_concat(distinct str(?parent_id) ; separator = ", ") AS ?_parent_id 
            group_concat(distinct str(?ancestor_id) ; separator = ", ") AS ?_ancestor_id
            group_concat(distinct str(?Child_ID) ; separator = ", ") AS ?children 
            group_concat(distinct str(?Component) ; separator = ", ") AS ?_Component
            group_concat(distinct str(?Complex) ; separator = ", ") AS ?_Complex
            FROM <http://purl.obolibrary.org/obo/pr>
            where {
            values ?PRO_term {""" + query_id + """}
            {
            ?PRO_term rdfs:subClassOf ?parent .
            ?parent rdfs:subClassOf* ?ancestor .
            ?ancestor oboInOwl:id ?ancestor_id .
            ?parent oboInOwl:id ?parent_id .
            FILTER(STRSTARTS(?ancestor_id, 'PR:')|| STRSTARTS(?ancestor_id, 'GO:')|| STRSTARTS(?ancestor_id, 'CHEBI:')) .
            FILTER (!isBlank(?ancestor)) .
            }
            union
            {
            ?child rdfs:subClassOf* ?PRO_term .
            ?child oboInOwl:id ?Child_ID .
            }
            union
            {
                       optional {  ?PRO_term
                            rdfs:subClassOf           [ a                         owl:Restriction ;
                                                        owl:onClass               ?Component ;
                                                        owl:onProperty            obo:RO_0002180 ;
                                                        owl:qualifiedCardinality  ?cardinality
                        ] .}}
                        union{
                      optional {  ?PRO_term
                            rdfs:subClassOf           [ a                   owl:Restriction ;
                                                        owl:onProperty      obo:RO_0002180 ;
                                                        owl:someValuesFrom  ?Component
                        ] .}
            }
            union
            {
                               optional {  ?Complex
                                    rdfs:subClassOf           [ a                         owl:Restriction ;
                                                                owl:onClass               ?PRO_term ;
                                                                owl:onProperty            obo:RO_0002180 ;
                                                                owl:qualifiedCardinality  ?cardinality
                                ] .}}
                                union{
                              optional {  ?Complex
                                    rdfs:subClassOf           [ a                   owl:Restriction ;
                                                                owl:onProperty      obo:RO_0002180 ;
                                                                owl:someValuesFrom  ?PRO_term
                                ] .}
            }
            }

            """
    information = []
    # url = 'https://sparql.proconsortium.org/virtuoso/sparql?default-graph-uri='
    # params = {'query': query, "format": "text/tab-separated-values", "timeout": 0}
    # response = requests.get(url, params=params)

    sparqlSearch = SparqlSearch()
    information, error = sparqlSearch.executeQuery(query)
    # reader = csv.DictReader(response.text.split('\n'), delimiter='\t')
    # for line in reader:
    #     information.append(line)
    # sparqlSearch = SparqlSearch()
    # information, error = sparqlSearch.executeQuery(query)
    for case in information:
        if '_parent_id' in case:
            dir_parents = case['_parent_id'].split(',')
        if '_ancestor_id' in case:
            parents = case['_ancestor_id'].split(',')
        if 'children' in case:
            children = case['children'].split(',')
        if '_Complex' in case:
            if case['_Complex'] != '':
                complexx = case['_Complex'].split(',')
                for i in complexx:
                    if i != '':
                        i = modify_sparql_id(i)
                        complex.append(i)
            else:
                complex = []
        if '_Component' in case:
            if case['_Component'] != '':
                componentt = case['_Component'].split(',')
                for i in componentt:
                    if i != '':
                        i = modify_sparql_id(i)
                        component.append(i)
            else:
                component = []
    dir_parents = check_ids(dir_parents)
    siblings = get_siblings(id, dir_parents)
    siblings = check_ids(siblings)
    hierarchy = [parents, children, complex, component, siblings]
    return hierarchy


def get_tree_pair(id):
    proId = id.replace(':', '_')
    newquery = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX obo: <http://purl.obolibrary.org/obo/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>

        SELECT distinct ?PRO ?PRO_name ?Parent ?Parent_name
        WHERE 
        {
    	    {
    		SELECT distinct ?ancestor as ?PRO ?PRO_name ?directParent as ?Parent ?Parent_name
    		WHERE
    		{
      			{
                  SELECT distinct ?ancestor
                  WHERE
                  {
                      values ?PRO_term {obo:"""
    newquerymiddle = """}
                      ?PRO_term rdfs:subClassOf ?parent .
                      ?parent rdfs:subClassOf* ?ancestor .
                  }
       			}
             UNION {
                  values ?ancestor {obo:"""
    newquerymiddle2 = """}
              ?ancestor oboInOwl:id ?ancestor_id .
            }
            ?ancestor rdfs:subClassOf ?directParent .
            ?directParent oboInOwl:id ?directParent_id .
            ?ancestor oboInOwl:id ?ancestor_id .
            ?ancestor rdfs:label ?ancestor_label .
            ?directParent rdfs:label ?directParent_label .
            FILTER(STRSTARTS(?directParent_id, 'PR:')|| STRSTARTS(?directParent_id, 'GO:'))
            FILTER (!isBlank(?directParent))
            FILTER(STRSTARTS(?ancestor_id, 'PR:')|| STRSTARTS(?ancestor_id, 'GO:'))
            FILTER (!isBlank(?ancestor))
            BIND(str(?ancestor_label) as ?PRO_name) .
            BIND(str(?directParent_label) as ?Parent_name) .
          }
    	    }
    	    UNION 
    	    {
          SELECT distinct ?children as ?PRO ?PRO_name ?directParent as ?Parent ?Parent_name
          WHERE
          {
             {
                SELECT distinct ?children
                WHERE
                {
                    values ?PRO_term {obo:"""
    newquerymiddle3 = """}
                    ?children rdfs:subClassOf* ?PRO_term .
                }
             }
             UNION {
                  values ?children {obo:"""
    newquerymiddle4 = """}
                  ?children oboInOwl:id ?children_id .
            }
            ?children rdfs:subClassOf ?directParent .
            ?directParent rdfs:subClassOf* obo:"""
    newquerytail = """ .
            ?directParent oboInOwl:id ?directParent_id .
            ?children oboInOwl:id ?children_id .
            ?children rdfs:label ?children_label .
            ?directParent rdfs:label ?directParent_label .
            FILTER(STRSTARTS(?directParent_id, 'PR:')|| STRSTARTS(?directParent_id, 'GO:'))
            FILTER (!isBlank(?directParent))
            FILTER(STRSTARTS(?children_id, 'PR:')|| STRSTARTS(?children_id, 'GO:'))
            FILTER (!isBlank(?children))
            BIND(str(?children_label) as ?PRO_name) .
            BIND(str(?directParent_label) as ?Parent_name) .
          }
            }
            }"""
    fnewquery = newquery + proId + newquerymiddle + proId + newquerymiddle2 + proId + newquerymiddle3 + proId + newquerymiddle4 + proId + newquerytail
    sparqlSearch = SparqlSearch()
    proIDs, error = sparqlSearch.executeQuery(fnewquery)
    rel_pair = []
    # child is_a parent
    # example: [u'PR:P97471', 'is_a', 'PR:000029032', 'OBO', '']
    for pair in proIDs:
        cid = modify_sparql_id(pair['PRO'])
        pid = modify_sparql_id(pair['Parent'])
        rel_pair.append([cid, 'is_a', pid, 'OBO', ''])
    return rel_pair

def get_hierarchy_by_ids(ids,relations):
    hierarchy_dic = {}
    # return hierarhcy for one PRO ID
    # hierarchy: 0 parents, 1 children,2 complex,3 component,4 siblings
    query_id_set = ''
    root_id = []
    for id in ids:
        newid = id.replace(' ','')
        if newid in hierarchy_root:
            root_id.append(newid)
            continue
        if newid == 'PR:000029032':
            root_id.append(newid)
            continue
        newid = newid.replace(':','_')
        if newid == '':continue
        query_id_set += 'obo:' + newid + ' '
    # query_id = 'obo:' + id.replace(':', '_')
    dir_parents = []
    children = []
    complex = []
    component = []
    parents = []
    query = """
                PREFIX obo: <http://purl.obolibrary.org/obo/>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX owl: <http://www.w3.org/2002/07/owl#> 
                PREFIX has_gene_template: <http://purl.obolibrary.org/obo/pr#has_gene_template>
                PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
                PREFIX PR: <http://purl.obolibrary.org/obo/PR_>
                Select  
                ?PRO_term
                group_concat(distinct str(?parent_id) ; separator = ", ") AS ?_parent_id 
                group_concat(distinct str(?ancestor_id) ; separator = ", ") AS ?_ancestor_id
                group_concat(distinct str(?Child_ID) ; separator = ", ") AS ?children 
                group_concat(distinct str(?Component) ; separator = ", ") AS ?_Component
                group_concat(distinct str(?Complex) ; separator = ", ") AS ?_Complex
                FROM <http://purl.obolibrary.org/obo/pr>
                where {
                values ?PRO_term {""" + query_id_set + """}
                {
                ?PRO_term rdfs:subClassOf ?parent .
                ?parent rdfs:subClassOf* ?ancestor .
                ?ancestor oboInOwl:id ?ancestor_id .
                ?parent oboInOwl:id ?parent_id .
                FILTER(STRSTARTS(?ancestor_id, 'PR:')|| STRSTARTS(?ancestor_id, 'GO:')|| STRSTARTS(?ancestor_id, 'CHEBI:')) .
                FILTER (!isBlank(?ancestor)) .
                }
                union
                {
                ?child rdfs:subClassOf ?PRO_term .
                ?child oboInOwl:id ?Child_ID .
                }
                union
                {
                           optional {  ?PRO_term
                                rdfs:subClassOf           [ a                         owl:Restriction ;
                                                            owl:onClass               ?Component ;
                                                            owl:onProperty            obo:RO_0002180 ;
                                                            owl:qualifiedCardinality  ?cardinality
                            ] .}}
                            union{
                          optional {  ?PRO_term
                                rdfs:subClassOf           [ a                   owl:Restriction ;
                                                            owl:onProperty      obo:RO_0002180 ;
                                                            owl:someValuesFrom  ?Component
                            ] .}
                }
                union
                {
                                   optional {  ?Complex
                                        rdfs:subClassOf           [ a                         owl:Restriction ;
                                                                    owl:onClass               ?PRO_term ;
                                                                    owl:onProperty            obo:RO_0002180 ;
                                                                    owl:qualifiedCardinality  ?cardinality
                                    ] .}}
                                    union{
                                  optional {  ?Complex
                                        rdfs:subClassOf           [ a                   owl:Restriction ;
                                                                    owl:onProperty      obo:RO_0002180 ;
                                                                    owl:someValuesFrom  ?PRO_term
                                    ] .}
                }
                }

                """
    information = []
    url = 'https://sparql.proconsortium.org/virtuoso/sparql?default-graph-uri='
    params = {'query': query, "format": "text/tab-separated-values", "timeout": 0}
    response = requests.get(url, params=params)
    reader = csv.DictReader(response.text.split('\n'), delimiter='\t')
    for line in reader:
        information.append(line)

    for case in information:
        siblings = []
        id = modify_sparql_id(case['PRO_term'])
        id = id.replace(' ','')
        if '_parent_id' in case:
            dir_parents = case['_parent_id'].split(',')
            for p in dir_parents:
                if p != '':
                    mp = p.replace(' ','')
                    if mp not in ids:
                        ids.append(p)
                    else:
                        if [id,'is_a',mp,'OBO',''] not in relations:
                            relations.append([id,'is_a',mp,'OBO',''])
        if '_ancestor_id' in case:
            parents = case['_ancestor_id'].split(',')
        if 'children' in case:
            children = case['children'].split(',')
            for c in children:
                if c != '':
                    mc = c.replace(' ','')
                    if mc not in ids:
                        continue
                    else:
                        if [mc,'is_a',id,'OBO',''] not in relations:
                            relations.append([mc,'is_a',id,'OBO',''])
        if '_Complex' in case:
            complex = case['_Complex'].split(',')
            for cpx in complex:
                if cpx != '':
                    cpx = modify_sparql_id(cpx)
                    mcpx = cpx.replace(' ','')
                    if mcpx not in ids:
                        ids.append(mcpx)
                    relations.append([mcpx,'has_component',id,'OBO',''])
        if '_Component' in case:
            component = case['_Component'].split(',')
            for comp in component:
                if comp != '':
                    comp = modify_sparql_id(comp)
                    mcomp = comp.replace(' ','')
                    if mcomp not in ids:
                        ids.append(mcomp)
                    relations.append([id,'has_component',mcomp,'OBO',''])
        # if id != '':
        #     siblings = get_siblings(id, dir_parents)
        hierarchy = [parents, children, complex, component, siblings]
        hierarchy_dic[id] = hierarchy
    for i in root_id:
        hierarchy_dic[i] = [[],[],[],[],[]]

    return hierarchy_dic,ids,relations

def fetch_uninodes(ids):
    # unsure
    # find children for uni nodes
    # input must be list
    children_set = []
    query_id = change_idlist_into_queryid(ids)

    query = """
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX has_gene_template: <http://purl.obolibrary.org/obo/pr#has_gene_template>
    PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
    PREFIX PR: <http://purl.obolibrary.org/obo/PR_>
    SELECT distinct ?id ?children_id
    WHERE
    {
    values ?PRO_term {""" + query_id + """}
    ?children rdfs:subClassOf* ?PRO_term .
    ?children oboInOwl:id ?children_id .
    ?PRO_term oboInOwl:id ?id .
    }
    """
    sparqlSearch = SparqlSearch()
    allchildren, error = sparqlSearch.executeQuery(query)

    for children_pair in allchildren:
        if children_pair['id'] in ids and children_pair['children_id'] != '':
            children_set.append(children_pair['children_id'])

    children_set = check_ids(children_set)

    return children_set

def fetct_childandtaxon_by_ids(ids):
    result =[]
    query_id = change_idlist_into_queryid(ids)
    query = """
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX has_gene_template: <http://purl.obolibrary.org/obo/pr#has_gene_template>
    PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
    PREFIX PR: <http://purl.obolibrary.org/obo/PR_>
    select DISTINCT* 
    where{
    values ?PRO_term{"""+query_id+"""} .
                   ?PRO_term rdfs:subClassOf [
                        a owl:Restriction ;
                        owl:onProperty obo:RO_0002160 ;
                        owl:someValuesFrom ?ncbi ] .
                ?ncbi
                    oboInOwl:hasOBONamespace 'ncbi_taxonomy'^^xsd:string ;
                    oboInOwl:id ?NCBITaxon_ID .
    }
    """
    sparqlSearch = SparqlSearch()
    allchildren, error = sparqlSearch.executeQuery(query)
    return result

# def get_sites(ids):
#     results = []
#     robj = ma.MvOboModResidueCompress()
#     for id in ids:
#         urlpatterns = "https://research.bioinformatics.udel.edu/PRO_API/V1/pros/" + id + "?showPROName=false&showPROTermDefinition=true&showCategory=false&showParent=false&showAnnotation=false&showAnyRelationship=false&showChild=false&showComment=false&showEcoCycID=false&showGeneName=false&showHGNCID=false&showMGIID=false&showOrthoIsoform=false&showOrthoModifiedForm=false&showPANTHERID=false&showPIRSFID=false&showPMID=false&showReactomeID=false&showSynonym=true&showUniProtKBID=true"
#         infoset = requests.get(urlpatterns)
#         jinfoset = infoset.json()
#         info = jinfoset[0]
#         tar = info['termDef']
#         x = tar.find('Uni')
#         tar = tar[x:]
#         uni = tar.find(',')
#         tar = tar[uni + 1:]
#         p = tar.find('.')
#         tar = tar[:p]
#         robj.subject = id
#         robj.residue = tar
#         results.append(robj)
#     return results

def get_xref_by_ids(ids):
    query_id = pass_ids_for_query(ids)
    query = """
    PREFIX obo: <http://purl.obolibrary.org/obo/> 
    PREFIX paf: <http://pir.georgetown.edu/pro/paf#> 
    PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
    SELECT * 
    where
    {
    values ?PRO_term{"""+query_id+"""}
    ?PRO_term oboInOwl:id ?id .
    ?PRO_term  oboInOwl:hasDbXref ?DbRef .
    }
    """

    sparqlSearch = SparqlSearch()
    xrefs, error = sparqlSearch.executeQuery(query)
    return xrefs


def get_enzyme(definition):
    # subject = models.CharField(primary_key=True, max_length=604)
    # type = models.CharField(max_length=400)
    # obo_dbxref_description = models.CharField(max_length=4000, blank=True)
    # aggkey = models.CharField(max_length=604, blank=True)
    # abbrev3 = models.CharField(max_length=12, blank=True)
    # position = models.IntegerField(blank=True, null=True)



    return ''

def get_residues(id):
    # subject = models.CharField(primary_key=True, max_length=604)
    # abbrev3 = models.CharField(max_length=12, blank=True)
    # position = models.IntegerField(blank=True, null=True)
    # mod_id = models.CharField(max_length=604, blank=True)

    return ''

def get_only_syn(ids):
    query_id = pass_ids_for_query(ids)
    query = """
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX has_gene_template: <http://purl.obolibrary.org/obo/pr#has_gene_template>
    PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
    PREFIX PR: <http://purl.obolibrary.org/obo/PR_>
    Select distinct ?PRO_term GROUP_CONCAT(DISTINCT ?synonym; separator='; ') as ?synonym
    where {
    values ?PRO_term {
    """ + query_id + """
    }
    OPTIONAL {?PRO_term oboInOwl:hasExactSynonym ?synonym .}
    }
    """
    sparqlSearch = SparqlSearch()
    SynAndProteo, error = sparqlSearch.executeQuery(query)

    return SynAndProteo