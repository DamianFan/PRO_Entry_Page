from django.conf.urls import include, url
from .views import *
from .entry import view_hierarchy

urlpatterns = [
    url(r'^process/$', process, name='process'),
    url(r'^test/$', test, name='test'),
    url(r'^entry/(?P<proId>.+)/$', entry, name='entry'),
    url(r'^obo/(?P<proId>.+)/$', obo, name='obo'),
    url(r'^idtree/(?P<proId>.+)$', view_hierarchy, name='hierarchy'),
    url(r'^nametree/(?P<proId>.+)$', view_hierarchy_name, name='hierarchyname'),

]

