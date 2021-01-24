from rest_framework import serializers

from .models import DroneCategory
from .models import Drone
from .models import Competition
from .models import Pilot


class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'drone-detail',
    )

    class Meta:
        model = DroneCategory
        fields = (
            'url',
            'pk',
            'name',
            'drones',
        )


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugField(
        queryset=DroneCategory.objects.all(),
        slug_field='name',
    )

    class Meta:
        model = Drone
        fields = (
            'urls',
            'name',
            'drone_category',
            'has_it_competed',
            'inserted_timestamp',
        )


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer()

    class Meta:
        model = Competition
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
        choices=Pilot.GENDER_CHOICES,
    )
    gender_description = serializers.CharField(
        source = 'get_gender_display',
        read_only = True,
    )

    class Meta:
        model = Pilot
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
    pilot = serializers.SlugField(
        queryset=Pilot.objects.all(),
        slug_field='name',
    )
    drone = serializers.SlugField(
        queryset=Drone.objects.all(),
        slug_field='name',
    )

    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'pilot',
            'drone',
        )
