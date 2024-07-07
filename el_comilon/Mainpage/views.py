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

        if not request.session.session_key:
            request.session.create()
        return request.session.session_key

    def get_queryset(self):
        carro, created= Carro.objects.get_or_create(key_sesion= self.session_key)
        return Carro.objects.filter(carro=carro)
    
    def get_cart(self):
        carro, created = Carro.objects.get_or_create(key_sesion=self.session_key)

        return carro


class mainpage(session_mixin, View):
    
    template_name= "main.html"

    def get(self, request):

        ofertas= Comidas.objects.filter(agregado=False).order_by('-precio')[:5]
        listado= Comidas.objects.all().order_by('fecha_ingreso')

        context = {
            'ofertas': ofertas,
            'listado': listado,
        }

        return render(request, self.template_name, context)

  


class agregar_al_carro(session_mixin, View):
    def post(self, request, slug):
        comida= get_object_or_404(Comidas, slug=slug)
        carro, created= Carro.objects.get_or_create(key_sesion= self.session_key)
        item_carro, created= items_carro.objects.get_or_create(carro=carro, comida=comida)
        if not created:
            item_carro.cantidad += 1
            item_carro.save()
        return redirect('mainpage')
    

class ver_carro(session_mixin, ListView):
    model=items_carro
    template_name= "ver_carro.html"
    context_object_name= 'items_carro'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carro= self.get_cart()
        context['carro']= carro
        return context

class borrar_item_carro(session_mixin, DeleteView):
    model = items_carro
    template_name= 'cart_delete.html'
    success_url= reverse_lazy('ver_carro.html')

    def get_queryset(self):
        return super().get_queryset()
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)
    
