from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Visita, Mensaje


class VisitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visita
        fields = ["url", "nombre_visitante", "empresa_procedencia", "rut", "fecha_ingreso", "fecha_salida", "motivo"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = ['id', 'contenido', 'fecha']


class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = ['id', 'autor', 'texto', 'fecha']