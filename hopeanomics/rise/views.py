from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
# Create your views here.

def start(request):
    return render(request, 'rise/start.html')

def choice(request):
    return HttpResponse('<h1>Take Action or Learn</h1>')

def action(request):
    return HttpResponse('<h1>How to Take Action</h1>')

def learn(request):
    return HttpResponse('<h1>This is your info</h1>')
