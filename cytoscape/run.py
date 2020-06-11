from database.fetch import *
from .node import *
from .edge import *

def mark(ids,marker, nodes):
  """For each element in 'ids', give 'marker' value to its Group attribute."""
  for id in ids:
    id = id.replace(' ','')
    if id in nodes and nodes[id].Group == '':
      nodes[id].Group = marker



def pro_run(ids):
  nodes = {}
  siblingSwitch = True
  requestIds = ids
  outNodes,outEdges,childrenMenu = processing_pro(requestIds,siblingSwitch, nodes)
  return export(requestIds,outNodes,outEdges,siblingSwitch,childrenMenu, nodes)


def processing_pro(requestIds,siblingSwitch,nodes):
  """
  Get the id list, sibling switch and version ("pro" or "iptmnet"),
  return all node list, edge list of the network and
  children menu (a sorted int list of Level that bigger than requested ids).
  """
  id_list = [requestIds]
  nodes,outNodes,outEdges,hierarchy = process_cytoscape(requestIds,nodes)
  childrenMenu = get_children_menu(hierarchy, id_list, nodes)
  return outNodes,outEdges,childrenMenu


def uni_run(requestIds,siblingSwitch,nodes):
    return ''


def process_cytoscape(id,nodes):
    # 01 input an id
    # 02 relations(outEdge)
        # 02-01 get hierarchy based on this id
        # 02-02 get addition based on hierarchy
            # addition needs category
    # 03 restore the relationship_pair from hierarchy and addition
    # 04 get node information from id,hierarchy,addition
    # 05 add node information into node object
        # 05-01 pre caculate PROHierarchy for each node

    # outEdges is relationship
    # example: [[u'PR:P97471', 'is_a', 'PR:000000128', 'OBO', ''],[u'PR:P97471', 'is_a', 'PR:000029032', 'OBO', '']]


    request_id = [id] # set request id
    outEdges = get_tree_pair(id) # this outEdges contain basic relation of current id
    # 01 id = input

    # 02-01 start get hierarchy
    hierarchy = get_hierarchy_by_id(id)

    # hierarchy = [parents, children, complex, component, siblings]
    request_parents = hierarchy[0]
    request_children = hierarchy[1]
    request_sibling = hierarchy[4]
    # print('after get hierarchy')
    # 02-01-01 add complex and component into outEdges
    if len(hierarchy[2]) > 0:
        for copl in hierarchy[2]:
            outEdges.append([copl,'has_component',id,'OBO',''])
    if len(hierarchy[3]) > 0:
        for copn in hierarchy[3]:
            outEdges.append([id,'has_component',copn,'OBO',''])

    rel_set = []
    for i in hierarchy:
        for j in i:
            rel_set.append(j)
    rel_set = check_ids(rel_set)

    # 02-02 process addition
    addition,outEdges = process_addition(rel_set,outEdges)
    maddition = check_ids(addition)
    # print('check maddition',maddition)
    # 03 restore relations
    # outEdge
    # 03-01 filter addition for marker
    # request_addition = []
    # for ad in maddition:
    #     if ad not in rel_set:
    #         request_addition.append(ad)
    # print('request_addition: ',request_addition)
    # 05-01 pre caculate PROHierarchy for each node
    rel_dic,afterhierarchy,outEdges = get_hierarchy_by_ids(maddition,outEdges)
    mafterhierarchy = check_ids(afterhierarchy)

    # 04 get node information
    for i in rel_set:
        if i not in mafterhierarchy:
            mafterhierarchy.append(i)
    data = get_node_info_by_ids(mafterhierarchy)
    # print('data in run.py: ',data)
    # 05 restore node information into object based on data
    for PROTerm in data:
        id = PROTerm[0]
        rel = [[],[],[],[],[]]
        if id == "*":
            continue
        if id in rel_dic:
            rel = rel_dic[id]
        nodes[id] = NODE(PROTerm,rel)

    # 06 mark groups
    # print('execuate mark')
    mark(request_id, 'request', nodes)
    mark(request_parents,'parent',nodes)
    mark(request_sibling,'sibling',nodes)
    if len(request_id)< 12:
        mark(request_children, 'related', nodes)
    else:
        mark(maddition, 'child', nodes)



    # print('check request children: ',request_children)

    return nodes,mafterhierarchy,outEdges,rel_set


def process_cytoscape_uni(id,nodes):
    outEdges = get_tree_pair(id)


    return ''


def export(requestIds, outNodes, outEdges, siblingSwitch, childrenMenu, nodes):
    r"""
    Get request id list, all nodes and edges list, sibling switch, and children menu list,
    print all data in javascript variable.
    Network is written in json format, describe in cytoscape.js:
    http://cytoscape.github.io/cytoscape.js/#notation/elements-json
    """
    nodeData = export_node(outNodes, nodes)
    edgeData = export_edge(outEdges, nodes)
    rtn = ''
    rtn += "var eleObj = {nodes:[" + nodeData + "],edges:[" + edgeData[:-1] + "]};"
    rtn += 'var requestIds =["' + '","'.join(sorted(requestIds)) + '"];'
    rtn += 'var siblingSwitch =' + ('1' if siblingSwitch else '0') + ';'
    rtn += 'var childrenMenu = ["' + '","'.join(map(str, childrenMenu)) + '"];'
    rtn += 'var obourlDownload = "' + get_url(outNodes, 'OBOEXACT') + '";'
    rtn += 'var pafurlDownload = "' + get_url(outNodes, 'PAFEXACT') + '";'
    return rtn


def export_node(outNodes, nodes, nodeData=''):
    # set ROOT
    for n in g.ROOT:
        if n in outNodes:
            nodeData += nodes[n].jsjson()
    # output nodes
    for n in sorted(outNodes):
        if n in g.ROOT + g.DELROOT: continue
        nodeData += nodes[n].jsjson()
    return nodeData


def export_edge(outEdges, nodes, edgeData=''):
    for e in outEdges:
        edge = EDGE()
        edgeData += edge.jsjson(e)
    return edgeData