from rest_framework import serializers
from .models.role import Role
from .models.status import Status
from .models.location import Location
from .models.tecnico import Tecnico
from .models.menu import Menu
from .models.permission import Permission
from .models.events import Events
from .models.maquina import Maquina
from .models.user import User
from django.contrib.auth.hashers import make_password


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        
class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super(MaquinaSerializer, self).to_representation(instance)

        # Determina si la solicitud es una consulta GET
        if self.context['request'].method == 'GET':
            # Incluye las relaciones en la representación
            data['status'] = StatusSerializer(instance.status).data
            data['location'] = LocationSerializer(instance.location).data

        return data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)

        # Determina si la solicitud es una consulta GET
        if self.context['request'].method == 'GET':
            # Incluye las relaciones en la representación
            data['status'] = StatusSerializer(instance.status).data
            data['role'] = RoleSerializer(instance.role).data
            data['location'] = LocationSerializer(instance.location).data

        return data
