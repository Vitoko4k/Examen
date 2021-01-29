"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appproyecto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingresar_moto/',views.ingresar_moto),
    path('ingreso_moto/',views.ingreso_moto),
    path('eliminar_moto/',views.eliminar_moto),
    path('eliminacion_motocicleta/',views.eliminacion_motocicleta),
    path('modificar_moto/',views.modificar_moto),
    path('modificar/',views.modificar),
    path('listar_moto/',views.listar_moto),
    path('lista_motocicleta/',views.lista_motocicleta),
    path('categorias/',views.categorias),
    path('cotizar/',views.cotizar),
    path('GaleriaDeImagenes/',views.GaleriaDeImagenes),
    path('index/',views.index),
    path('QuienesSomos/',views.QuienesSomos),

]
