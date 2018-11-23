from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cliente/', views.cliente_list)
]