from django.db.models import fields
from rest_framework import serializers
from inventario.models import Equipo

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id','tipo','marca','modelo','cantidad')