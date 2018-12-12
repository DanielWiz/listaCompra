from .models import Lista,Producto,Tienda,User
from rest_framework import serializers
from django.db.models import CharField
from django.contrib.auth import authenticate

class ProductoSerializer( serializers.HyperlinkedModelSerializer ):
    Tienda = serializers.CharField( source='Tienda.Nombre', read_only=True)

    class Meta:
        model = Producto
        fields = ('NombreProducto','CostoReal','Tienda','Notas','Estado','Lista')

class ListaSerializer( serializers.HyperlinkedModelSerializer ):
    Producto = serializers.CharField( source='Producto.NombreProducto', read_only=True)

    class Meta:
        model = Lista
        fields = ('NombreLista','Estado','Producto')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")

