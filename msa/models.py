from django.db import models

# Create your models here.
class MvMapping(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    object = models.CharField(max_length=604)
    predicate = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'mv_mapping'


class MvOboComment(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    category = models.CharField(max_length=440, blank=True)
    is_automatic = models.CharField(max_length=15, blank=True)
    enzyme = models.CharField(max_length=4000, blank=True)
    comment_field = models.CharField(db_column='comment_', max_length=4000,
                                     blank=True)  # Field renamed because it ended with '_'.
    requester = models.CharField(max_length=456, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_comment'


class MvOboDef(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    definition = models.CharField(max_length=4000, blank=True)
    evidence = models.CharField(max_length=4000, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_def'


class MvOboEnzyme(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    type = models.CharField(max_length=400)
    obo_dbxref_description = models.CharField(max_length=4000, blank=True)
    aggkey = models.CharField(max_length=604, blank=True)
    abbrev3 = models.CharField(max_length=12, blank=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_enzyme'


class MvOboEnzymeCompress(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    type = models.CharField(max_length=400)
    objectname = models.CharField(max_length=4000, blank=True)
    objectid = models.CharField(max_length=4000, blank=True)
    position = models.CharField(max_length=4000, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_enzyme_compress'


class MvOboHierarchy(models.Model):
    child = models.CharField(primary_key=True, max_length=604)
    child_category = models.CharField(max_length=400, blank=True)
    child_name = models.CharField(max_length=4000, blank=True)
    predicate = models.CharField(max_length=15, blank=True)
    parent = models.CharField( max_length=604)
    parent_category = models.CharField(max_length=400, blank=True)
    parent_name = models.CharField(max_length=4000, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_hierarchy'


class MvOboIntersectionOf(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    predicate = models.CharField(max_length=604)
    object = models.CharField(max_length=604)
    name = models.CharField(max_length=4000, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_intersection_of'


class MvOboModResidue(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    abbrev3 = models.CharField(max_length=12, blank=True)
    position = models.IntegerField(blank=True, null=True)
    mod_id = models.CharField(max_length=604, blank=True)

    # class Meta:
    #     managed = False
    #     db_table = 'mv_obo_mod_residue'


class MvOboModResidueCompress(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    residue = models.CharField(max_length=4000, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_mod_residue_compress'


class MvOboProteinRegion(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    low = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_protein_region'


class MvOboProteinRegionCompress(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    region = models.CharField(max_length=4000, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_protein_region_compress'


class MvOboRelationship(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    predicate = models.CharField(max_length=604)
    object = models.CharField(max_length=604)
    name = models.CharField(max_length=4000, blank=True)
    modname = models.CharField(max_length=4000, blank=True)
    modvalue = models.CharField(max_length=400, blank=True)
    obo_dbxref_description = models.CharField(max_length=4000, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_relationship'


class MvOboRelationshipMore(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    predicate = models.CharField(max_length=604)
    object = models.CharField(max_length=604)
    name = models.CharField(max_length=4000, blank=True)
    modname = models.CharField(max_length=4000, blank=True)
    modvalue = models.CharField(max_length=400, blank=True)
    obo_dbxref_description = models.CharField(max_length=4000, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_relationship_more'


class MvOboSynonym(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    synonym_field = models.CharField(db_column='synonym_', max_length=4000,
                                     blank=True)  # Field renamed because it ended with '_'.
    type = models.CharField(max_length=4000)
    name = models.CharField(max_length=4000, blank=True)
    curator = models.CharField(max_length=4000, blank=True)
    obo_dbxref_description = models.CharField(max_length=4000, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_synonym'


class MvOboTerm(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    refsub = models.CharField(max_length=604, blank=True)
    refshsub = models.CharField(max_length=604, blank=True)
    name = models.CharField(max_length=4000)
    namespace = models.CharField(max_length=200)
    category = models.CharField(max_length=400, blank=True)
    definition = models.CharField(max_length=4000, blank=True)
    obsolete = models.IntegerField()
    comment_field = models.CharField(db_column='comment_', max_length=4000,
                                     blank=True)  # Field renamed because it ended with '_'.
    is_automatic = models.IntegerField(blank=True, null=True)
    is_anonymous = models.IntegerField(blank=True, null=True)
    is_uncommitted = models.IntegerField(blank=True, null=True)
    requester = models.CharField(max_length=400, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_term'


class MvPaf(models.Model):
    paf_row_num = models.CharField(primary_key=True, max_length=604)
    pro_id = models.CharField(max_length=604, blank=True)
    object_term = models.CharField(max_length=4000)
    object_syn = models.CharField(max_length=4000, blank=True)
    modifier = models.CharField(max_length=4000, blank=True)
    relation = models.CharField(max_length=400)
    ontology_id = models.CharField(max_length=604, blank=True)
    ontology_term = models.CharField(max_length=1020, blank=True)
    relative_to = models.CharField(max_length=4000, blank=True)
    interaction_with = models.CharField(max_length=4000, blank=True)
    evidence_source = models.CharField(max_length=4000, blank=True)
    evidence_code = models.CharField(max_length=4000, blank=True)
    taxon = models.CharField(max_length=4000, blank=True)
    inferred_from = models.CharField(max_length=4000, blank=True)
    db_id = models.CharField(max_length=4000, blank=True)
    protein_region = models.CharField(max_length=4000, blank=True)
    residue = models.CharField(max_length=4000, blank=True)
    date_field = models.DateField(db_column='date_', blank=True, null=True)  # Field renamed because it ended with '_'.
    assigned_by = models.CharField(max_length=604, blank=True)
    comment_field = models.CharField(db_column='comment_', max_length=4000,
                                     blank=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'mv_paf'


class MvOboUniprotXref(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    object = models.CharField(max_length=604, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_obo_uniprot_xref'


class MvTaxonomy(models.Model):
    subject = models.CharField(primary_key=True, max_length=151)
    taxonomy = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'mv_taxonomy'


class MvWebsite(models.Model):
    subject = models.CharField(primary_key=True, max_length=604)
    name = models.CharField(max_length=4000)
    category = models.CharField(max_length=400, blank=True)
    definition = models.CharField(max_length=4000, blank=True)
    evidence = models.CharField(max_length=4000, blank=True)
    comment_field = models.TextField(db_column='comment_', blank=True)  # Field renamed because it ended with '_'.
    sites = models.CharField(max_length=4000, blank=True)
    short_label = models.CharField(max_length=4000, blank=True)
    complex_count = models.FloatField(blank=True, null=True)
    paf_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mv_website'


class Sequence(models.Model):
    subject = models.CharField(primary_key=True, max_length=25)
    sequence = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'sequence'
