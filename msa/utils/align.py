import sys
import subprocess
import threading

from django.conf import settings

from Bio import AlignIO
from Bio import SeqIO
from Bio.Align.Applications import MuscleCommandline
from Bio.Align import MultipleSeqAlignment

from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

class MuscleWithTimeout(object):
    """
    Timeout func: http://stackoverflow.com/questions/1191374/using-module-subprocess-with-timeout
    """
    def __init__(self, data):
        self.data = data
        self.process = None
        self.alignment = None

    def run(self, timeout):
        #print("???", self.data)
        #self.data = [SeqRecord(seq=Seq('MQPLWLCWALWVLPLASPGAALTGEQLLGSLLRQLQLKEVPTLDRADMEELVIP...LQP', IUPAC.protein), id=u'PR:000000643', name=u'LEFTY1/iso:1/Clv:1', description='', dbxrefs=[u'UniProtKB:O75610-1']), SeqRecord(seq=Seq('MPFLWLCWALWALSLVSLREALTGEQILGSLLQQLQLDQPPVLDKADVEGMVIP...LQP', IUPAC.protein), id=u'PR:000036547', name=u'mLEFTY1/iso:1/Clv:1', description='', dbxrefs=[u'UniProtKB:Q64280-1'])]

        def target():
            muscleCline = MuscleCommandline(settings.MUSCLE_EXE,clwstrict=True)
            #print(str(muscleCline))
            self.process = subprocess.Popen(str(muscleCline),
                                            stdin=subprocess.PIPE,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,
                                            shell=(sys.platform!="win32"))

            # for d in self.data:
            #     print(data[d] + " | "+ data[d].seqRecord)
            SeqIO.write(self.data, self.process.stdin, "fasta")
            self.process.stdin.close()
            #print(self.process.stdout)
            self.alignment = AlignIO.read(self.process.stdout, "clustal")

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            # print 'Terminating process'
            self.process.kill()
            thread.join()

        return self.alignment


class ALIGN(object):
    r"""
    Define ALIGN object for MSA view.
    Input: list of seqRecord objects.
    Alignment: biopython wrapper for MUSCLE
        http://www.drive5.com/muscle/manual/
        http://www.drive5.com/muscle/downloads.htm
    Output: two views in HTML format
      detailed view (DV): showing full length sequence, each position is an amino acid.
      overview (OV): sequence sketch, display length = full sequence/legend step. For each
                step, display amino acid if it's modified, otherwise show a dash line or
                gap.
    """

    def __init__(self):
        """
        Attributes:
        records -- a dict of RECORD object, key is id.
        alnRecords -- a list of seqRecords objects, keep seqRecords that has unique sequence that need to align
        modRecords -- a list of seqRecords objects, keep seqRecords that only need to decorate ptm
        align -- biopython align object, save MUSCLE output
        order --  An ordered id list based on Group attributes.
        alnLen -- alignment length
        alnRef -- if alignRecord's dbxref is not its id, keep alignment here. (prepare for mode that only contain ptmforms)
        """

        self.records = {}
        self.alnRecords = []
        self.modRecords = []
        self.align = []
        self.alnLen = 0
        self.alnRef = {}
        self.order = []


    def alignment(self, all):
        self.records = all
        #print(self.records)
        # separate records that needs alignment or just decorate
        self.set_align_mod()
        # MUSCLE multiple sequence alignment
        self.generate_alignment()
        if self.align is None:
            return
        # mv each alignment to corresponded MSARecords
        self.data_organize()
        # add align to each ptmforms (not participate alignment)
        self.data_organize_ptmforms()
        # get alignment length
        self.alnLen = self.align.get_alignment_length()
        # arrange records order to better display
        self.data_order()


    def set_align_mod(self):
        dbxrefsList = []
        for i in self.records.keys():
            r = self.records[i].seqRecord
            if len(set(r.dbxrefs) & set(dbxrefsList))==0:
                dbxrefsList.extend(r.dbxrefs)
                self.alnRecords.append(r)
            else:
                self.modRecords.append(r)


    def generate_alignment(self):
        """Perform alignment by MUSCLE, save result in align attribute."""
        #print(self.alnRecords)
        alen = len(self.alnRecords)
        if alen == 1:
            #print(self.alnRecords[0])
            self.align = MultipleSeqAlignment([self.alnRecords[0]])
            return
        elif alen > 30:
            data = self.alnRecords[:30]
            print "Only show first 30 entries"
        else:
            data = self.alnRecords

        muscle = MuscleWithTimeout(data)
        self.align = muscle.run(timeout=60)


    def data_organize(self):
        """mv each alignment to corresponded MSARecords."""       
        for aln in self.align:
            id = aln.id
            self.records[id].align = aln
            ref = self.records[id].seqRecord.dbxrefs
            if len(ref)>0 and not id == ref[0]:
                self.alnRef[ref[0]] = aln


    def data_organize_ptmforms(self):
        """
        Add alignment result for PTM Records.
        PTM Records share same sequence as their parent form and they are not submit to alignment.
        """

        for r in self.modRecords:
            id = r.id
            ref = self.records[id].seqRecord.dbxrefs[0]
            # if isoform is in align
            if self.records.has_key(ref):
                self.records[id].align = self.records[ref].align
            # check alnRef for more reference
            elif self.alnRef.has_key(ref):
                self.records[id].align = self.alnRef[ref]
            # fail to find alignment
            else:
                print "Can't get alignment for "+ r.id


    def data_order(self):
        """ check records group to determine order """
        order = [[] for x in xrange(4)]
        for r in self.records.values():
            r = r.seqRecord
            g = r.annotations["relationship"]
            if g=="msa-request":     order[0].append(r)
            elif g=="msa-orthoform": order[1].append(r)
            elif g=="msa-isoform":   order[2].append(r)
            elif g=="msa-ptmform":   order[3].append(r)
            else:                    order[0].append(r)
        order[2] = sorted(order[2], key=lambda x: x.id)
        # ptmforms' order is determined by dbxref
        # order[3] = sorted(order[3], key=lambda x: x.dbxrefs[0])
        order[3] = sorted(order[3], key=lambda x: x.name)
        self.order = [r.id for g in order for r in g ]
