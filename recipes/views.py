import os

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.pagination import make_pagination

from .models import Recipe

PER_PAGE = os.environ.get('PER_PAGE', 6)
PER_PAGE = int(PER_PAGE)

# Create your views here.
def category(request, category_id):
 
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published = True).order_by('-id')
        )
    
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    
    return render(request,'recipes/pages/category.html', context={
        'recipes':  page_obj,  
        'pagination_range': pagination_range,
        'title': f'{page_obj[0].category.name} - Category' }
                  )

def home(request):
    recipes = Recipe.objects.filter(is_published = True).order_by('-id')
    
    messages.success(request, 'EPA, VOCÊ FOI PESQUISAR ALGO QUE EU VI!')
    
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
 
    
    return render(request,'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        })
    
   # return render(request,'recipes/pages/home.html', context={'recipes': recipes})

def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)
    
    return render(request,'recipes/pages/recipe-view.html', context={'recipe':
       recipe,'is_detail_page':True})

def search(request):
    
    
    search_term = request.GET.get('q','').strip()
    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
        Q(title__icontains =  search_term) |
        Q(description__icontains = search_term),
            )
    recipes =  recipes.order_by('-id')
    recipes= recipes.filter(is_published = True)
    
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    
    return render(request, 'recipes/pages/search.html',  
    context={
        'page_title': f'Search for "{search_term}" | ',
        'search_term':search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_qery': f'&q={search_term}',
    })
