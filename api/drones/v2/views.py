import rest_framework as rf
import rest_framework.generics as rfg

import drones.views as dronesv

class ApiRootVersion2(rfg.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        rev = rf.reverse.reverse
        return rf.response.Response({
            'vehicle-categories': rev(dronesv.DroneCategoryList.name, request=request),
            'vehicles': rev(dronesv.DroneList.name, request=request),
            'pilots': rev(dronesv.PilotList.name, request=request),
            'competitions': rev(dronesv.CompetitionList.name, request=request),
        })
