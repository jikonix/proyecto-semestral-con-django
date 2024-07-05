from django.urls import path
from .views import (
    inventario, 
    borrar_item,
    editar_item
)
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    #path('', include('Mainpage.urls')),
    
]

