import django.conf.urls as dju
import drones.views as dronesv
import drones.v2.views as drones2v


app_name = 'drones2'

def path(url, view):
    return dju.re_path(url, view.as_view(), name=view.name)

urlpatterns = [
    path(r'^vehicle-categories/$', dronesv.DroneCategoryList),
    path(r'^vehicle-categories/(?P<pk>[0-9]+)$', dronesv.DroneCategoryDetail),
    path(r'^vehicles/$', dronesv.DroneList),
    path(r'^vehicles/(?P<pk>[0-9]+)$', dronesv.DroneDetail),
    path(r'^pilots/$', dronesv.PilotList),
    path(r'^pilots/(?P<pk>[0-9]+)$', dronesv.PilotDetail),
    path(r'^competitions/$', dronesv.CompetitionList),
    path(r'^competitions/(?P<pk>[0-9]+)$', dronesv.CompetitionDetail),
    path(r'^$', drones2v.ApiRootVersion2),
]
