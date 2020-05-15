from django.db.models import Q
#from pro.models import *
from django.shortcuts import get_object_or_404
from django.db import connection
import urllib
from itertools import chain


# def get_direct_parent(id):
#     return get_object_or_404(MvOboHierarchy, child=id).parent
#
#
# def get_taxon(id):
#     taxon = MvTaxonomy.objects.filter(subject=id)
#     return taxon[0].taxonomy if taxon else None
#
#
# def get_children(id, sameTaxon, taxon):
#     """if sameTaxon is True, get entry(id)'s taxon first"""
#     # taxon = taxon if sameTaxon else '%%'
#     query = """
#         SELECT hier.child
#         FROM
#         (
#         SELECT CHILD, CHILD_CATEGORY
#         FROM MV_obo_hierarchy
#         WHERE child != '%s'
#         START WITH child = '%s'
#         CONNECT BY PRIOR child = parent
#         ) hier
#         """ % (id, id)
#
#     if sameTaxon:
#         query += """JOIN MV_taxonomy t ON hier.child = t.subject AND t.taxonomy = '%s' """ %(taxon)
#
#     query += """ORDER BY hier.child ASC"""
#
#     # cursor = connection.cursor()
#     # cursor.execute(query)
#     # return [r[0] for r in cursor.fetchall()]
#     return None
#
#
# def get_terms(ids):
#     return MvOboTerm.objects.filter(subject__in=ids).only('subject', 'name', 'definition', 'category')
#

# def get_short_label(ids):
#     return MvOboSynonym.objects.filter(Q(subject__in=ids) & Q(name='PRO-short-label')).only('subject', 'synonym_field')


# def get_sites(ids):
#     return MvOboModResidueCompress.objects.filter(subject__in=ids)


# def get_xrefs(ids):
#     x1 = MvOboRelationship.objects.filter(
#         Q(subject__in=ids) & Q(predicate='term_xref') & Q(object__startswith='UniProtKB'))
#     x2 = MvOboUniprotXref.objects.filter(subject__in=ids)
#     return list(chain(x1, x2))


# def get_enzymes(ids):
#     return MvOboEnzyme.objects.filter(subject__in=ids)


# def get_mod_residues(ids):
#     return MvOboModResidue.objects.filter(subject__in=ids)


# def get_def_xref(ids):
#     return MvOboRelationship.objects.filter(Q(subject__in=ids) & Q(predicate='def_xref')).only('subject', 'object')


# def get_seqs(ids):
#     return Sequence.objects.filter(subject__in=ids)


# def get_seq_external(id):
#     raw = (urllib.urlopen('http://www.uniprot.org/uniprot/' + id + '.fasta')).readlines()
#     seq = ''.join(raw[1:]).replace('\n', '')
#     return seq