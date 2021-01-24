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
    path(r'^drone-categories/(?P<pk>[0-9]+)$', DroneCategoryList),
    path(r'^drones/$', DroneCategoryList),
    path(r'^drones/(?P<pk>[0-9]+)$', DroneCategoryList),
    path(r'^pilots/$', DroneCategoryList),
    path(r'^pilots/(?P<pk>[0-9]+)$', DroneCategoryList),
    path(r'^competitions/$', DroneCategoryList),
    path(r'^competitions/(?P<pk>[0-9]+)$', DroneCategoryList),
    path(r'^$', ApiRoot)
]
