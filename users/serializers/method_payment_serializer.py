
from rest_framework.serializers import ModelSerializer
from users.models import MethodPayment
from users.serializers.user_serializer import UserSerializer
class MethodPaymentSerializer(ModelSerializer):
    user=UserSerializer()
    class Meta:
        model:MethodPayment
        fields: ['title','user']