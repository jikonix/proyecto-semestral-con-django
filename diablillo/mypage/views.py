from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.db import models
from django.views import view


# Create your views here.
class homepage(view):
    template= 