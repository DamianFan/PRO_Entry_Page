class PTM(object):
    """An object used to save one PTM site annotation."""

    def __init__(self):
        """
        Attributes:
        substrate -- substrate id
        enzyme -- a dict of PTM enzymes, ac: symbol
        modType -- modification abbreviation.
                    all possible values are in databases/update/updateFiles/mod.txt
        seqPos -- modified position
        aa -- one letter protein (amino acid)
              http://biopython.org/DIST/docs/api/Bio.Alphabet.IUPAC.ExtendedIUPACProtein-class.html
        source -- the source database
                  possible values: "psp","pelm","hprd"...
        note -- additional comment
                May used to distinguished HTP or LTP data
        pmid -- a list of PMIDs
        """

        self.substrate = ''
        self.enzyme = {}
        self.modType = ''
        self.seqPos = 0  # int
        self.aa = ''
        self.source = ''
        self.note = ''
        self.pmid = []



    def cls_ptm(self):
        """Return a HTML class string for one PTM. It describes enzyme, source and note."""
        cls = []
        if not len(self.enzyme) == 0:
            for e in self.enzyme:
                cls.append("msa-enzyme-" + e)
        if not self.source == '':
            cls.append("msa-source-" + self.source)
        if not self.note == '':
            cls.append("msa-note-" + self.note)
        return cls


    def __str__(self):
        str = '['
        str += "substrate: "+ self.substrate +", "
        str += "ptm enzyme: "+ self.enzyme + ", "
        str += "modification type: " + self.modType + ", "
        str += "seqence position: " + self.seqPos + ", "
        str += "amino acid: " + self.aa + ", "
        str += "source: " + self.source + ", "
        str += "note: " + self.note + ", "
        str += "pmid: "
        for p in self.pmid:
            str += p + ", "
        str += "]"
        #print(str)
        return str