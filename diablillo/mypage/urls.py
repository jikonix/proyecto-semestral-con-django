from django.urls import path
from .views import homepage
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('', homepage.as_view(), name='homepage')
] 