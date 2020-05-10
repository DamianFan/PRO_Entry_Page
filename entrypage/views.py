from database.fetch import *
from django.shortcuts import render
from django.http import HttpResponse
from .entry import *
from .hierarchy import *
from msa.collect import *
import numpy as np
from msa.views import loadingMSA
from msa.msa_data import *

import requests

from Bio import AlignIO
from Bio import SeqIO
from Bio.Align.Applications import MuscleCommandline
from Bio.Align import MultipleSeqAlignment


# Create your views here.
def process(request):
    id = 'PR:000025934'
    children = ['PR:Q15796', 'PR:000050145', 'PR:000025960', 'PR:000000474', 'PR:000000473', 'PR:000000472', 'PR:000000471', 'PR:000000470', 'PR:000049281', 'PR:Q15796-2', 'PR:Q15796-1', 'PR:000045371', 'PR:000036554', 'PR:000025937', 'PR:000025936', 'PR:000025935', 'PR:000025934', 'PR:000036556', 'PR:000025938', 'PR:000045494', 'PR:000049284', 'PR:000049283', 'PR:000049282']
    string = 'A smad2 isoform Long phosphorylated form in which the phosphorylation occurs at the last two Ser residues within the SSxS C-terminal motif by TGF-beta pathway activation. Example: UniProtKB:Q15796-1, Ser-465/Ser-467,MOD:00046.'
    result = get_xref_by_ids([id])
    # sequences = [SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS', 'IUPACProtein()'), id='PR:Q15796', name=' hSMAD2', description='', dbxrefs=['UniProtKB:Q15796']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS', 'IUPACProtein()'), id='PR:000036555', name=' mSMAD2', description='Ser-465/Ser-467, MOD:00046|MOD:01148.', dbxrefs=['UniProtKB:Q62432-1']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS', 'IUPACProtein()'), id='PR:000036554', name=' hSMAD2', description='Lys-19, MOD:00064|Ser-465/Ser-467, MOD:00046.', dbxrefs=['UniProtKB:Q15796-1']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS', 'IUPACProtein()'), id='PR:000025943', name=' mSMAD2', description='Ser-435/Ser-437, MOD:00046.', dbxrefs=['UniProtKB:Q62432-2']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS', 'IUPACProtein()'), id='PR:000045494', name=' hSMAD2', description='Ser-435/Ser-437, PR:000026291.', dbxrefs=['UniProtKB:Q15796-2']), SeqRecord(seq=Seq(''), id='PR:000028327', name='SMAD2', description='', dbxrefs=[]), SeqRecord(seq='', id='PR:000018296', name='SMAD2', description='', dbxrefs=[]), SeqRecord(seq='', id='PR:000000574', name='SMAD2', description='', dbxrefs=[]), SeqRecord(seq='', id='PR:000025960', name='hSMAD2', description='', dbxrefs=[]), SeqRecord(seq='', id='PR:000000572', name='SMAD2', description='', dbxrefs=[]), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS', 'IUPACProtein()'), id='PR:Q62432', name=' mSMAD2', description='', dbxrefs=['UniProtKB:Q62432']), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSASGSSGAGGGGEQNGQEEKWCEKAVKSLVKKLK...SMS', 'IUPACProtein()'), id='PR:Q9I9P9', name=' z-SMAD2', description='', dbxrefs=['UniProtKB:Q9I9P9']), SeqRecord(seq='', id='PR:000000364', name=' mothers against DPP homolog 2', description='', dbxrefs=[]), SeqRecord(seq='', id='PR:000000573', name='SMAD2', description='', dbxrefs=[]), SeqRecord(seq='', id='PR:000002570', name='SMAD2', description='', dbxrefs=[]), SeqRecord(seq=Seq('MSSILPFTPPVVKRLLGWKKSAGGSGGAGGGEQNGQEEKWCEKAVKSLVKKLKK...SMS', 'IUPACProtein()'), id='PR:O70436', name=' rSMAD2', description='', dbxrefs=['UniProtKB:O70436']), SeqRecord(seq='', id='PR:000000576', name='SMAD2', description='', dbxrefs=[]), SeqRecord(seq='', id='PR:000002571', name='SMAD2', description='', dbxrefs=[]), SeqRecord(seq='', id='PR:000025973', name='SMAD2', description='', dbxrefs=[]), SeqRecord(seq='', id='PR:000000575', name='SMAD2', description='', dbxrefs=[])]
    #
    # SeqIO.write(sequences,'example.fasta','fasta')

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


