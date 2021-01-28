from django.urls import re_path
from . import views


app_name = 'drones2'

def path(url, view):
    return re_path(url, view.as_view(), name=view.name)

urlpatterns = [
    path(r'^drone-categories/$', views.DroneCategoryList),
    path(r'^drone-categories/(?P<pk>[0-9]+)$', views.DroneCategoryDetail),
    path(r'^drones/$', views.DroneList),
    path(r'^drones/(?P<pk>[0-9]+)$', views.DroneDetail),
    path(r'^pilots/$', views.PilotList),
    path(r'^pilots/(?P<pk>[0-9]+)$', views.PilotDetail),
    path(r'^competitions/$', views.CompetitionList),
    path(r'^competitions/(?P<pk>[0-9]+)$', views.CompetitionDetail),
    path(r'^$', views.ApiRoot)
]
