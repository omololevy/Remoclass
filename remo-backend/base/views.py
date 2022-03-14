from email.policy import HTTP
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .models import Unit
from .serializer import UnitSerializer

# Create your views here.

@api_view(['GET', 'POST', 'DELETE', 'UPDATE'])
def unit_list(request):
    if request.method == 'GET':
        units = Unit.objects.all()
        title = request.GET.get('title', None)

        if title is not None:
            units = units.filter(title__icontains =title)

        units_serializer = UnitSerializer(units, many = True)
        return JsonResponse(units_serializer.data, safe = False)


    elif request.method == 'POST':
        unit_data = JSONParser().parse(request)
        unit_serializer = UnitSerializer(data = unit_data)
        if unit_serializer.is_valid():
            unit_serializer.save()
            return JsonResponse(unit_serializer.data, status = status.HTTP_201_CREATED)

        return JsonResponse(unit_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        total = Unit.objects.all().delete
        return JsonResponse({'message': "{} has been removed!". 
        format(total[0])}, status = status.HTTP_204_NO_CONTENT)

