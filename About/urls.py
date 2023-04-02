from django.contrib import admin
from django.urls import path
from About import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
]
