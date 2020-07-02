from django.shortcuts import render , redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
import requests
from .models import Banks,Branches
from .serializers import BanksSerializer,BranchesSerializer

@api_view(['POST'])
def get_from_ifsc(request):
    req_ifsc = (request.data.get("ifsc"))
    branch = list(Branches.objects.filter(ifsc = req_ifsc).values())[0]
    serializer = BranchesSerializer(data = branch)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def get_from_name_city(request):
    params = request.data
    bank = params.get("bank")
    city = params.get("city")
    bank_id = (Banks.objects.get(name = bank)).id
    branches = list(Branches.objects.filter(city = city, bank_id = bank_id).values())
    serializer = BranchesSerializer(data = branches,many = True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def index (request):
    urlpatterns = [
    "path('',views.index,name = 'index')" ,
    "path('IFSC/', views.get_from_ifsc , name = 'GetFromIFSC')" ,
    "path('Filter/', views.get_from_name_city , name = 'GetFromBankAndCity')" ,
    ]
    return Response(urlpatterns)
