from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.template import Variable, VariableDoesNotExist
import os
import json

APP_STATIC = os.path.join(os.path.dirname(__file__), '../static')
with open(os.path.join(APP_STATIC, 'external_links.json'), 'r') as f:
    l = json.load(f)

import re
register = template.Library()

def add_href(url, title, val):
    return '<a target="_blank" href="%s" title="%s">%s</a>' % (url, title, val)

@register.filter
@stringfilter
def link(full):
    debris = full.split(':')
    prefix = debris[0]
    if prefix == 'PR':
        url = reverse('webpage:entry', kwargs={'id': full})
    else:
        url = l["fullid"].get(prefix, None)
        if prefix in ['MOD', 'PSI-MOD']:
            url += full.replace(':', '_')
        elif url is not None:
            url += full
        else:
            url = l["noprefix"].get(prefix, None)
            if url is not None and len(debris[1]) > 0:
                url += debris[1]
            else:
                return full
    return mark_safe(add_href(url, '', full))


@register.filter
@stringfilter
def links(ids):
    urls = []
    for id in re.split('[|;,]\s?', ids):
        urls.append(link(id))
    return mark_safe(', '.join(urls))


@register.filter
@stringfilter
def replace(str_, args):
    arg = args.split('||')
    assert len(arg)==2
    return mark_safe(str_.replace(arg[0], arg[1]))


@register.assignment_tag()
def lookup(dict_, key_):
    try: 
        rtn = dict_[key_]
        if len(rtn) == 0:
            return None
        else:
            return rtn
    except:
        return None




# @register.filter
# def previous(value, arg):
#     try:
#         if int(arg) > 0:
#             return value[int(arg) - 1]
#         else:
#             return None
#     except:
#         return None
# 
# 
# @register.filter
# def cat_tree(value, prev):
#     if prev is not None:
#         # print value, prev[1]['category']
#         return mark_safe(cat_tree_svg(value))
# 
# 
# def cat_tree_svg(value):
#     return '<svg class="cat-tree"><path id="test" d="M 10 0 L10 20 L100 20" style="fill:none; stroke:red; stroke-width:2px;"/><text style="text-anchor:middle; font: 10px sans-serif;" dy="-8"><textPath xlink:href="#test" startOffset="75%">'+value+'</textPath></text></svg>'
