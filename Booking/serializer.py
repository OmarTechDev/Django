from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from Booking.models import Booking
from estate.models import Estate
from estate.serializer import EstateSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']

class BookingSerializer(ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    estate_id = serializers.PrimaryKeyRelatedField(queryset=Estate.objects.all())
    tenant = UserSerializer(source='tenant_id',read_only=True)
    estate = EstateSerializer(source='estate_id',read_only=True)

    class Meta:
        model= Booking
        fields= ['id','register_date','days','total_amount','start_date','end_date',
                    'is_paid','estate_id','tenant_id','tenant','estate']


    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['estate_id'] = EstateSerializer(instance.estate_id).data
    #     representation['tenant_id'] = UserSerializer(instance.tenant_id).data


























