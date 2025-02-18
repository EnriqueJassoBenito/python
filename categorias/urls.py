from django.urls import path
from .views import *

urlpatterns = [
    path('agregar/', agregar_categoria, name='agregar'),
    path('ver/', ver_categoria, name='ver'),
    path('', index, name='home'),
    path('api/get/', lista_categoria, name='lista'),
]