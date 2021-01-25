from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django_filters import (
    FilterSet,
    AllValuesFilter,
    DateTimeFilter,
    NumberFilter,
)

from .models import DroneCategory
from .models import Drone
from .models import Pilot
from .models import Competition

from .serializers import DroneCategorySerializer
from .serializers import DroneSerializer
from .serializers import PilotSerializer
from .serializers import PilotCompetitionSerializer


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-detail'


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'
    filter_fields = (
        'name',
        'drone_category',
        'manufacturing_date',
        'has_it_competed',
    )
    search_fields = ('^name',)
    ordering_fields = (
        'name',
        'manufacturing_date',
    )


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'


class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-list'
    fielter_fields = (
        'name',
        'gender',
        'races_count',
    )
    search_fields = ('^name',)
    ordering_fields = (
        'name',
        'races_count',
    )


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'


class CompetitionFilter(FilterSet):
    from_achievement_date = DateTimeFilter(
        field_name = 'distance_achievement_date',
        lookup_expr='gte',
    )
    to_achievement_date = DateTimeFilter(
        field_name = 'distance_achievement_date',
        lookup_expr='lte',
    )
    min_distance_in_feet = NumberFilter(
        field_name = 'distance_in_feet',
        lookup_expr = 'gte'
    )
    max_distance_in_feet = NumberFilter(
        field_name = 'distance_in_feet',
        lookup_expr = 'lte'
    )
    drone_name = AllValuesFilter(field_name = 'drone__name')
    pilot_name = AllValuesFilter(field_name = 'pilot__name')

    class Meta:
        model = Competition
        fields = (
            'distance_in_feet',
        )


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition'
    filter_class = CompetitionFilter
    ordering_fields = (
        'distance_in_feet',
        'distance_achievement_date',
    )


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args):
        return Response({
            'drone-categories': reverse(DroneCategoryList.name, request=request),
            'drones': reverse(DroneList.name, request=request),
            'pilots': reverse(PilotList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request),
        })
