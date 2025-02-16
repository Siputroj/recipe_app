from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def home(request):
    context = {}
    return render(request, 'index.html', context)