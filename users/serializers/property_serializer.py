from rest_framework.serializers import ModelSerializer
from users.models import Property
from users.serializers.user_serializer import UserSerializer
class PropertySerializer(ModelSerializer):
    owner = UserSerializer() 
    class Meta:
        model: Property
        fields: ['title','owner']