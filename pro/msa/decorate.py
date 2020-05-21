from collections import defaultdict
from .msaview import *
from .record import *

modTypeList = ['p', 'ac', 'g', 'm', 'ub']
conservedModAa = {'p': ["S", "T"],
                  'g': ["S", "T"]}

pubmed = "http://www.ncbi.nlm.nih.gov/pubmed/"

class DECORATE(object):
    """Draw two views with ALIGN object."""

    def __init__(self, a):
        """
        input: take an ALIGN object.
        conservation -- modified position(align position): conservation[alnpos] = (aa,mod)
                (only capture one possibility) used to judge conservation
        """

        self.records = a.records
        self.order = a.order
        self.alnLen = a.alnLen
        self.stat = defaultdict(list)
        self.conservation = {}
        self.dv = VIEW()
        self.ov = VIEW()


    def draw(self):
        if self.alnLen == 0:
            return 
        self.summary()
        self.preprocess()
        self.detailview()
        self.overview()


    def summary(self):
        """View summary information. Used to generate view head menu."""
        self.stat["enzyme"] = {}
        for id in self.records:
            ptms = self.records[id].seqRecord.annotations["modification"]
            for pos in ptms:
                ptmArray = ptms[pos]
                for ptm in ptmArray:
                    mod = ptm.modType
                    if not mod in modTypeList:
                        mod = 'o'
                    self.stat["modType"].append(mod)
                    if not len(ptm.enzyme) == 0:
                        self.stat["enzyme"] = dict(ptm.enzyme.items())
                        self.records[id].enzymes.extend(ptm.enzyme.values())
                    if not ptm.source == '':
                        self.stat["source"].append(ptm.source)
                    if not ptm.note == '':
                        self.stat["note"].append(ptm.note)
            self.records[id].enzymes = set(self.records[id].enzymes)
        for key in self.stat.keys():
            if key == "enzyme": continue
            self.stat[key] = list(set(self.stat[key]))


    def preprocess(self):
        """Preprocess alignment data. Help to judge conservation."""
        for id in self.order:
            obj = self.records[id]
            alnSeq = obj.align
            gapCounter = 0

            for p in range(len(alnSeq)):
                aa = alnSeq[p]
                if aa == '-':
                    gapCounter += 1
                else:
                    seqPos = p - gapCounter + 1
                    sites = obj.seqRecord.annotations["modification"]
                    if seqPos in sites:
                        self.conservation[p] = (aa, sites[seqPos][0].modType)
                        # ptm summary
                        ptmArray = obj.seqRecord.annotations["modification"][seqPos]
                        cls, title = [], []
                        if len(ptmArray) > 1:
                            # how many distinct mod type in multiple ptm sites
                            if len(set([ptm.modType for ptm in ptmArray])) > 1:
                                cls.append("msa-mod-multi")
                        # organize each ptm for display class and title(tooltip)
                        # ptmSum[modaapos][enz]=[pmids]
                        ptmSum = defaultdict(dict)
                        for ptmObj in ptmArray:
                            mod = ptmObj.modType
                            modaapos = mod + alnSeq[p] + '-' + str(seqPos)
                            enz = ",".join(set(ptmObj.enzyme.values())) if len(ptmObj.enzyme) > 0 else ''

                            if enz not in ptmSum[modaapos]:
                                ptmSum[modaapos][enz] = []
                            ptmSum[modaapos][enz].extend(ptmObj.pmid)
                            if not mod in modTypeList:
                                mod = "o"
                            cls.append("msa-mod-" + mod)
                            cls.extend(ptmObj.cls_ptm())
                        for s in ptmSum:
                            for e in ptmSum[s]:
                                title.append("%(modaapos)s %(enz)s PMID: %(pmid)s" % dict(modaapos=s, enz='(%s)' % e if len(e)>0 else '', pmid=self.__evidence(ptmSum[s][e])))
                                obj.ptmInAln[p] = list(set(cls)), "<br/>".join(set(title))


    def detailview(self):
        self.dv.tid = 'DV'
        self.dv.numOfSeq = len(self.order)
        self.dv.alnLen = self.alnLen
        self.dv.scale = 1
        self.dv.equalSymbol = '='
        self.dv.header = self.__draw_header_detailed()

        for id in self.order:
            obj = self.records[id]
            alnSeq = obj.align

            gapCounter = 0
            for p in range(len(alnSeq)):
                aa = alnSeq[p]
                cls, seqPos, gapCounter = self.__mark_position_gap(p, aa, gapCounter)
                title = ''
                if not aa == '-':
                    if p in obj.ptmInAln:
                        c, title = obj.ptmInAln[p]
                        cls.extend(c)
                    else:
                        title = seqPos
                        if p in self.conservation:
                            aa = alnSeq[p]
                            if self.conservation[p][0] == aa:
                                cls.append('msa-con')
                            elif aa in conservedModAa.get(self.conservation[p][1], []):
                                cls.append("msa-con-sub")
                        else:
                            cls.append("msa-aa")
                obj.dvSeq.append(HTML(cls, title, aa))


    def overview(self):
        step = int(self.alnLen / 80.0 + 0.5)
        self.ov.tid = 'OV'
        self.ov.numOfSeq = len(self.order)
        self.ov.alnLen = self.alnLen
        self.ov.scale = step
        self.ov.equalSymbol = "&#8776;"
        self.ov.header = self.__draw_header_overview(step)

        for id in self.order:
            obj = self.records[id]
            alnSeq = obj.align
            ptm = obj.ptmInAln

            start = 0
            seqLen = len(alnSeq)
            while start < seqLen:
                boo = self.__find_nearest_ptm(start, start + step)
                if boo - start >= 1:
                    end = boo
                elif boo - start == 0:
                    end = boo + 1
                else:
                    end = (start + step if (start + step) <= seqLen else seqLen)

                if boo - start == 0:
                    i = boo
                    if i in ptm:
                        cls, title = ptm[i]
                        obj.ovSeq.append(HTML(cls, title, alnSeq[i]))
                    elif i in self.conservation:
                        aa = alnSeq[i]
                        if self.conservation[i][0] == aa:
                            cls = ["msa-con"]
                        elif aa in conservedModAa.get(self.conservation[i][1], []):
                            cls = ["msa-con-sub"]
                        else:
                            cls = ['msa-aa']
                        obj.ovSeq.append(HTML(cls, '', alnSeq[i]))
                elif alnSeq[start:end].seq.count('-') > 0:  # subseq = alnSeq[start,end].seq
                    obj.ovSeq.append(HTML(["msa-gap"], '', "-"))
                else:
                    obj.ovSeq.append(HTML(["msa-aa"], '', "&#9472;"))
                start = end


    def __draw_header_detailed(self):
        """Sequence legend. Ruler of detail view."""
        header = ''
        for i in range(10, self.alnLen + 1, 10):
            header += '.' * (10 - len(str(i))) + str(i)
        header += '.' * (self.alnLen - len(header))
        header = header.replace('.....', '....:')
        return list(header)


    def __draw_header_overview(self, step):
        """Sequence legend. Ruler of overview."""
        header = ''
        for label in range(step * 10, self.alnLen + 1, step * 10):
            c = self.__count_ptm_pos_with_penalty(label - step * 10, label, step)
            header += '.' * (10 - len(str(label))) + '.' * c + str(label)
        return list(header)


    def __count_ptm_pos_with_penalty(self, a, b, step, score=0):
        """Count the number of PTM sites between position a and b. 
           Penalty: if two ptms are too close (< step), add 1 penalty score. 
                    But if two ptms are consecutive, no penalty. 
           Return number."""
        last = None
        for i in range(a, b):
            if i in self.conservation:
                score += 1
                if last and i-last > 1 and i - last < step:
                    score += 1
                last = i
        return score


    def __mark_position_gap(self, idx, aa, gapCounter):
        """Judge gap or amino acid, return class,seqPos and gapCounter"""
        if aa == '-':
            gapCounter += 1
            return ['msa-gap'], 'gap', gapCounter
        else:
            pos = idx - gapCounter + 1
            return [], str(pos), gapCounter


    def __find_nearest_ptm(self, a, b):
        """Find nearest (to a) PTM site between position a and b. Return nearest position or False."""
        for i in range(a, b):
            if i in self.conservation: #
                return i
        return 0

    def __evidence(self, evidences):
        """could be avoid using better sturcture in templates.... like a pmids attribute """
        links = []
        evidences = list(set(evidences))
        if '' in evidences:
            evidences.remove('')
        if len(evidences) == 0:
            return 'NA'
        for evi in evidences:
            if evi.startswith('PMID:'):
                links.append("<a href='" + pubmed + evi[5:] + "' class='pmid' target='_blank'>" + evi[5:] + "</a>")
        if len(links) > 3:
            links[3] = "<span class='msa-pmid-show' onclick='msa_pmid_show(this)';>...</span>" + \
                       "<span class='msa-pmid-hide'>" + links[2]
            links[-1] += "</span>"
        return ", ".join(links)