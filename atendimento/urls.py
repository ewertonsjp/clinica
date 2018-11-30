from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cliente/', views.cliente_list),
    path('cliente/<int:cliente_id>/', views.cliente_show)
]