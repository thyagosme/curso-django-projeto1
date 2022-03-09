from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
 
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')  #'recipe:home' = app_name (name space) :  url_name
        self.assertEqual(url,'/')
        
        
    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id':1})
       
        
        self.assertEqual(url,'/recipes/category/1/')
        
    def tests_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id':10})
    
        
        self.assertEqual(url,'/recipes/10/')
    
    def test_recipe_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url,'/recipes/search/')
