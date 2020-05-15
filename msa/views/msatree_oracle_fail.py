from django.views.generic.base import TemplateView
from django.db import connection

class MsaTreeView(TemplateView):
    template_name = 'msa/tree.html'

    def get_context_data(self, query):
        context = {
            'id': query,
            'result': '['
        }
        
        cursor = connection.cursor()
        cursor.execute("""
        WITH pro_hier AS (
            SELECT hier.*, s.synonym_ as shortlabel
            FROM (
            SELECT ROWNUM as RNUM, child, Level as Lvl
            FROM MV_obo_hierarchy
            WHERE child_category LIKE 'organism%%' or child_category = 'gene'
            START WITH child = %s
            CONNECT BY PRIOR child = parent
            ) hier 
            LEFT JOIN MV_OBO_SYNONYM s ON hier.child = s.subject AND s.name = 'PRO-short-label'
        )
        SELECT
        CASE 
            WHEN Lvl = 1 THEN '{'
            /* when the last level is lower (shallower) than the current level, start a "children" array */
            WHEN Lvl - LAG(Lvl) OVER (order by rnum) = 1 THEN ',"children" : [{' 
            ELSE ',{' 
          END 
          || ' key: "' || child || '", '
          || ' title: "' || shortlabel || '", '
          || ' icon: false, '
          || ' select: true '
          
          /* when the next level lower (shallower) than the current level, close a "children" array */
          || CASE WHEN LEAD(Lvl, 1, 1) OVER (order by rnum) - Lvl <= 0 
             THEN '}' || rpad( ' ', 1+ (-2 * (LEAD(Lvl, 1, 1) OVER (order by rnum) - Lvl)), ']}' )
             ELSE NULL 
        END 
        FROM pro_hier
        ORDER BY rownum
            """, [query])
        
        context['result'] = ''.join([r[0] for r in cursor.fetchall()])
        return context