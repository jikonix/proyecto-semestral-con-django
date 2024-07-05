from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.db import models
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView
from .models import Comidas
from .forms import Nuevo_item as ni
# Create your views here.

class inventario(ListView):
    model= Comidas
    template_name= "inventario.html"
    paginate_by= 10
    context_object_name= "comidas"
    form= ni()

    def post(self, request, *args, **kwargs):
        self.form= ni(request.POST, request.FILES)
        form= self.form
        if form.is_valid():
            form.save()
            return redirect("inventario")
        return self.get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]= self.form
        return context

class borrar_item(DeleteView):
    model=Comidas
    template_name= "eliminar_item.html"
    success_url= reverse_lazy("inventario")


class editar_item(UpdateView):
    model= Comidas
    template_name= "editar_item.html"
    success_url= reverse_lazy("inventario")
    form_class= ni

    def form_valid(self, form) -> HttpResponse:
        form.save()
        return redirect("inventario")
    