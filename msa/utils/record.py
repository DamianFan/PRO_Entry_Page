from collections import defaultdict

class RECORD(object):
    """Define RECORD object for MSA view."""

    def __init__(self):
        """
        seqRecord
        align -- align result
        enzymes -- list of all enzyme ac(code)
        ptmInAln --  store class and title
        dvSeq -- a list of HTML object containing all sequences (align) for detail view
        ovSeq -- a list of HTML object containing all sequences (align) for overview
        """

        self.seqRecord = ''
        self.align = ''
        self.enzymes = []
        self.ptmInAln = defaultdict(dict)
        self.dvSeq = []
        self.ovSeq = []

    def __str__(self):
        str = "["
        str += self.seqRecord +', '
        str += self.align +"] "

class HTML(object):
    def __init__(self, cls, title, content):
        self.cls = [c.replace(':','_') for c in cls]
        self.title = title
        self.content = content.replace('-','&nbsp;')