from database.fetch import *
from database.sparql import SparqlSearch
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, JsonResponse
from .hierarchy import *
from msa.views import loadingMSA
import re
import string
import requests
import request
import database.root_setting as g

hroot = g.ROOT+g.DELROOT

def content_test(request):
    content = {}
    return render(request,'entry_page_test.html',content)

def add_url(id):
    url = '/pro2/entry/'+id
    return url

def load_entry(id):
    content = {}
    content['checkroot'] = True
    content['id'] = id
    content['url'] = add_url(id)
    content['jstreeurl'] = '/pro2/idtree/'+id
    content['jstreenameurl'] = '/pro2/nametree/'+id
    content['msatreeurl'] = '/pro2/msa/tree/'+id
    content['msaparenturl'] = '/pro2/msa/tree/'+id
    # content['obo_url'] = 'https://proconsortium.org/app/export/obo/' + id
    content['obo_url'] = '/pro2/obo/' + id
    category = ''
    content['copx_and_conp'] = []
    content['formTableName'] = 'Protein'
    copx_and_conp = []
    terminfo = pass_node_info_by_ids([id])
    Name = ''
    Label = ''
    definition = ''
    category = ''
    go_frontend = {}
    category_types = []
    content['gocellular'] = []
    content['gomolecular'] = []
    content['gobiological'] = []
    content['checkgocellular'] = False
    content['checkgobiological'] = False
    content['checkgomolecular'] = False
    content['checkrcr'] = True
    content['checkanno'] = True
    content['termscategory'] = False
    content['msaEntryUrl'] = '/pro2/msa/view/entry/'+id
    content['hasmsa'] = True
    content['hashierarchy'] = True
    content['hashierarchytext'] = 'True'
    content['checkpaf'] = False
    finalparentlist = []
    # content['msaview'] = loadingMSA(request,'entry',id)
    xref_set = get_xref(id)
    for i in range(len(xref_set)):
        xref_set[i] = modify_info_url(xref_set[i])
    content['xref'] = xref_set
    for info in terminfo:
        if 'name' in info:
            Name = info['name']
            content['name'] = Name
        else: content['name'] = ''
        if 'Category' in info:
            content['comment'] = modify_info_url(info['Category'])
            CategoryAndComment = info['Category'].split('.')
            for i in CategoryAndComment:
                if i.find('Category=')!= -1:
                    content['category'] = i.replace('Category=','')
                    category = content['category']
                    break
                else:
                    if i != '':
                        category = i
        if 'synonym' in info:
            if Name.find('complex') > -1 or category.find('complex') > -1 or id.find('CHEBI') > -1:
                Label = Name
            else:
                synonym = info['synonym'].split(';')
                for syns in synonym:
                    if syns.find('EXACT PRO-short-label') != -1:
                        j = syns.split(' ')
                        Label = j[1].replace('"', '')
                    elif syns.find('UniProtKB') == -1 and syns.find('(') == -1:
                        Label = syns
            content['synonyms'] = Label
        if 'PRO_termDef' in info:
            definition = info['PRO_termDef']
            content['definition'] = modify_info_url(definition)
            # print(content['definition'])
        else: content['definition'] = ''
    if id in hroot:
        content['has_parent'] = False
        content['checkforms'] = False
        content['terms_cat'] = False
        content['hasmsa'] = False
        content['hashierarchy'] = False
        content['hashierarchytext'] = 'false'
        return content
    else:
        paf_frontend = {id: {'name': Name, 'set': []}}
        dir_parent = get_all_direct_parent(id)
        if dir_parent != []:
            content['has_parent'] = True
            content['dir_parents'] = dir_parent
            for i in dir_parent:
                pid = i[0]
                i.append(add_url(pid))
                # parentcatelist = get_category_by_ids([pid])

        content['checkforms'] = False
        forms = [[id,Name,modify_info_url(definition),category,Label,'','','','']]
        # content['forms'] = [[id,Name,modify_info_url(definition),category,Label,[],[],[],[]]]
        content['terms_cat'] = ''
        children = get_children_by_query(id)
        children.append(id)
        checkcate = ['gene','organism-gene']
        if content['category'] in checkcate:
            content['termscategory'] = True
             # 0 organism-gene, 1 organism-sequence, 2 organism-modification
            formschild = True
            content['terms_cat'] = True
            has_component,copx_and_conp = pass_complex(id)
            content['has_component'] = has_component
            content['copx_and_conp'] = copx_and_conp

            conp = []
            for cc in copx_and_conp:
                if cc[3] not in conp:
                    conp.append(cc[3])
            if category == 'organism-gene':
                for i in dir_parent:
                    finalparentlist.append(i[0])
                parentidandcate = get_category_by_ids(finalparentlist)
                for i in parentidandcate:
                    if 'Category' in i and i['Category'] == 'gene':
                        trueparentforog = i['id']
                        print(trueparentforog)
                        content['msaparenturl'] = '/pro2/msa/tree/' + trueparentforog
                ogcount = [0, 0, 0]
                nodeinfo,formschild = view_organismgene(children)
                content['checkforms'] = formschild
                for i in nodeinfo:
                    i[2] = modify_info_url(i[2])
                    if i not in forms:
                        forms.append(i)
                for i in forms:
                    if i[3] == 'organism-gene':
                        ogcount[0] += 1
                    if i[3] == 'organism-sequence':
                        ogcount[1] += 1
                    if i[3] == 'organism-modification':
                        ogcount[2] += 1
                content['term_pro_cat'] = ogcount
            if category == 'gene':
                content['terms_cat'] = False
                ogcount = [0,0,0,0,0,0,0]
                nodeinfo, formschild = view_organismgene(children)
                content['checkforms'] = formschild
                for i in nodeinfo:
                    if i not in forms:
                        forms.append(i)
                for i in forms:
                    if i[3] == 'gene':
                        ogcount[0] += 1
                    if i[3] == 'organism-gene':
                        ogcount[1] += 1
                    if i[3] == 'sequence':
                        ogcount[2] += 1
                    if i[3] == 'organism-sequence':
                        ogcount[3] += 1
                    if i[3] == 'modification':
                        ogcount[4] += 1
                    if i[3] == 'organism-modification':
                        ogcount[5] += 1
                    if i[3] == 'union':
                        ogcount[6] += 1
                content['term_pro_cat'] = ogcount
            children.extend(conp)

        for i in forms:
            if i[3] != '' and i[3] not in category_types:
                category_types.append(i[3])

        content['forms'] = forms
        # print(forms)
        content['category_types'] = category_types
        # print(category_types)
        for i in children:
            paf_frontend[i] = {'name':'','set':[]}

        paf_result,go_result = get_pafs(children)
        for paf in paf_result:
            if paf[0] in paf_frontend:
                paf_frontend[paf[0]]['name'] = paf[1]
                if paf[2] not in paf_frontend[paf[0]]['set']:
                    paf_frontend[paf[0]]['set'].append(paf[2])

        for go in go_result:
            if go[0] not in go_frontend:
                go_frontend[go[0]] = {'name':go[1],'set':go[2]}
            else:
                go_frontend[go[0]]['set'].append(go[2][0])

        paf_frontend_after = []
        go_frontend_biological = []
        go_frontend_cellular = []
        go_frontend_molecular = []
        for i in paf_frontend:
            if paf_frontend[i]['set'] != []:
                resources = paf_frontend[i]['set']
                for j in resources:
                    j[2] = modify_space_url(j[2])
                    evi = j[4].split(',')
                    evi_after = []
                    for k in evi:
                        k = k.replace(' ','')
                        if k.find('PMID')!=-1:
                            k = "<a target=\"_blank\" href=\"http://www.ncbi.nlm.nih.gov/pubmed/"+k.replace('PMID:','')+"\" title=\"\">"+k+"</a>"
                        if k.find('Reactome:')!=-1:
                            k="<a target=\"_blank\" href=\"http://www.ncbi.nlm.nih.gov/pubmed/"+k.replace('Reactome:','')+"\" title=\"\">"+k+"</a>"
                        if k.find('PIRSF:')!=-1:
                            k="<a target=\"_blank\" href=\"http://proteininformationresource.org/cgi-bin/ipcSF?id="+k.replace('PIRSF:','')+"\" title=\"\">"+k+"</a>"
                        if k.find('DOID:') != -1:
                            k = '<a href=\"http://disease-ontology.org/term/' + k + '\" target=\"_blank\" title=\"\">' + k + '</a>'
                        if k.find('GO:') != -1:
                            k = '<a href=\"http://amigo.geneontology.org/amigo/term/' + k + '\" target=\"_blank\" title=\"\">' + k + '</a>'
                        evi_after.append(k)
                    j[4] = evi_after
                # <a target="_blank" href="http://www.ncbi.nlm.nih.gov/pubmed/12732634" title="">PMID:12732634</a>
                # <a target="_blank" href="http://www.reactome.org/content/detail/REACT_7382" title="">Reactome:REACT_7382</a>
                paf_frontend_after.append([i,paf_frontend[i]['name'],resources,len(paf_frontend[i]['set'])+1])
        content['paf'] = paf_frontend_after
        # print(content['paf'])
        for i in go_frontend:
            for j in go_frontend[i]['set']:
                evis = j[2].split(',')
                evis_after = []
                for k in evis:
                    if k.find('PMID') != -1:
                        k = "<a target=\"_blank\" href=\"http://www.ncbi.nlm.nih.gov/pubmed/" + k.replace('PMID:','') + "\" title=\"\">" + k + "</a>"
                    if k.find('Reactome:') != -1:
                        k = "<a target=\"_blank\" href=\"http://www.ncbi.nlm.nih.gov/pubmed/" + k.replace('Reactome:', '') + "\" title=\"\">" + k + "</a>"
                    if k.find('PIRSF:') != -1:
                        k = "<a target=\"_blank\" href=\"http://proteininformationresource.org/cgi-bin/ipcSF?id=" + k.replace('PIRSF:', '') + "\" title=\"\">" + k + "</a>"
                    evis_after.append(k)
                j[2] = evis_after

                if j[3] == 'located_in' and [i,go_frontend[i]['name'],go_frontend[i]['set'],len(go_frontend[i]['set'])+1] not in go_frontend_cellular:
                    go_frontend_cellular.append([i,go_frontend[i]['name'],go_frontend[i]['set'],len(go_frontend[i]['set'])+1])
                elif j[3] == 'has_function' and [i,go_frontend[i]['name'],go_frontend[i]['set'],len(go_frontend[i]['set'])+1] not in go_frontend_molecular:
                    go_frontend_molecular.append([i,go_frontend[i]['name'],go_frontend[i]['set'],len(go_frontend[i]['set'])+1])
                elif [i,go_frontend[i]['name'],go_frontend[i]['set'],len(go_frontend[i]['set'])+1] not in go_frontend_biological:
                    if j[3] == 'located_in':continue
                    go_frontend_biological.append([i,go_frontend[i]['name'],go_frontend[i]['set'],len(go_frontend[i]['set'])+1])

        content['gocellular'] = go_frontend_cellular
        content['gomolecular'] = go_frontend_molecular
        content['gobiological'] = go_frontend_biological

        if len(go_frontend_cellular) > 0:
            content['checkgocellular'] = True
        if len(go_frontend_biological) >0:
            content['checkgobiological'] = True
        if len(go_frontend_molecular) > 0:
            content['checkgomolecular'] = True

        if content['xref'] == []:
            content['checkrcr']=False

        if content['forms'] != []:
            content['checkforms']=True
        if content['paf'] != []:
            content['checkpaf'] = True
        # print(content['copx_and_conp'])
        return content


def view_hierarchy(request,proId):
    proId = proId.replace(':', '_')
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
    if error == None:
        allnodes = []
        children = {}
        parents = {}
        linkset = {}
        IdAndName = {'PR_000018263':'amino acid chain'}
        default_color = "color:black"
        redcolor = "color:red;"
        searchNode = ''

        for x in proIDs:
            # cn = '[' + x['PRO_name'] + ']'
            cu = x['PRO']
            cid = cu[31:]
            # cpair = {'ID' : cu[31:], 'name': x['PRO_name']}

            if cid not in IdAndName:
                IdAndName[cid] = x['PRO_name']
            x['PRO_name'] = cid
            # find the search node
            if cid == proId:
                searchNode = x['PRO_name']

            pu = x['Parent']
            pn = pu[31:]
            pname = x['Parent_name']
            if pn not in IdAndName:
                IdAndName[pn] = pname
            x['Parent_name'] = pn

            # idset.append({'PRO':cu, 'PRO_name':cid, 'Parent':pu, 'Parent_name':pu[31:]})


        for keyname in proIDs:
            proname = keyname['PRO_name']
            child_url = keyname['PRO']
            proparentname = keyname['Parent_name']
            parent_url = keyname['Parent']
            if proname not in linkset:
                linkset[proname] = '/pro2/entry/' + child_url[31:].replace('_', ':')
            if proparentname not in linkset:
                linkset[proparentname] = '/pro2/entry/' + parent_url[31:].replace('_', ':')



        for x in proIDs:
            pro = x['PRO_name']
            pro_parent = x['Parent_name']
            if pro not in allnodes:
                allnodes.append(pro)
            if pro_parent not in allnodes:
                allnodes.append(pro_parent)
            if pro_parent in children:
                children[pro_parent].append(pro)
            else:
                child = []
                child.append(pro)
                children[pro_parent] = child
            if pro in parents:
                parents[pro].append(pro_parent)
            else:
                p = []
                p.append(pro_parent)
                parents[pro] = p
    # print(IdAndName)
    # request.session['IdAndName'] = IdAndName
    # \"title\":\"testtittle\",
    def getChildren(node):
        child_node = ''
        for child in children[node]:
            link = linkset[child]
            if child == searchNode:
                links = "{\"href\":\"" + link + "\", \"style\": \"" + redcolor + "\", \"title\": \""+IdAndName[child]+"\"}"
            else:
                links = "{\"href\":\"" + link + "\", \"style\": \"" + default_color + "\", \"title\": \""+IdAndName[child]+"\"}"
            if (child in children) and (len(children[child]) > 0):
                # child_node += "{\"text\" : \"" + child + "\", \"children\" :[" + getChildren(child) + "]},"
                child_node += "{\"text\" : \"" + child + "\", \"a_attr\" : " + links + ", \"children\" :[" + getChildren(
                    child) + "]},"
            else:
                # links = "{\"href\":\"" + link + "\", \"style\": \"" + redcolor + "\"}"
                child_node += "{\"text\" : \"" + child + "\",\"a_attr\" : " + links + ", \"children\" :[ ]},"
        return child_node

    json = ''
    for node in allnodes:
        if node not in parents:
            link = linkset[node]
            links = "{\"href\":\"" + link + "\", \"style\": \"" + default_color + "\", \"title\": \""+IdAndName[node]+"\"}"
            if node in children and len(children[node]) > 0:
                # json += "{\"text\" : \"" + node + "\", \"children\" :[" + getChildren(node) + "]},"
                json += "{\"text\" : \"" + node + "\",\"a_attr\" : " + links + ", \"children\" :[" + getChildren(
                    node) + "]},"
            else:
                json += "{\"text\" : \"" + node + "\",\"a_attr\" : " + links + ", \"children\" :[]},"

    json = re.sub(r',]}', ']}', json)
    json = re.sub(r',$', '', json)
    json = "[" + json.replace(",]}", "]}") + "]"

    return HttpResponse(json)

def view_family():
    # if category == family
    return ''


def view_gene(id,content, organism=False):
    # if category == gene
    catList = []


    return ''

def view_organismgene(children,formschild = True):
    # if category == organism-gene
    # find its parents
    # find its taxon
    # then execute view_gene()

    # change by zida
    # find direct children
    # show id, name, category, definition

    nodeinfo = []
    if len(children) != 0:
        nodeinfo = get_node_info_by_ids(children)
    else:
        formschild = False
    return nodeinfo,formschild

def pass_complex(id):
    # 0 component id, 1 component name, 2 component url
    # 3 complex id, 4 complex name, 5 complex url
    find_names = []
    copx_and_conp = []
    result_list = []
    result = get_children_by_query(id)
    children = check_ids(result)
    hierarchy, ids, relations = get_hierarchy_by_ids(children, [])
    for rela in relations:
        if rela[1] == 'has_component':
            copx_and_conp.append(rela)
    if len(copx_and_conp) >0:
        has_component = True
    else:
        has_component = False

    if has_component:

        for case in copx_and_conp:
            find_names.append(case[0])
            find_names.append(case[2])
        namedict = get_name_by_ids(find_names)

        for cp in copx_and_conp:
            result_list.append([cp[2],namedict[cp[2]],add_url(cp[2]),cp[0],namedict[cp[0]],add_url(cp[0])])

    return has_component,result_list



def get_pafs(children):

    annotation_results = []
    go_results = []
    query_id = change_idlist_into_queryid(children)

    query = """
    PREFIX obo: <http://purl.obolibrary.org/obo/> 
    PREFIX paf: <http://pir.georgetown.edu/pro/paf#> 
    PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
    
    SELECT 
      ?PRO_term   
      str(?_Object_term) as ?Object_term 
      str(?_Modifier) as ?Modifier 
      str(?_Relation) as ?Relation 
      str(?_Ontology_ID) as ?Ontology_ID 
      str(?_Ontology_term) as ?Ontology_term 
      group_concat(distinct str(?_Evidence_source) ; separator = ", ") AS ?Evidence_source   
    WHERE 
    { 
     GRAPH <http://pir.georgetown.edu/pro/paf> 
     {
        values ?PRO_term {"""+query_id+"""}
        ?PRO_term paf:objectTerm ?_Object_term . 
        ?x a rdf:Statement . 
        ?x rdf:subject ?PRO_term . 
        ?x rdf:predicate ?xp . 
        ?xp paf:relation ?_Relation . 
        ?x rdf:object ?xo . 
       ?xo paf:ontologyID ?_Ontology_ID . 
       ?xo paf:ontologyTerm ?_Ontology_term . 
        ?x paf:evidenceSource ?_Evidence_source . 
        OPTIONAL { ?x paf:modifier ?_Modifier .} 
        OPTIONAL { ?x paf:relativeTo ?_Relative_to .}  
      }
    }
    """
    sparqlSearch = SparqlSearch()
    pafs, error = sparqlSearch.executeQuery(query)
    # 0 proid, 1 name, 2 not/yes(modifier), 3 relaotionships, 4 goid, 5 goname, 6 evidence
    for i in pafs:
        pro_term = modify_sparql_id(i['PRO_term'])
        pro_term = pro_term.replace(' ','')
        annotation_results.append([pro_term,i['Object_term'],[i['Modifier'],i['Relation'],i['Ontology_ID'],i['Ontology_term'],i['Evidence_source']]])
        go_results.append([i['Ontology_ID'],i['Ontology_term'],[[pro_term,i['Object_term'],i['Evidence_source'],i['Relation']]]])
    return annotation_results,go_results




def modify_info_url(string):
    string=string.replace('Example:','Example,')
    list = re.split(r'([,;.|])',string)
    for i in range(len(list)):
        if list[i].find('UniProtKB:')!=-1 and len(list[i].split(' '))<=2:
            list[i] = list[i].replace(' ', '')
            list[i] = ' <a href=\"http://www.uniprot.org/uniprot/' + list[i].replace('UniProtKB:','') + '\" target=\"_blank\" title=\"\">'+list[i]+'</a>'
        elif list[i].find('MOD:')!=-1 and len(list[i].split(' '))<=2:
            list[i] = list[i].replace(' ', '')
            list[i] = ' <a href=\"http://purl.obolibrary.org/obo/' + list[i].replace(':','_') + '\" target=\"_blank\" title=\"\">'+list[i]+'</a>'
        elif list[i].find('CHEBI:')!=-1 and len(list[i].split(' '))<=2:
            list[i] = list[i].replace(' ', '')
            list[i] = ' <a href=\"http://purl.obolibrary.org/obo/' + list[i].replace(':','_') + '\" target=\"_blank\" title=\"\">'+list[i]+'</a>'
        elif list[i].find('PR:')!=-1 and len(list[i].split(' '))<=2:
            list[i] = list[i].replace(' ', '')
            list[i] = ' <a href=\"/pro2/entry/' + list[i] + '\" target=\"_blank\" title=\"\">'+list[i]+'</a>'
        # <a target="_blank" href="http://www.reactome.org/content/detail/R-HSA-177099" title="">Reactome:R-HSA-177099</a>
        elif list[i].find('Reactome:')!=-1 and len(list[i].split(' '))<=2:
            list[i] = list[i].replace(' ', '')
            list[i] = ' <a href=\"http://www.reactome.org/content/detail/' + list[i].replace('Reactome:','') + '\" target=\"_blank\" title=\"\">' + list[i] + '</a>'
    afterstring = ''.join(list)
    afterstring = afterstring.replace('Example,', 'Example:')
    return afterstring

def modify_space_url(string):
    list = re.split(r' ', string)
    for i in range(len(list)):
        if list[i].find('DOID:') != -1:
            list[i] = '<a href=\"http://disease-ontology.org/term/' + list[i] + '\" target=\"_blank\" title=\"\">' + list[i] + '</a>'
        elif list[i].find('GO:') != -1:
            list[i] = '<a href=\"http://amigo.geneontology.org/amigo/term/' + list[i] + '\" target=\"_blank\" title=\"\">' + list[i] + '</a>'
    afterstring = ' '.join(list)
    return afterstring


def get_xref(id):
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



def view_hierarchy_name(request, proId):
    proId = proId.replace(':','_')
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

    newquerymiddle3 ="""}
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



    if error == None:
        allnodes = []
        children = {}
        parents = {}
        linkset = {}
        IdAndName = {}
        idset = []
        default_color = "color:black"
        redcolor = "color:red;"
        searchNode = ''

        for x in proIDs:
            cn = '[' + x['PRO_name'] + ']'
            cu = x['PRO']
            # cpair = {'ID' : cu[31:], 'name': x['PRO_name']}
            cid = cu[31:]
            if cid not in IdAndName:
                IdAndName[cid] = x['PRO_name']
            x['PRO_name'] = cid + ' ' + cn
            # find the search node
            if cid == proId:
                searchNode = x['PRO_name']
            pn = '[' + x['Parent_name'] + ']'
            pu = x['Parent']
            x['Parent_name'] = pu[31:] + ' ' + pn
            idset.append({'PRO':cu, 'PRO_name':cid, 'Parent':pu, 'Parent_name':pu[31:]})



        for keyname in proIDs:
            proname = keyname['PRO_name']
            child_url = keyname['PRO']
            proparentname = keyname['Parent_name']
            parent_url = keyname['Parent']
            if proname not in linkset:
                linkset[proname] = '/pro2/entry/' + child_url[31:].replace('_',':')
            if proparentname not in linkset:
                linkset[proparentname] = '/pro2/entry/' + parent_url[31:].replace('_',':')


        for x in proIDs:
            pro = x['PRO_name']
            pro_parent = x['Parent_name']
            if pro not in allnodes:
                allnodes.append(pro)
            if pro_parent not in allnodes:
                allnodes.append(pro_parent)
            if pro_parent in children:
                children[pro_parent].append(pro)
            else:
                child = []
                child.append(pro)
                children[pro_parent] = child
            if pro in parents:
                parents[pro].append(pro_parent)
            else:
                p = []
                p.append(pro_parent)
                parents[pro] = p


    # request.session['IdAndName'] = IdAndName

    def getChildren(node):
        child_node = ''
        for child in children[node]:
            link = linkset[child]
            if child == searchNode:
                links = "{\"href\":\"" + link + "\", \"style\": \"" + redcolor + "\"}"
            else:
                links = "{\"href\":\"" + link + "\", \"style\": \"" + default_color + "\"}"
            if (child in children) and (len(children[child]) > 0):
                    # child_node += "{\"text\" : \"" + child + "\", \"children\" :[" + getChildren(child) + "]},"
                child_node += "{\"text\" : \"" + child + "\", \"a_attr\" : " + links + ", \"children\" :[" + getChildren(child) + "]},"
            else:
                    # links = "{\"href\":\"" + link + "\", \"style\": \"" + redcolor + "\"}"
                child_node += "{\"text\" : \"" + child+ "\", \"a_attr\" : " + links + ", \"children\" :[ ]},"
        return child_node

    json = ''
    for node in allnodes:
        if node not in parents:
            link = linkset[node]
            links = "{\"href\":\"" + link + "\", \"style\": \"" + default_color + "\"}"
            if node in children and len(children[node]) > 0:
                # json += "{\"text\" : \"" + node + "\", \"children\" :[" + getChildren(node) + "]},"
                json += "{\"text\" : \"" + node + "\", \"a_attr\" : " + links + ", \"children\" :[" + getChildren(node) + "]},"
            else:
                json += "{\"text\" : \"" + node + "\", \"a_attr\" : " + links + ", \"children\" :[]},"

    json = re.sub(r',]}', ']}', json)
    json = re.sub(r',$', '', json)
    json = "[" + json.replace(",]}", "]}") + "]"

    # buildtree(proIDs)

    # return JsonResponse(colorset, safe=False)
    return HttpResponse(json)

#
# def view_hierarchy_idandname(request, proId):
#     proId = proId.replace(':','_')
#     newquery = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
#     PREFIX obo: <http://purl.obolibrary.org/obo/>
#     PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#     PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
#
#     SELECT distinct ?PRO ?PRO_name ?Parent ?Parent_name
#     WHERE
#     {
# 	    {
# 		SELECT distinct ?ancestor as ?PRO ?PRO_name ?directParent as ?Parent ?Parent_name
# 		WHERE
# 		{
#   			{
#               SELECT distinct ?ancestor
#               WHERE
#               {
#                   values ?PRO_term {obo:"""
#
#     newquerymiddle = """}
#                   ?PRO_term rdfs:subClassOf ?parent .
#                   ?parent rdfs:subClassOf* ?ancestor .
#               }
#    			}
#          UNION {
#               values ?ancestor {obo:"""
#
#     newquerymiddle2 = """}
#           ?ancestor oboInOwl:id ?ancestor_id .
#         }
#         ?ancestor rdfs:subClassOf ?directParent .
#         ?directParent oboInOwl:id ?directParent_id .
#         ?ancestor oboInOwl:id ?ancestor_id .
#         ?ancestor rdfs:label ?ancestor_label .
#         ?directParent rdfs:label ?directParent_label .
#         FILTER(STRSTARTS(?directParent_id, 'PR:')|| STRSTARTS(?directParent_id, 'GO:'))
#         FILTER (!isBlank(?directParent))
#         FILTER(STRSTARTS(?ancestor_id, 'PR:')|| STRSTARTS(?ancestor_id, 'GO:'))
#         FILTER (!isBlank(?ancestor))
#         BIND(str(?ancestor_label) as ?PRO_name) .
#         BIND(str(?directParent_label) as ?Parent_name) .
#       }
# 	    }
# 	    UNION
# 	    {
#       SELECT distinct ?children as ?PRO ?PRO_name ?directParent as ?Parent ?Parent_name
#       WHERE
#       {
#          {
#             SELECT distinct ?children
#             WHERE
#             {
#                 values ?PRO_term {obo:"""
#
#     newquerymiddle3 ="""}
#                 ?children rdfs:subClassOf* ?PRO_term .
#             }
#          }
#          UNION {
#               values ?children {obo:"""
#
#     newquerymiddle4 = """}
#               ?children oboInOwl:id ?children_id .
#         }
#         ?children rdfs:subClassOf ?directParent .
#         ?directParent rdfs:subClassOf* obo:"""
#
#     newquerytail = """ .
#         ?directParent oboInOwl:id ?directParent_id .
#         ?children oboInOwl:id ?children_id .
#         ?children rdfs:label ?children_label .
#         ?directParent rdfs:label ?directParent_label .
#         FILTER(STRSTARTS(?directParent_id, 'PR:')|| STRSTARTS(?directParent_id, 'GO:'))
#         FILTER (!isBlank(?directParent))
#         FILTER(STRSTARTS(?children_id, 'PR:')|| STRSTARTS(?children_id, 'GO:'))
#         FILTER (!isBlank(?children))
#         BIND(str(?children_label) as ?PRO_name) .
#         BIND(str(?directParent_label) as ?Parent_name) .
#       }
#         }
#         }"""
#
#     fnewquery = newquery + proId + newquerymiddle + proId + newquerymiddle2 + proId + newquerymiddle3 + proId + newquerymiddle4 + proId + newquerytail
#     sparqlSearch = SparqlSearch()
#     proIDs, error = sparqlSearch.executeQuery(fnewquery)
#
#
#
#     if error == None:
#         allnodes = []
#         children = {}
#         parents = {}
#         linkset = {}
#         IdAndName = {'PR_000018263':'amino acid chain'}
#         idset = []
#         default_color = "color:black"
#         redcolor = "color:red;"
#         searchNode = ''
#
#         for x in proIDs:
#             cu = x['PRO']
#             cid = cu[31:]
#             if cid not in IdAndName:
#                 IdAndName[cid] = x['PRO_name']
#             x['PRO_name'] = cid
#             # find the search node
#             if cid == proId:
#                 searchNode = x['PRO_name']
#             pu = x['Parent']
#             x['Parent_name'] = pu[31:]
#             if pu not in IdAndName:
#                 IdAndName[pu] = x['Parent_name']
#             idset.append({'PRO':cu, 'PRO_name':cid, 'Parent':pu, 'Parent_name':pu[31:]})
#
#
#         # print(IdAndName)
#         # print(proIDs)
#         # print(idset)
#         # request.session['idset'] = idset
#         # print(searchNode)
#
#         for keyname in proIDs:
#             proname = keyname['PRO_name']
#             child_url = keyname['PRO']
#             proparentname = keyname['Parent_name']
#             parent_url = keyname['Parent']
#             if proname not in linkset:
#                 linkset[proname] = '/entry/' + child_url[31:].replace('_',':')
#             if proparentname not in linkset:
#                 linkset[proparentname] = '/entry/' + parent_url[31:].replace('_',':')
#
#
#         for x in proIDs:
#             pro = x['PRO_name']
#             pro_parent = x['Parent_name']
#             if pro not in allnodes:
#                 allnodes.append(pro)
#             if pro_parent not in allnodes:
#                 allnodes.append(pro_parent)
#             if pro_parent in children:
#                 children[pro_parent].append(pro)
#             else:
#                 child = []
#                 child.append(pro)
#                 children[pro_parent] = child
#             if pro in parents:
#                 parents[pro].append(pro_parent)
#             else:
#                 p = []
#                 p.append(pro_parent)
#                 parents[pro] = p
#
#
#     # request.session['IdAndName'] = IdAndName
#
#     def getChildren(node):
#         child_node = ''
#         for child in children[node]:
#             link = linkset[child]
#             # print('this is child', child)
#
#             if child == searchNode:
#                 links = "{\"href\":\"" + link + "\", \"style\": \"" + redcolor + "\", \"tittle\": \""+ IdAndName[child] +"\"}"
#             else:
#                 links = "{\"href\":\"" + link + "\", \"style\": \"" + default_color + "\", \"tittle\": \""+ IdAndName[child] +"\"}"
#             if (child in children) and (len(children[child]) > 0):
#                     # child_node += "{\"text\" : \"" + child + "\", \"children\" :[" + getChildren(child) + "]},"
#                 child_node += "{\"text\" : \"" + child + "\", \"a_attr\" : " + links + ", \"children\" :[" + getChildren(child) + "]},"
#             else:
#                     # links = "{\"href\":\"" + link + "\", \"style\": \"" + redcolor + "\"}"
#                 child_node += "{\"text\" : \"" + child+ "\", \"a_attr\" : " + links + ", \"children\" :[ ]},"
#         return child_node
#
#     json = ''
#     for node in allnodes:
#         if node not in parents:
#             link = linkset[node]
#             links = "{\"href\":\"" + link + "\", \"style\": \"" + default_color + "\", \"tittle\": \""+ IdAndName[node] +"\"}"
#             if node in children and len(children[node]) > 0:
#                 # json += "{\"text\" : \"" + node + "\", \"children\" :[" + getChildren(node) + "]},"
#                 json += "{\"text\" : \"" + node + "\", \"a_attr\" : " + links + ", \"children\" :[" + getChildren(node) + "]},"
#             else:
#                 json += "{\"text\" : \"" + node + "\", \"a_attr\" : " + links + ", \"children\" :[]},"
#
#     json = re.sub(r',]}', ']}', json)
#     json = re.sub(r',$', '', json)
#     json = "[" + json.replace(",]}", "]}") + "]"
#
#     # buildtree(proIDs)
#
#     # return JsonResponse(colorset, safe=False)
#     return HttpResponse(json)
