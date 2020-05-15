# import os
# import pickle
# import sys
# 
# sys.path.append('/var/www/django/iptmnet_website/')
# # sys.path.append('/homes/annotation/htdocs/text_mining/iptmnet/django/iptmnet_website/')
# 
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iptmnet_website.settings")
# 
# from django.conf import settings
# db = settings.DATABASES['default']
# 
# import django
# django.setup()
# 
# from iptmnet.models.materialized_views import *
# from entry import *
# from collect import *
# 
# 
# for e in MvEntry.objects.filter(iptm_entry_type="uniprot_ac").only("iptm_entry_code").order_by("iptm_entry_code"):
#     id = e.iptm_entry_code
#     print id
#     file = os.path.join(os.path.dirname(__file__), '../preprocess', id+'.p')
#     obj = ENTRY(id).initial()
#     all = merge_with_pro(obj, 'msa-request')
#     with open(file, 'wb') as pf:
#         pickle.dump(all, pf)