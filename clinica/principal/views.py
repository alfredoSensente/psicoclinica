"""Views principal"""
from django.shortcuts import render

# Create your views here.
def login(request):
    """Login"""
    return render(request,'principal/login.html')
