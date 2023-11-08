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
from .models.day import Day
from .models.workOrder import WorkOrder

from datetime import datetime, timedelta


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
        
    def to_representation(self, instance):
        data = super(EventSerializer, self).to_representation(instance)
        if self.context['request'].method == 'GET':
            if instance.status is not None:
                data['status'] = StatusSerializer(instance.status).data
            if instance.tecnico is not None:
                data['tecnico'] = TecnicoSerializer(instance.tecnico, context=self.context).data
            if instance.maquina is not None:
                data['maquina'] = MaquinaSerializer(instance.maquina, context=self.context).data
            if instance.day is not None:
                data['day'] = DaySerializer(instance.day, context=self.context).data
        return data
    def create(self, validated_data):
        start_date = validated_data.get('start').date()
        end_date = validated_data.get('end')
        
        end_date = datetime.combine(end_date, datetime.max.time()) - timedelta(microseconds=1)
        day, created = Day.objects.get_or_create(dayDate=start_date)
        if created:
            day.save()
            
        validated_data['end'] = end_date  # Asigna la hora de finalización ajustada
        validated_data['day'] = day
        event = Events.objects.create(**validated_data)
        return event

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
    
class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'
        
    def validate(self, data):
        dayDate = data.get('dayDate')

        if dayDate is not None:
            # Verifica si ya existe un día con la misma fecha en la base de datos
            existing_day = Day.objects.filter(dayDate=dayDate).first()
            if existing_day:
                raise serializers.ValidationError('El día ya existe')
        
        return data

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super(WorkOrderSerializer, self).to_representation(instance)

        # Determina si la solicitud es una consulta GET
        if self.context['request'].method == 'GET':
            # Incluye las relaciones en la representación
            if instance.status is not None:
                data['status'] = StatusSerializer(instance.status).data
            if instance.event is not None:
                data['event'] = EventSerializer(instance.event, context=self.context).data
            if instance.tecnico is not None:
                data['tecnico'] = TecnicoSerializer(instance.tecnico, context=self.context).data
            if instance.user is not None:
                data['user'] = UserSerializer(instance.user, context=self.context).data

        return data