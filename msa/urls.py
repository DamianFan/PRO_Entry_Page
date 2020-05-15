from django.conf.urls import url
from msa.views import *

urlpatterns = [
   url(r'^$', MsaHomeView.as_view(), name='home'),
   url(r'^tree/(?P<query>[\w:\-]+)/$', MsaTreeView.as_view(), name='tree'),
   url(r'^data/(?P<mod>[\w-]+)/(?P<query>[\w:\-\,]+)/$', MsaView, name='data'),
   url(r'^view/(?P<mod>[\w-]+)/(?P<query>[\w:\-\,]+)/$', loadingMSA, name='view'),
]
