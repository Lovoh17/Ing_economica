# archivo: economica/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='index'),
    path('conversión/', views.conversion_intereses, name='conversion_intereses'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
    path('conversion_tasas/', views.convertir_tasa, name='conversion_tasas'),

]
