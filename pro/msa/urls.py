from django.conf.urls import include, url
from .views import *
from .msatree import *
from .msahome import *

urlpatterns = [
    url(r'^$', MsaHomeView.as_view(), name='home'),
    url(r'^view/(?P<mod>[\w-]+)/(?P<query>[\w:\-\,]+)/$',loadingMSA, name='view'),
    url(r'^data/(?P<mod>[\w-]+)/(?P<query>[\w:\-\,]+)/$',MsaView, name='data'),
    url(r'^tree/(?P<query>[\w:\-]+)/$', MsaTreeView.as_view(), name='tree'),
    url(r'^test/$', test, name='msatest'),
]