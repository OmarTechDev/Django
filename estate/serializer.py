from rest_framework.serializers import ModelSerializer
from users.models import User
from estate.models import Estate

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']

class EstateSerializer(ModelSerializer):
    owner_id = UserSerializer(read_only=True)
    class Meta:
        model = Estate
        fields= ['id','name','rooms','bathrooms','floors','price','is_available','owner_id']

    def create(self, validated_data):
        validated_data.pop('is_available', None)  # Esto asegura que se use el valor por defecto
        estate = Estate.objects.create(**validated_data)
        return estate