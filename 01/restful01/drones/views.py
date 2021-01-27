from rest_framework import generics
from rest_framework import permissions as rfpermisions
from rest_framework.response import Response
from rest_framework.reverse import reverse

import django_filters as filters

from . import models
from . import serializers
from . import permissions

class DroneCategoryList(generics.ListCreateAPIView):
    queryset = models.DroneCategory.objects.all()
    serializer_class = serializers.DroneCategorySerializer
    name = 'dronecategory-list'
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DroneCategory.objects.all()
    serializer_class = serializers.DroneCategorySerializer
    name = 'dronecategory-detail'


class DroneList(generics.ListCreateAPIView):
    queryset = models.Drone.objects.all()
    serializer_class = serializers.DroneSerializer
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
    permission_classes = (
        rfpermisions.IsAuthenticatedOrReadOnly,
        permissions.IsCurrentUserOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Drone.objects.all()
    serializer_class = serializers.DroneSerializer
    name = 'drone-detail'
    permission_classes = (
        rfpermisions.IsAuthenticatedOrReadOnly,
        permissions.IsCurrentUserOwnerOrReadOnly,
    )


class PilotList(generics.ListCreateAPIView):
    queryset = models.Pilot.objects.all()
    serializer_class = serializers.PilotSerializer
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
    queryset = models.Pilot.objects.all()
    serializer_class = serializers.PilotSerializer
    name = 'pilot-detail'


class CompetitionFilter(filters.FilterSet):
    from_achievement_date = filters.DateTimeFilter(
        field_name = 'distance_achievement_date',
        lookup_expr='gte',
    )
    to_achievement_date = filters.DateTimeFilter(
        field_name = 'distance_achievement_date',
        lookup_expr='lte',
    )
    min_distance_in_feet = filters.NumberFilter(
        field_name = 'distance_in_feet',
        lookup_expr = 'gte'
    )
    max_distance_in_feet = filters.NumberFilter(
        field_name = 'distance_in_feet',
        lookup_expr = 'lte'
    )
    drone_name = filters.AllValuesFilter(field_name = 'drone__name')
    pilot_name = filters.AllValuesFilter(field_name = 'pilot__name')

    class Meta:
        model = models.Competition
        fields = (
            'distance_in_feet',
        )


class CompetitionList(generics.ListCreateAPIView):
    queryset = models.Competition.objects.all()
    serializer_class = serializers.PilotCompetitionSerializer
    name = 'competition'
    filter_class = CompetitionFilter
    ordering_fields = (
        'distance_in_feet',
        'distance_achievement_date',
    )


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Competition.objects.all()
    serializer_class = serializers.PilotCompetitionSerializer
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
