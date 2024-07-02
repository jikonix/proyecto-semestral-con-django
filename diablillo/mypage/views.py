from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import models
from django.views import View
from .forms import nueva_pizza as np
from .models import Pizza
# Create your views here.
class homepage(View):
    template= loader.get_template("home.html")
    newpizza= np()
    
    def get(self, request):
        pizzas=Pizza.objects.all()
        print(pizzas)
        context= {
        'form': self.newpizza,
        'pizzas': pizzas
        }
        return HttpResponse(self.template.render(context, request))

    def post(self, request):
        
        self.newpizza=np(request.POST)
        form=self.newpizza
        if form.is_valid():
            form.save()
        return redirect('homepage')