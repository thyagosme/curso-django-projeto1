from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class RecipeURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        variavel = '123456'
        print('OLÁ MUNDO')
        assert 1==1 
        
        
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url,'/')
    
