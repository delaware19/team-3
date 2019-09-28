from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'rise/index.html')

def choice(request):
    return render (request, 'rise/choice.html') 

def action(request):
    return render (request, 'rise/action.html') 

def learn(request):
    return render (request, 'rise/learn.html')



