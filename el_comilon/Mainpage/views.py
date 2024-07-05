from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.db import models
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView
from Adminpage.models import Comidas
from .models import Carro, items_carro

# Create your views here.

class session_mixin:
    def dispatch(self, request, *args, **kwargs):
        self.session_key = self.get_session(request)
        return super().dispatch(request, *args, **kwargs)

    def get_session(self, request):
        session_key= request.session.session_key

        if not session_key:
            request.sessionkey.create()
            session_key= request.session.session_key
        
        return session_key



class carrito(session_mixin, View):

    def post(self, request, slug):
        comida= get_object_or_404(Comidas, slug=slug)
        
        carro, created= Carro.objects.get_or_create(key_sesion= self.session_key)
        item_carro, created= items_carro.objects.get_or_create(carro=carro, comida=comida)
        if not created:
            item_carro.cantidad += 1
            item_carro.save()
        return redirect('ver_carro')

