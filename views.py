from rest_framework import viewsets, generics
from aeroporto.models import Aeroporto
from aeroporto.serializer import AeroportoSerializer
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import AeroportoSerializer

from .models import Aeroporto


@api_view(['GET'])
def aeroportoOverview(request):
	aeroporto_urls = {
		'Lista':'/aeroporto-list/',
		'Create':'/aeroporto-create/',
		'Update':'/aeroporto-update/<str:pk>/',
		'Delete':'/aeroporto-delete/<str:pk>/',
		}

	return Response(aeroporto_urls)

@api_view(['GET'])
def aeroportoList(request):
	aeroporto = Aeroporto.objects.all().order_by('-id')
	serializer = AeroportoSerializer(aeroporto, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def aeroportoCreate(request):
	serializer = AeroportoSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def aeroportoUpdate(request, pk):
	aeroporto = Aeroporto.objects.get(id=pk)
	serializer = AeroportoSerializer(instance=aeroporto, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def aeroporoDelete(request, pk):
	aeroporto = Aeroporto.objects.get(id=pk)
	aeroporto.delete()

	return Response('Deletado com sucesso')
