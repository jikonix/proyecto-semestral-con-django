from django.urls import path
from .views import homepage
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('', homepage.as_view(), name='homepage')
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)