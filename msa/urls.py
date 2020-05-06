from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^view/(?P<mod>[\w-]+)/(?P<query>[\w:\-\,]+)/$',loadingMSA, name='view'),
    url(r'^data/(?P<mod>[\w-]+)/(?P<query>[\w:\-\,]+)/$',MsaView, name='data'),
    url(r'^test/$', test, name='msatest'),
]