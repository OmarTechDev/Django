from rest_framework.serializers import ModelSerializer
from users.models import User
from estate.models import Estate
from rest_framework import serializers
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']

class EstateSerializer(ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    class Meta:
        model = Estate
        fields= ['id','name','rooms','bathrooms','floors','price','is_available','owner_id']

    def create(self, validated_data):
        validated_data.pop('is_available', None)  # Esto asegura que se use el valor por defecto
        estate = Estate.objects.create(**validated_data)
        return estate

    def to_representation(self, instance):
        # Sobreescribe el método `to_representation` para incluir la información del `User` en el `owner_id`
        representation = super().to_representation(instance)
        # Serializa el objeto `User` en lugar de solo su ID
        representation['owner_id'] = UserSerializer(instance.owner_id).data
        return representation