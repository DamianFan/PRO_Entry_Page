from database.fetch import *
from django.shortcuts import render
from django.http import HttpResponse
from .entry import *
from .hierarchy import *
from msa.collect import *
import numpy as np
from msa.views import loadingMSA

# Create your views here.
def process(request):
    id = 'PR:Q15796'
    children = ['PR:Q15796', 'PR:000050145', 'PR:000025960', 'PR:000000474', 'PR:000000473', 'PR:000000472', 'PR:000000471', 'PR:000000470', 'PR:000049281', 'PR:Q15796-2', 'PR:Q15796-1', 'PR:000045371', 'PR:000036554', 'PR:000025937', 'PR:000025936', 'PR:000025935', 'PR:000025934', 'PR:000036556', 'PR:000025938', 'PR:000045494', 'PR:000049284', 'PR:000049283', 'PR:000049282']
    string = 'A smad2 isoform Long phosphorylated form in which the phosphorylation occurs at the last two Ser residues within the SSxS C-terminal motif by TGF-beta pathway activation. Example: UniProtKB:Q15796-1, Ser-465/Ser-467,MOD:00046.'
    result = pass_node_info_by_ids(['PR:000025934'])


    return HttpResponse(result)

def test(request):
    return render(request, 'entry_page_test.html',{'mod': 'view', 'query': 'entry'})

def entry(request, proId):

    content = load_entry(proId)
    content['msaview'] = loadingMSA(request, 'entry', "PR:000025934")

    return render(request, 'base.html',content)


