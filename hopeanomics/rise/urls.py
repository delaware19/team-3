from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='rise-index'),
    path('issue.html', views.issue, name='rise-issue'),
    path('choice.html/',  views.choice, name='rise-choice'),
    path('action.html/', views.action, name='rise-action'),
    path('learn.html/', views.learn, name='rise-learn'),
    path('register.html/', views.register, name='rise-register'),
]
