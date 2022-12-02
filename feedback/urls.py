from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback , name='feedback'),
    path('done/', views.submited , name='submitted'),
]