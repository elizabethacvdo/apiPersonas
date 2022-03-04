from dataclasses import fields
from rest_framework import serializers
from personaApp.models import persona


class PersonaSerializer(serializers.ModelSerializer):


    class Meta:
        model = persona
        fields = ('nombre','apellido','dui','direccion','telefono')