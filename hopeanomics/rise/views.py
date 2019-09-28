from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from uniauth.decorators import login_required

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
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('start')
    else:
        form = UserCreationForm()
    return render(request, 'rise/register.html', {'form': form})


@login_required
def checklist(request): 
    return render(request, 'rise/checklist.html')