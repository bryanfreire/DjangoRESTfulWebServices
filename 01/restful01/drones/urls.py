from django.urls import re_path

from .views import DroneCategoryList
from .views import DroneCategoryDetail
from .views import DroneList
from .views import DroneDetail
from .views import PilotList
from .views import PilotDetail
from .views import CompetitionList
from .views import CompetitionDetail
from .views import ApiRoot

def path(url, view):
    return re_path(url, view.as_view(), name=view.name)

urlpatterns = [
    path(r'^drone-categories/$', DroneCategoryList),
    path(r'^drone-categories/(?P<pk>[0-9]+)$', DroneCategoryDetail),
    path(r'^drones/$', DroneList),
    path(r'^drones/(?P<pk>[0-9]+)$', DroneDetail),
    path(r'^pilots/$', PilotList),
    path(r'^pilots/(?P<pk>[0-9]+)$', PilotDetail),
    path(r'^competitions/$', CompetitionList),
    path(r'^competitions/(?P<pk>[0-9]+)$', CompetitionDetail),
    path(r'^$', ApiRoot)
]
