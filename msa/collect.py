from database.sparql import SparqlSearch
from database.fetch import *
from .msa_data import *
from .entry import *
from .record import *

_UNMOD_TERMS = ["UnMod", "PhosRes-", "unmodified", "unphospho", "UnPhos"]

def mark_group(f):
    # mark groups
    for r in f:
        if r.Cat == 'organism-gene':
            r.Group = 'msa-orthoform'
        elif r.Cat == 'organism-sequence':
            r.Group = 'msa-isoform'
        elif r.Cat == 'organism-modification':
            r.Group = 'msa-ptmform'
    return f

# def collect_myself(id):
#     # if no proteoforms is returned by collect_pro,
#     # just display the requested id itself.
#     obj = ENTRY.batch_initial([id], True)[0]
#     all = {id: new_seqrecord(obj)}
#     return all


def collect_pro(dao, proid, sameTaxon=False, taxon=None):
    # print(sameTaxon)
    # print("collect_pro: proid: "+proid)
    # print(taxon)
    all = {}
    formObjs = proteoforms(dao, proid, sameTaxon, taxon)
    # change entry's Group
    formObjs = mark_group(formObjs)
    # add proteoforms as new records
    for formObj in formObjs:
        all[formObj.id] = new_seqrecord(formObj)
    return all


def collect_myself(dao, ids):
    # if no proteoforms is returned by collect_pro,
    # just display the requested id itself.
    obj = ENTRY.batch_initial(dao, [ids], True)[0]
    # print(obj)
    # print(id , type(id))
    if type(ids) is not list:
        all = {ids: new_seqrecord(obj)}
    else:
        for id in ids:
            all = {id: new_seqrecord(obj)}
    return all


def check_unmod(f):
    for unmod in _UNMOD_TERMS:
        if f.name.find(unmod) > -1:
            return True
    else:
        return False


def proteoforms(dao, proid, sameTaxon, taxon, full=True):
    """
    :param id
    :return: forms entry objects
    """
    # try:
    # get all forms id
    # dao = DAO(proid)
    forms = dao.get_children(proid, sameTaxon, taxon)
    # print(forms)
    # intial all terms
    formObjs = ENTRY.batch_initial(dao, forms, full)

    # clean the forms objects
    for f in formObjs[:]:
        # print f.id, f.dbxrefs

        # remove unmod forms (they don't have dbxref)
        if check_unmod(f):
            formObjs.remove(f)
            continue

        # remove no dbxref terms
        if len(f.dbxrefs) == 0:
            formObjs.remove(f)
            continue

        # if dbxref ends with -1, check if request id doesn't have "-1",
        # the dbxref removes "-1"
        xref = f.dbxrefs[0]
        if xref.endswith("-1") and xref[:-2] == id:
            f.dbxrefs[0] = id

    return formObjs

# def collect_pro(proid, sameTaxon=False, taxon=None):
#     print('enter collect pro')
#     all = {}
#     formObjs = proteoforms(proid, sameTaxon, taxon)
#     # change entry's Group
#     formObjs = mark_group(formObjs)
#     # add proteoforms as new records
#     for formObj in formObjs:
#         all[formObj.id] = new_seqrecord(formObj)
#
#     return all
#
# def proteoforms(proid,sameTaxon,taxon,full=True):
#     print('enter proteoforms')
#     forms = get_children_by_query(proid) # need to remain only relevent children
#
#     forms.append(proid)
#     xrefs = get_UniprotKB_ids(forms)
#     idfiter = []
#     for a in xrefs.keys():
#         if a not in idfiter:
#             idfiter.append(a)
#     print('idfiter',idfiter)
#     print('check childrens: ',forms)
#     formObjs = ENTRY.batch_initial(idfiter, full)
#     # clean the forms objects
#     for f in formObjs:
#         # remove unmod forms (they don't have dbxref)
#         if check_unmod(f):
#             del f
#             continue
#         # remove no dbxref terms
#         if len(f.dbxrefs) == 0:
#             del f
#             continue
#
#         # if dbxref ends with -1, check if request id doesn't have "-1",
#         # the dbxref removes "-1"
#         xref = f.dbxrefs[0]
#         if xref.endswith("-1") and xref[:-2] == id:
#             f.dbxrefs[0] = id
#
#     return formObjs
#
# def childrenAndBatch(id):
#     children = get_children_by_query(id)
#     info = pass_node_info_by_ids(children)
#
#     return info


# def check_unmod(f):
#     for unmod in _UNMOD_TERMS:
#         if f.name.find(unmod) > -1:
#             return True
#     else:
#         return False

def new_seqrecord(obj):
    """ add Entry objects to all{}. """
    r = RECORD()
    r.seqRecord = obj.generate_seqrecords()
    return r
