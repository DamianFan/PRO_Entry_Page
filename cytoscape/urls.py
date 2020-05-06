from django.conf.urls import include, url
from .views import *

urlpatterns = [
   url(r'view/(?P<ids>.+)?$', sparql_cyto_view, name='pro'),
   url('download', download_xgmml, name="download_xgmml"),
]