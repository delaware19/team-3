from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
# Create your views here.

def start(request):
    return render(request, 'rise/start.html') 

def choice(request):
    return render (request, 'rise/choice.html') 

def action(request):
    return render (request, 'rise/action.html') 

def learn(request):
    return render (request, 'rise/learn.html') 

