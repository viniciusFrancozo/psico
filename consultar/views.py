from django.shortcuts import render, redirect

# Create your views here.

def consultar(request):
    return request(request, 'consultar.html')
