import database.root_setting as g

class NODE(object):
    """Define Cytsocape node object."""

    def __init__(self, data,rel):
        # print('this data and rel in NODE,', data, rel)
        """
        Attributes:
        data -- a list contains PROTerm data
                0 id  1 Name  2 Def  3 Category  4 Label  5 Sites  6 Mapping  7 Shape  8 ptm 9	evidence
        Level -- an integer transfer from entry's Category.
                  Default is 0, others define in setting.py, C2L dict.
        Group -- a string keeps entry position in hierarchy structure.
                  Possible values are: parent, sibling, child, request,
                                       addition, annotation,related(upro)
        rel -- a list contains PROHierarchy relations
                0 parents  1 children  2 complex  3 component  4 sibling
        """
        self.data = data
        self.Level = g.C2L.get(self.data[3], 0)
        self.Group = ''
        self.rel = rel

    def opt_cwdisplay(self, label):
        """
        Optimize cytoscape label dipslaying.
        Cutting long label into multi-line.
        """
        if label.find('/') >= 0 and label.find(':') >= 0: return label
        debris = label.split(' ')
        s, c = '', 0
        for d in debris:
            if len(d) <= 3:
                s, c = s + ' ' + d, c + len(d)
            elif len(d) >= 14:
                s, c = s + '\\n' + d, len(d)
            else:
                if c + len(d) < 19:
                    s, c = s + ' ' + d, c + len(d)
                else:
                    s, c = s + '\\n' + d, len(d)
        if s.startswith('\\n'):
            return s[2:]
        elif s.startswith(' '):
            return s[1:]
        else:
            return s

    def json(self):
        """Cytoscape Web Node"""
        if self.data[5] != '':
            label = self.data[4] + "\\n(" + self.data[5] + ")"
        else:
            label = self.data[4]
        return '{id: "' + self.data[0] + '", ID: "' + self.data[0] + '", Name: "' + self.data[1] + '", Def: "' + \
               self.data[2] + '", Category: "' + self.data[3] + '", Level: "' + str(
            self.Level) + '", Label: "' + self.opt_cwdisplay(label) + '", Mapping: "' + self.data[6] + '", Shape: "' + \
               self.data[7] + '", ptm: "' + self.data[8] + '", Group: "' + self.Group + '"},'

    def jsjson(self):
        """Cytoscape.js Node"""
        if self.data[5] != '':
            label = self.data[4] + "\\n(" + self.data[5] + ")"
        else:
            label = self.data[4]
        if self.data[1] == '':
            # label = get_symbol(self.data[0])
            label = ''
        # return ''
        return '{data: {id: "' + self.data[0] + '", ID: "' + self.data[0] + '", Name: "' + self.data[1] + '", Def: "' + \
               self.data[2] + '", Category: "' + self.data[3] + '", Level: "' + str(
            self.Level) + '", Label: "' + self.opt_cwdisplay(label) + '", Mapping: "' + self.data[6] + '", Shape: "' + \
               self.data[7] + '", ptm: "' + self.data[8] + '", Group: "' + self.Group + '"}},'
