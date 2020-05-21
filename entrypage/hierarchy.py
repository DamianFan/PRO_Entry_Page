from database.sparql import SparqlSearch
from database.fetch import *

def idtree(proId):
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
    print('query', fnewquery)
    sparqlSearch = SparqlSearch()
    proIDs, error = sparqlSearch.executeQuery(fnewquery)

    if error == None:
        allnodes = []
        children = {}
        parents = {}
        linkset = {}
        IdAndName = {}
        default_color = "color:black"
        redcolor = "color:red;"
        searchNode = ''

        for x in proIDs:
            # cn = '[' + x['PRO_name'] + ']'
            cu = x['PRO']
            cn = cu[31:]
            # cpair = {'ID' : cu[31:], 'name': x['PRO_name']}
            cid = cn
            if cid not in IdAndName:
                IdAndName[cid] = x['PRO_name']
            x['PRO_name'] = cid
            # find the search node
            if cid == proId:
                searchNode = x['PRO_name']

            pu = x['Parent']
            pn = pu[31:]
            x['Parent_name'] = pn
            # idset.append({'PRO':cu, 'PRO_name':cid, 'Parent':pu, 'Parent_name':pu[31:]})
            print('before idandname, ', IdAndName)


        # print(searchNode)

        for keyname in proIDs:
            proname = keyname['PRO_name']
            child_url = keyname['PRO']
            proparentname = keyname['Parent_name']
            parent_url = keyname['Parent']
            if proname not in linkset:
                linkset[proname] = '/entrypage/' + child_url[31:].replace('_', ':')
            if proparentname not in linkset:
                linkset[proparentname] = '/entrypage/' + parent_url[31:].replace('_', ':')


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

    return json