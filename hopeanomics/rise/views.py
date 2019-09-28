from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def start(request):
    return render(request, 'rise/start.html') 

def choice(request):
    return render (request, 'rise/choice.html') 

def action(request):
    return render (request, 'rise/action.html') 

def learn(request):
    return render (request, 'rise/learn.html') 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('start')
    else:
        form = UserCreationForm()
    return render(request, 'rise/register.html', {'form': form})

def people(request):
    return render (request, 'rise/people.html')

def deadlines(request):
    return render (deadlines, 'rise/deadlines.html')