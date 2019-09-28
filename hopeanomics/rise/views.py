from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def start(request):
    return HttpResponse('<h1>Enter your state and campaign</h1>')

def choice(request):
    return HttpResponse('<h1>Take Action or Learn</h1>')

def action(request):
    return HttpResponse('<h1>How to Take Action</h1>')

def learn(request):
    return HttpResponse('<h1>This is your info</h1>')