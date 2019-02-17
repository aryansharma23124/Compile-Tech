from django.http import HttpResponse
from django.template import  loader
from .models import users
from django.shortcuts import render


def index(request):
    return (render(request,"home.html"))