from database.fetch import *
from django.shortcuts import render
from django.http import HttpResponse
from .entry import *
from .hierarchy import *
from msa.collect import *
import numpy as np
from msa.views import loadingMSA
from msa.msa_data import *
from Bio.Alphabet import IUPAC
import requests
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import AlignIO
from Bio import SeqIO
from Bio.Align.Applications import MuscleCommandline
from Bio.Align import MultipleSeqAlignment
import datetime


# Create your views here.
def process(request):
    # id = 'PR:000000470'
    # children = ['PR:Q15796', 'PR:000050145', 'PR:000025960', 'PR:000000474', 'PR:000000473', 'PR:000000472', 'PR:000000471', 'PR:000000470', 'PR:000049281', 'PR:Q15796-2', 'PR:Q15796-1', 'PR:000045371', 'PR:000036554', 'PR:000025937', 'PR:000025936', 'PR:000025935', 'PR:000025934', 'PR:000036556', 'PR:000025938', 'PR:000045494', 'PR:000049284', 'PR:000049283', 'PR:000049282']
    # string = 'A smad2 isoform Long phosphorylated form in which the phosphorylation occurs at the last two Ser residues within the SSxS C-terminal motif by TGF-beta pathway activation. Example: UniProtKB:Q15796-1, Ser-465/Ser-467,MOD:00046.'
    # result = get_UniprotKB_ids([id])
    # # sequences = [SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS'), id='PR:Q15796', name='mothers against decapentaplegic homolog 2 (human)', description='', dbxrefs=['UniProtKB:Q15796']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS'), id='PR:Q15796-1', name='mothers against decapentaplegic homolog 2 isoform Long (human)', description='', dbxrefs=['UniProtKB:Q15796-1']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS'), id='PR:Q15796-2', name='mothers against decapentaplegic homolog 2 isoform Short (human)', description='', dbxrefs=['UniProtKB:Q15796-2']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS'), id='PR:Q62432-2', name='mothers against decapentaplegic homolog 2 isoform Short (mouse)', description='', dbxrefs=['UniProtKB:Q62432-2']), SeqRecord(seq=Seq(''), id='PR:000049282', name='mothers against decapentaplegic homolog 2, initiator methionine removed phosphorylated 1 (human)', description=' 2-467, Ser-465/Ser-467, MOD:00046', dbxrefs=['UniProtKB:Q15796. UniProtKB:Q15796']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK'), id='PR:000049283', name='mothers against decapentaplegic homolog 2, initiator methionine removed phosphorylated 5 (human)', description=' 2-467, Thr-220, MOD:00047|Ser-465/Ser-467, MOD:00046', dbxrefs=[]), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKKSMS'), id='PR:Q62432', name='mothers against decapentaplegic homolog 2 (mouse)', description='', dbxrefs=['UniProtKB:Q62432']), SeqRecord(seq=Seq(''), id='PR:000000470', name='smad2 sequence variant R133C (human)', description=' Arg-133, CHEBI:29950', dbxrefs=[]), SeqRecord(seq=Seq(''), id='PR:000000471', name='smad2 sequence variant L440R (human)', description=' Leu-440, CHEBI:29952', dbxrefs=[]), SeqRecord(seq=Seq(''), id='PR:000000472', name='smad2 sequence variant P445H (human)', description=' Pro-445, CHEBI:29979', dbxrefs=[]), SeqRecord(seq=Seq(''), id='PR:000000473', name='smad2 sequence variant D450E (human)', description=' Asp-450, CHEBI:29972', dbxrefs=[]), SeqRecord(seq=Seq(''), id='PR:000000474', name='smad2 sequence variant 5 (human)', description=' 2-343, 359-467', dbxrefs=[]), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS'), id='PR:Q62432-1', name='mothers against decapentaplegic homolog 2 isoform Long (mouse)', description='', dbxrefs=['UniProtKB:Q62432-1']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS'), id='PR:O70436', name='mothers against decapentaplegic homolog 2 (rat)', description='', dbxrefs=['UniProtKB:O70436']), SeqRecord(seq=Seq('MNGLLHMHGPAVKKLLGWKIGEDEEKWCEKAVEALVKKLKKKNNGCGTLEDLEC...SMT', 'IUPACProtein()'), id='PR:P45896', name='dwarfin sma-3 (worm)', description='', dbxrefs=['UniProtKB:P45896']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSASGSSGAGGGGEQNGQEEKWCEKAVKSLVKKLK...SMS', 'IUPACProtein()'), id='PR:Q9I9P9', name='mothers against decapentaplegic homolog 2 (zebrafish)', description='', dbxrefs=['UniProtKB:Q9I9P9'])]
    # # key_value = result.keys()
    # sequences =  [SeqRecord(seq=Seq('MQPLWLCWALWVLPLASPGAALTGEQLLGSLLRQLQLKEVPTLDRADMEELVIP...LQP',IUPAC.protein), id='PR:000036546', name='lefty 1 isoform 1 cleaved 1 (human)', description=' 77-366', dbxrefs=['UniProtKB:O75610-1']), SeqRecord(seq=Seq('MPFLWLCWALWALSLVSLREALTGEQILGSLLQQLQLDQPPVLDKADVEGMVIP...LQP',IUPAC.protein), id='PR:Q64280-1', name='left-right determination factor 1 isoform 1 (mouse)', description='', dbxrefs=['UniProtKB:Q64280-1'])]
    # SeqIO.write(sequences,'example.fasta','fasta')
    # print(result)
    id = 'PR:000000364'
    result = get_category_by_ids([id])
    for i in result:
        print(i)
    return HttpResponse(result)

def test(request,proId):
    content = load_entry(proId)
    content['msaview'] = loadingMSA(request, 'entry', proId)
    return render(request, 'entry_page_test.html',content)

def entry(request, proId):

    content = load_entry(proId)
    content['msaview'] = loadingMSA(request, 'entry', "PR:000025934")

    return render(request, 'base.html',content)

def resize(request, proId):
    content = load_entry(proId)
    content['msaview'] = loadingMSA(request, 'entry', proId)
    return render(request, 'entry_page_test.html', content)

def obo(request, proId):
    url = "https://research.bioinformatics.udel.edu/PRO_API/V1/obo/"+proId
    response = requests.get(url)

    return HttpResponse(response, content_type="text/plain")

def per_test(request):
    casenum = 1

    # o-g
    idlist = ['PR:Q15796','PR:O14709','PR:Q8BLY3','PR:Q8BVN9','PR:P27448','PR:O74963','PR:G5EBR8','PR:Q62950','PR:Q4V8E5','PR:Q4V8E4']
    # o-m
    # idlist = ['PR:000036308','PR:000036300','PR:000036304','PR:000035428','PR:000025934','PR:000025935','PR:000035421','PR:000035426','PR:000046207','PR:000050111']
    # g
    # idlist = ['PR:000003146','PR:000002031','PR:000002033','PR:000031365','PR:000007515','PR:000007519','PR:000036300','PR:000035423','PR:Q505J8','PR:000002030']
    # mo
    # idlist = ['PR:000021331','PR:000000383','PR:000044456','PR:000050090','PR:000050119','PR:000000651','PR:000000574','PR:000031533','PR:000003932','PR:000031360']
    # s
    # idlist = ['PR:000000468','PR:000044087','PR:000041854','PR:000041858','PR:000037979','PR:000010271','PR:000000145','PR:000040655','PR:000040656','PR:000041850']
    # o-s
    # idlist = ['PR:Q04912-3','PR:Q9UTS5-1','PR:Q9YHV4-1','PR:Q04912-2','PR:Q04912-6','PR:Q5VWK5-3','PR:Q9JI44-1','PR:Q62623-1','PR:Q68G31-1','PR:Q9D291-1']
    # f
    # idlist = ['PR:000025989','PR:000025824','PR:000001818','PR:000001810','PR:000001814','PR:000001023','PR:000001416','PR:000001926','PR:000001118','PR:000044673']



    for ddd in idlist:
        print('this is case ', casenum)
        casenum+=1

        test_id = ddd
        # oepageurl = "https://research.bioinformatics.udel.edu/pro/entry/"
        # oepageurl = "https://proconsortium.org/app/visual/cytoscape/pro/"
        # nepageurl = "https://research.bioinformatics.udel.edu/pro2/entry/"
        # nepageurl = "https://research.bioinformatics.udel.edu/pro2/cytoscape/view/"
        oepageurl = "https://research.bioinformatics.udel.edu/pro/visual/msa/tree/"
        nepageurl = "https://research.bioinformatics.udel.edu/pro2/msa/tree/"
        ourl = oepageurl + test_id
        nurl = nepageurl + test_id
        # url = "https://research.bioinformatics.udel.edu/pro2/entry/PR:Q15796"

        lto = []
        ltn = []
        # print('old page: ')
        for i in range(0,10):
            d1 = tt()
            requests.get(ourl)
            d2 = tt()
            x = d2-d1
            xx = str(x).replace('0:00:0','')
            xxx = float(xx)
            # print(x)
            lto.append(xxx)


        # print('new page: ')
        for j in range(0,10):
            d3 = tt()
            requests.get(nurl)
            d4 = tt()
            y = d4-d3
            yy = str(y).replace('0:00:0', '')
            yy = str(yy).replace('0:00', '')
            yyy = float(yy)
            # print(y)
            ltn.append(yyy)

        os = 0
        ns = 0

        for a in lto:
            os += a
        oavg = os / 10

        for b in ltn:
            ns += b
        navg = ns / 10


        print('current id: ', test_id)
        print('old result: ', lto)
        print('new result: ',ltn)
        print('old avg: ', oavg)
        print('new avg:', navg)
        print('\n')
    return HttpResponse(casenum)


def tt():
    # t = time.localtime()
    # current_time = time.strftime("%Y%m%d%H%M%S%f", t)
    # print(current_time)

    date = datetime.datetime.now()
    # print(date)
    return date