from django.contrib.auth import models as authmodels

from rest_framework import serializers
from . import  models


class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Drone
        fields = (
            'url',
            'name',
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = authmodels.User
        fields = (
            'url',
            'pk',
            'username',
            'drone',
        )


class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'drone-detail',
    )

    class Meta:
        model = models.DroneCategory
        fields = (
            'url',
            'pk',
            'name',
            'drones',
        )


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(
        queryset=models.DroneCategory.objects.all(),
        slug_field='name',
    )
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Drone
        fields = (
            'url',
            'name',
            'drone_category',
            'manufacturing_date',
            'has_it_competed',
            'inserted_timestamp',
        )


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer()

    class Meta:
        model = models.Competition
        fields = (
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'drone',
        )



class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(
        choices=models.Pilot.GENDER_CHOICES,
    )
    gender_description = serializers.CharField(
        source = 'get_gender_display',
        read_only = True,
    )

    class Meta:
        model = models.Pilot
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'races_count',
            'inserted_timestamp',
            'competitions',
        )


class PilotCompetitionSerializer(serializers.ModelSerializer):
    pilot = serializers.SlugRelatedField(
        queryset=models.Pilot.objects.all(),
        slug_field='name',
    )
    drone = serializers.SlugRelatedField(
        queryset=models.Drone.objects.all(),
        slug_field='name',
    )

    class Meta:
        model = models.Competition
        fields = (
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'pilot',
            'drone',
        )
