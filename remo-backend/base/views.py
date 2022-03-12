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

    
