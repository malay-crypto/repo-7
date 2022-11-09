
from django.urls import path

from app1 import views

urlpatterns = [
    path('', views.index),
    path('login/', views.loginPage),
    path('register/', views.register),
    path('loginvalidation/', views.loginValidation),
    path('signup/', views.signUp),
    path('home/', views.home),
    path('form/', views.form),
    path('inventory/', views.inventory),
    path('logout/', views.logout_view),
]
