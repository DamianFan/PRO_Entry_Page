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


# Create your views here.
def process(request):
    id = 'PR:000049283'
    children = ['PR:Q15796', 'PR:000050145', 'PR:000025960', 'PR:000000474', 'PR:000000473', 'PR:000000472', 'PR:000000471', 'PR:000000470', 'PR:000049281', 'PR:Q15796-2', 'PR:Q15796-1', 'PR:000045371', 'PR:000036554', 'PR:000025937', 'PR:000025936', 'PR:000025935', 'PR:000025934', 'PR:000036556', 'PR:000025938', 'PR:000045494', 'PR:000049284', 'PR:000049283', 'PR:000049282']
    string = 'A smad2 isoform Long phosphorylated form in which the phosphorylation occurs at the last two Ser residues within the SSxS C-terminal motif by TGF-beta pathway activation. Example: UniProtKB:Q15796-1, Ser-465/Ser-467,MOD:00046.'
    result = get_UniprotKB_ids([id])
    sequences = [SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS'), id='PR:Q15796', name='mothers against decapentaplegic homolog 2 (human)', description='', dbxrefs=['UniProtKB:Q15796']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS'), id='PR:Q15796-1', name='mothers against decapentaplegic homolog 2 isoform Long (human)', description='', dbxrefs=['UniProtKB:Q15796-1']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS'), id='PR:Q15796-2', name='mothers against decapentaplegic homolog 2 isoform Short (human)', description='', dbxrefs=['UniProtKB:Q15796-2']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS'), id='PR:Q62432-2', name='mothers against decapentaplegic homolog 2 isoform Short (mouse)', description='', dbxrefs=['UniProtKB:Q62432-2']), SeqRecord(seq=Seq(''), id='PR:000049282', name='mothers against decapentaplegic homolog 2, initiator methionine removed phosphorylated 1 (human)', description=' 2-467, Ser-465/Ser-467, MOD:00046', dbxrefs=['UniProtKB:Q15796. UniProtKB:Q15796']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK'), id='PR:000049283', name='mothers against decapentaplegic homolog 2, initiator methionine removed phosphorylated 5 (human)', description=' 2-467, Thr-220, MOD:00047|Ser-465/Ser-467, MOD:00046', dbxrefs=[]), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKKSMS'), id='PR:Q62432', name='mothers against decapentaplegic homolog 2 (mouse)', description='', dbxrefs=['UniProtKB:Q62432']), SeqRecord(seq=Seq(''), id='PR:000000470', name='smad2 sequence variant R133C (human)', description=' Arg-133, CHEBI:29950', dbxrefs=[]), SeqRecord(seq=Seq(''), id='PR:000000471', name='smad2 sequence variant L440R (human)', description=' Leu-440, CHEBI:29952', dbxrefs=[]), SeqRecord(seq=Seq(''), id='PR:000000472', name='smad2 sequence variant P445H (human)', description=' Pro-445, CHEBI:29979', dbxrefs=[]), SeqRecord(seq=Seq(''), id='PR:000000473', name='smad2 sequence variant D450E (human)', description=' Asp-450, CHEBI:29972', dbxrefs=[]), SeqRecord(seq=Seq(''), id='PR:000000474', name='smad2 sequence variant 5 (human)', description=' 2-343, 359-467', dbxrefs=[]), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS'), id='PR:Q62432-1', name='mothers against decapentaplegic homolog 2 isoform Long (mouse)', description='', dbxrefs=['UniProtKB:Q62432-1']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS'), id='PR:O70436', name='mothers against decapentaplegic homolog 2 (rat)', description='', dbxrefs=['UniProtKB:O70436']), SeqRecord(seq=Seq('MNGLLHMHGPAVKKLLGWKIGEDEEKWCEKAVEALVKKLKKKNNGCGTLEDLEC...SMT', 'IUPACProtein()'), id='PR:P45896', name='dwarfin sma-3 (worm)', description='', dbxrefs=['UniProtKB:P45896']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSASGSSGAGGGGEQNGQEEKWCEKAVKSLVKKLK...SMS', 'IUPACProtein()'), id='PR:Q9I9P9', name='mothers against decapentaplegic homolog 2 (zebrafish)', description='', dbxrefs=['UniProtKB:Q9I9P9'])]
    # key_value = result.keys()
    #
    # sss = [SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKKSMS'), id='PR:000049283', name='mothers', description=' 2-467, Thr-220, MOD:00047|Ser-465/Ser-467, MOD:00046', dbxrefs=[])]
    # ssss = [SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKKSMS'), id='PR:Q15796', name='mothers against decapentaplegic homolog 2 (human)', description='', dbxrefs=['UniProtKB:Q15796'])]
    #
    # SeqIO.write(sequences,'example.fasta','fasta')
    # print(result)
    # print(key_value)
    print(result)
    return HttpResponse(result)

def test(request):
    return render(request, 'entry_page_test.html',{'mod': 'view', 'query': 'entry'})

def entry(request, proId):

    content = load_entry(proId)
    content['msaview'] = loadingMSA(request, 'entry', "PR:000025934")

    return render(request, 'base.html',content)

def obo(request, proId):
    url = "https://research.bioinformatics.udel.edu/PRO_API/V1/obo/"+proId
    response = requests.get(url)

    return HttpResponse(response, content_type="text/plain")


