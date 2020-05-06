from .models import *
from database.sparql import SparqlSearch
from database.fetch import *
from .collect import *
import urllib
from itertools import chain
import json

def get_terms(ids):
    # subject, name, definition, category
    result = pass_node_info_by_ids(ids)
    term_list = []
    for case in result:
        robj = MvOboTerm()
        robj.subject = case['id']
        robj.name = case['name']
        robj.definition = case['PRO_termDef']
        robj.category = case['Category']
        term_list.append(robj)
    return term_list


# direct parent: get_all_direct_parent()

def get_direct_parent(id):
    parent = get_all_direct_parent(id)
    return parent

def get_children_and_taxon(id):
    childrenlist = []



    return childrenlist