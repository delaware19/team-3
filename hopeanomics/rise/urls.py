from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.start, name='rise-start'),
    path('choice/',  views.choice, name='rise-choice'),
    path('action/', views.action, name='rise-action'),
    path('learn/', views.learn, name='rise-learn'),
    path('register/', views.register, name='rise-register'),
    path('login/', auth_views.LoginView.as_view(template_name='rise/login.html'), name='rise-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='rise/logout.html'), name='rise-logout'),
    path('accounts/profile/', views.checklist, name="checklist")
]