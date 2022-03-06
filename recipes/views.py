from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe

from .models import Category, Recipe


# Create your views here.
def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id,is_published = True).order_by('-id')
    return render(request,'recipes/pages/category.html', context={'recipes':
        recipes})

    # return render(request,'recipes/pages/home.html', context={'recipes':
    #     [make_recipe() for _ in range(10)]})
def home(request):
    recipes = Recipe.objects.filter(is_published = True).order_by()
    return render(request,'recipes/pages/home.html', context={'recipes':
        recipes})


def recipe(request, id):
    return render(request,'recipes/pages/recipe-view.html', context={'recipe':
       make_recipe(),
       'is_detail_page':True})

