from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404

from inventario.models import Equipo
from inventario.serializers import InventarioSerializer

class ApiOverview(APIView):
    def get(self, request):
        api_urls = {
            'todos los objetos': '/',
            'buscar por tipo': '/?category=category_name',
            'buscar por marca': '/?subcategory=category_name',
            'Add': '/create',
            'Update': '/update/pk',
            'Delete': '/item/pk/delete'
        }
        return Response(api_urls)

class AddItems(APIView):
    def post(self, request):
        item = InventarioSerializer(data=request.data)
        if Equipo.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')
        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ViewItems(APIView):
    def get(self, request):
        if request.query_params:
            items = Equipo.objects.filter(**request.query_params.dict())
        else:
            items = Equipo.objects.all()
        if items:
            serializer = InventarioSerializer(items, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UpdateItems(APIView):
    def patch(self, request, pk):
        item = Equipo.objects.get(pk=pk)
        data = InventarioSerializer(instance=item, data=request.data, partial=True)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteItems(APIView):
    def delete(self, request, pk):
        item = get_object_or_404(Equipo, pk=pk)
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)