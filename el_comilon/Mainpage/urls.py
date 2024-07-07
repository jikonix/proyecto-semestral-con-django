from django.urls import path
from .views import (
    mainpage,
    ver_carro,
    agregar_al_carro,
    borrar_item_carro

)
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    #path('', include('Mainpage.urls')),
    path('', mainpage.as_view(), name='mainpage'),
    path('agregar_al_carro/<pk>', agregar_al_carro.as_view(), name='añadir al carro'),
    path('ver_carro/<pk>', ver_carro.as_view(), name='carro'),
    path('ver_carro/borar_item/<int:pk>', borrar_item_carro.as_view(), name='borrar_item_carro'),
    
]

