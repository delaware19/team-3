# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from uniauth.decorators import login_required

def start(request):
    st = request.GET.get('State')
    cache.set('a', st)
    print(cache.get('a'))
    return render(request, 'rise/start.html', {})
    
def issue(request):

    print(cache.get('a')) 
    iss = request.GET.get('Issue')
    return render(request, 'rise/issue.html', {})
    
def index(request):
    return render(request, 'rise/index.html')

def choice(request):
    # learnbutton = request.POST.get("learn")
    # actionbutton = request.POST.get("action")
    # if learnbutton:
    #     return render(request, 'rise/learn.html')
    # elif actionbutton:
    #     return render(request, 'rise/action.html')
    return render (request, 'rise/choice.html') 

def action(request):
    return render (request, 'rise/action.html')

def learn(request):
    peoplebutton = request.POST.get("people")
    deadlinesbutton = request.POST.get("deadlines")
    if peoplebutton:
        return render(request, 'rise/people.html')
    elif deadlinesbutton:
        return render(request, 'rise/deadlines.html')
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

def people(request):
    return render(request, 'rise/people.html')

def deadlines(request):
    return render (request, 'rise/deadlines.html')

def feed(request):
    return render(request, 'rise/feed.html')
