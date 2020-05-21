URL={
  'OBOEXACT':"/cgi-bin/textsearch_pro?OBO=SEL&opt_dsp_list2=PRO_NAME_TXT,PRO_DEF_TXT,CATEGORY,PARENT,MATCHED&page=1&db=",
  'PAFEXACT':"/cgi-bin/textsearch_pro?PAF=SEL&opt_dsp_list2=PRO_NAME_TXT,PRO_DEF_TXT,CATEGORY,PARENT,MATCHED&page=1&db="
}


# entry in ROOT don't retrive children node, there are too many.
ROOT=["PR:000000001","PR:000018264","GO:0043234","PR:000037070","PR:000036194", "PR:000029067"]

# entry in DELROOT are not displaying.
DELROOT = ["PR:000018263","GO:0032991","CHEBI:23367"]

# category to level dict
C2L= {'\t':1,'':1,'family':3,'gene':5,'organism-gene':6,'sequence':7,'organism-sequence':8,'modification':9,'organism-modification':10,'complex':11,'organism-complex':12}
