
from rest_framework.serializers import ModelSerializer
from users.models import Reservation
from users.serializers.property_serializer import PropertySerializer
from users.serializers.user_serializer import UserSerializer
class ReservationSerializer(ModelSerializer):
    user=UserSerializer()
    property = PropertySerializer()
    class Meta:
        model: Reservation
        fields:['name','user','property','days','price','start_date','end_date','is_paid']