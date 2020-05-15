# The main alignment program is from iptmnet's msa app
# I modified a lot in entry.py, collect.py, fetch.py and preprocess.py

from django.shortcuts import render
from django.http import JsonResponse
from msa.utils.collect import *
from msa.utils.align import *
from msa.utils.dao import DAO
from msa.utils.decorate import *
from msa.utils.dump import *
import pickle


def loadingMSA(request, mod, query):
    return render(request, 'msa/msa.html', {'mod': mod, 'query': query})

def MsaView(request, mod, query):
    """
    "entry" shows request id + isoform + ptmforms
    "full" shows request id + ptmforms AND ortholog's id + ptmforms
    "full-selected" bases on "full", but only display listed ids
    :param mod: possible values are "entry", "entry-full", "full"
    :param query: a list of valid id (which are in d_iptm_entry table),
                  only in mod "full-selected", [1:] will be used to 
                  filter entries that are displayed
    :return: decorated aligned json for display
    """
    context = {
        'query': query,
        'mod': mod,
        'result': ''
    }

    requestList = query.split(',')
    id = requestList.pop(0)

    all = get_data(requestList, id, mod)

    #print(all)
    # for a in all:
    #     print(all[a].seqRecord)
    # alian
    a = ALIGN()
    a.alignment(all)

    # decorate
    d = DECORATE(a)
    d.draw()

    # dump
    context['result'] = dump_view(d)
    return JsonResponse(context)


def get_data(requestList, id, mod):
    # debug
    all = generate(requestList, id, mod)

    # file = os.path.join(os.path.dirname(__file__), '../preprocess', 
    # id+'-'+mod[0:1]+'.pk')
    # try:
    #     # try loading preprocess data, if fails, collect data now
    #     with open(file, 'rb') as f:
    #         all = pickle.load(f)
    # except:
    #     all = generate(requestList, id, mod)                
    #     with open(file, 'wb') as f:
    #      pickle.dump(all, f)
    return all


def generate(requestList, id, mod):
    dao = DAO(id)
    entry = dao.get_terms([id])[0]
    # print(entry)
    # print(entry.category)
    # print(mod)

    if entry.category == "organism-gene":
        # parent = dao.get_direct_parent(id)
        # assert parent != ''
        parent = id
    elif entry.category == "gene": # keep this condition?
        parent = id
    else:
        parent = id

    all = None
    if mod == "entry":
        # isoforms and ptmforms must have the same taxon id with the request one
        taxon = dao.get_taxon(id)
        if entry.category == "gene":
            all = collect_pro(dao, parent)
        else:
            #print("should be here")
            all = collect_pro(dao, parent, sameTaxon=True, taxon=taxon)
    elif mod.startswith("full"):
        # isoforms and ptmforms can be with any taxon ids
        all = collect_pro(dao, parent)
        if mod == "full-selected":
            for e in all.keys():
                if e != id and e not in requestList:
                    del all[e]

    if not all:
        all = collect_myself(dao, parent)

    return all
