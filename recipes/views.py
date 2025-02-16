from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Recipe

# Create your views here.
def recipe_home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
        'count': recipes.count()
               }
    return render(request, 'recipe_home.html', context)

