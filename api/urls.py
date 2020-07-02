from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('IFSC/', views.get_from_ifsc , name = "GetFromIFSC"),
    path('Filter/', views.get_from_name_city , name = "GetFromBankAndCity"),
]