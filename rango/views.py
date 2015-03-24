from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Sup peeps <br/><a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("This is at the About Page <br/><a href='/rango/'>Index</a>")
