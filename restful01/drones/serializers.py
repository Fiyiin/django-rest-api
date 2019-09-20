from rest_framework import serailizers
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Competition
from drones.models import Pilot
import drones.views


class DroneCategorySerializer(serailizers.HyperlinkedModelSerializer):
    drones = serailizers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name='drone-detail'
    )

    class Meta:
        model = DroneCategory
        fields = (
            'url',
            'pk',
            'name',
            'drones'
        )


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serailizers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field='name')
    class Meta:
        model = Drone
        fields = (
            'url',
            'name',
            'drone_categoty',
            'manufacturing_date',
            'has_it_competed',
            'inserted_timestamp'
        )