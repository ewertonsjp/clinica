from django.shortcuts import render
from django.http import HttpResponse
from . models import Cliente

def home(request):
    return render(request, 'home.html', {})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 
        'cliente/list.html', {'clientes':clientes})

def cliente_show(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 
        'cliente/show.html', {'cliente':cliente})