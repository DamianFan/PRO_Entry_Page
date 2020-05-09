from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from .msa_data import *
from .collect import *
from .align import *
from .decorate import *
from .dump import *
import requests
import request


def test(request):
    a = ['PR:000000650']
    result=get_children_by_query(a)
    return HttpResponse(result)


def loadingMSA(request, mod, query):
    return render(request, 'msa/msa.html', {'mod': mod, 'query': query})



def MsaView(request, mod, query):
    context = {
        'query': query,
        'mod': mod,
        'result': ''
    }
    requestList = query.split(',')
    id = requestList.pop(0)
    all = get_data(requestList, id, mod)
    # for i in all:
    #     print('row in all', i)
    a = ALIGN()
    a.alignment(all)
    # decorate
    d = DECORATE(a)
    d.draw()
    # dump
    context['result'] = dump_view(d)
    return JsonResponse(context)


def get_data(requestList, id, mod):
    all = generate(requestList,id,mod)
    return all

def generate(requestList, id, mod):
    entryset = get_terms([id])
    entry = entryset[0]
    # print('entry in generate: ',entry)
    if entry.category == "organism-gene":
        parent = id
        parentandname = get_all_direct_parent(id)
        parentset = []
        for i in parentandname:
            parentset.append(i[0])
        parentandcate = get_category_by_ids(parentset)
        for p in parentandcate:
            if p['Category']!= '':
                parent = p['id']
                break
        assert parent != ''
    else: parent = id

    all = None
    # print('parent in generate: ',parent)
    if mod == 'entry':
        if entry.category == 'gene':

            all = collect_pro(parent) # this should be collect_pro
        else:
            all = collect_pro(parent)
    elif mod.startswith("full"):
        # isoforms and ptmforms can be with any taxon ids
        all = collect_pro(parent)
        if mod == "full-selected":
            for e in all.keys():
                if e != id and e not in requestList:
                    del all[e]

    if not all:
        all = collect_myself(parent)

    return all