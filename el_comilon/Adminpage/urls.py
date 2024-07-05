from django.urls import path
from .views import inventario, borrar_item
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    #path('', include('Mainpage.urls')),
    path("inventario", inventario.as_view(), name='inventario'),
    path("inventario/eliminar/<slug:slug>", borrar_item.as_view(), name='eliminar_item')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)