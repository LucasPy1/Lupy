from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add_abilities/', views.add_abilities)
]