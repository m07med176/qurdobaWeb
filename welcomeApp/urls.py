from django.urls import path
from welcomeApp import views

urlpatterns = [
    path('', views.welcome,name='welcome'),
]