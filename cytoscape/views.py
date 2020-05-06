from django.shortcuts import render
from django.http import HttpResponse
import requests
from database.fetch import *
from .run import *


def sparql_cyto_view(request, ids):
    context = {}
    ids = ids.replace('/','')
    if request.method == 'POST':
        ids = request.POST.get('id', None)
    if ids.startswith('PR:') and len(ids) < 12:
        context['cyto_script'] = pro_run(ids)
        context['uniprot'] = True
        return render(request, 'entry_cw_pro.html', context)
    else:
        context['cyto_script'] = pro_run(ids)
        context['uniprot'] = False
        return render(request, 'entry_cw_pro.html', context)

def download_xgmml(request):
    network = request.POST.get('xgmmlNetwork', '')
    response = HttpResponse(network, content_type='text/xgmml')
    response['Content-Disposition'] = 'attachment; filename=cytoscapeView.xgmml'
    return response