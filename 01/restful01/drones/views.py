from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import DroneCategory
from .models import Drone
from .models import Pilot
from .models import Competition

from .serializers import DroneCategorySerializer
from .serializers import DroneSerializer
from .serializers import PilotSerializer
from .serializers import PilotCompetitionSerializer


class DroneCategoryList(ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'


class DroneCategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-detail'


class DroneList(ListCreateAPIView):
    queryset = Dronte.objects.all()
    serializer_class = DronteSerializer
    name = 'drone-list'


class DroneDetail(RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'


class PilotList(ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-list'


class PilotDetail(RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'


class CompetitionList(ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition'


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args):
        return Response({
            'drone-categories': reverse(DroneCategoryList.name, request=request)
            'drones': reverse(DroneList.name, request=request)
            'pilots': reverse(PilotList.name, request=request)
            'competitions': reverse(CompetitionList.name, request=request)
        })
