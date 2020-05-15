from django.views.generic.base import TemplateView
from msa.utils.collect import *
from msa.utils.entry import *
from msa.utils.dao import DAO

class MsaTreeView(TemplateView):
    template_name = 'msa/tree.html'

    def get_context_data(self, query):
        """
        :param query:  should be a gene level term
        :return:
        """
        context = {
            'id': query,
            'result': ''
        }
        
        context['result'] = '[%s]' % (self.make_tree(query))
        return context


    def make_tree(self, parent):
        # root
        dao = DAO(parent)
        parentObj = ENTRY.batch_initial(dao, [parent], full=False)[0]
        tree = self.start(parentObj, 'unselectable:true, ')

        # leaves
        formObjs = proteoforms(dao, parent, sameTaxon=False, taxon=None, full=False)
        
        orthos, isos, ptms = [], [], []
        for f in formObjs:
            if f.Cat == 'organism-gene':
                orthos.append(f)
            elif f.Cat == 'organism-sequence':
                isos.append(f)
            elif f.Cat == 'organism-modification':
                ptms.append(f)
                
        orthos = sorted(orthos, key=lambda x:x.name)
        isos = sorted(isos, key=lambda x:x.name)
        ptms = sorted(ptms, key=lambda x:x.name)
                
        for ortho in orthos:
            tree += self.start(ortho, '')
            
            for iso in isos:
                # [u'UniProtKB:Q62432-2'] [u'UniProtKB:Q15796']
                if iso.dbxrefs[0].startswith(ortho.dbxrefs[0]):
                    tree += self.start(iso, '')  # unselectable:true, 
                    
                    for ptm in ptms[:]:
                        if ptm.dbxrefs[0] in iso.dbxrefs:
                            tree += self.start(ptm, '')
                            tree += self.end() # ptm
                            ptms.remove(ptm)
                            
                    tree += self.end() # iso
                    
            tree += self.end()   # ortho
        else:
            for ptm in ptms[:]:
                tree += self.start(ptm,'')
                tree += self.end()
                
        tree += self.end() #root
        return tree


    def start(self, obj, attr):
        return '{title: "%s", key: "%s", icon:false, select:true, %s children: [' % (
            obj.name, obj.id, attr)

    def end(self):
        return ']},'