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


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super(RoleSerializer, self).to_representation(instance)

        # Determina si la solicitud es una consulta GET
        if self.context['request'].method == 'GET':
            # Incluye las relaciones en la representación
            if instance.status is not None:
                data['status'] = StatusSerializer(instance.status).data
        return data

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super(LocationSerializer, self).to_representation(instance)

        # Determina si la solicitud es una consulta GET
        if self.context['request'].method == 'GET':
            # Incluye las relaciones en la representación
            if instance.status is not None:
                data['status'] = StatusSerializer(instance.status).data
        return data

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super(TecnicoSerializer, self).to_representation(instance)

        # Determina si la solicitud es una consulta GET
        if self.context['request'].method == 'GET':
            # Incluye las relaciones en la representación
            if instance.status is not None:
                data['status'] = StatusSerializer(instance.status).data
        return data
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super(MenuSerializer, self).to_representation(instance)

        # Determina si la solicitud es una consulta GET
        if self.context['request'].method == 'GET':
            # Incluye las relaciones en la representación
            if instance.status is not None:
                data['status'] = StatusSerializer(instance.status).data
        return data    
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

    def to_representation(self, instance):
        data = super(PermissionSerializer, self).to_representation(instance)

        # Determina si la solicitud es una consulta GET
        if self.context['request'].method == 'GET':
            # Incluye las relaciones en la representación
            if instance.menu is not None:
                data['menu'] = MenuSerializer(instance.menu, context=self.context).data
            if instance.role is not None:
                data['role'] = RoleSerializer(instance.role, context=self.context).data
        return data  
class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super(MaquinaSerializer, self).to_representation(instance)

        # Determina si la solicitud es una consulta GET
        if self.context['request'].method == 'GET':
            # Incluye las relaciones en la representación
            if instance.status is not None:
                data['status'] = StatusSerializer(instance.status).data
            if instance.location is not None:
                data['location'] = LocationSerializer(instance.location, context=self.context).data
        return data
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        depth = 1 
        
    def to_representation(self, instance):
        data = super(EventSerializer, self).to_representation(instance)
        if self.context['request'].method == 'GET':
            if instance.status is not None:
                data['status'] = StatusSerializer(instance.status).data
            if instance.tecnico is not None:
                data['tecnico'] = TecnicoSerializer(instance.tecnico, context=self.context).data
            if instance.maquina is not None:
                data['maquina'] = MaquinaSerializer(instance.maquina, context=self.context).data

           
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
            if instance.status is not None:
                data['status'] = StatusSerializer(instance.status).data
            if instance.role is not None:
                data['role'] = RoleSerializer(instance.role, context=self.context).data
            if instance.location is not None:
                data['location'] = LocationSerializer(instance.location, context=self.context).data

        return data
