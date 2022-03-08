from unittest import skip

from django.urls import resolve, reverse
from recipes import views
from recipes.models import Recipe

from .test_recipe_base import RecipeTestBase

# Create your tests here.

   
   
class RecipeViewsTest(RecipeTestBase):
    @skip('Estou pulando este teste!!!')  
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home')) # busca dados no arquivo recipe.urls
        self.assertIs(view.func, views.home)
        self.assertIs()
     
        
    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        
    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
    
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here! 😭</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        recipe1 = self.make_recipe(author_data={'first_name': 'Thyago1'}, category_data={'name': 'café da manhã'}, preparation_time=15)
        #recipe2 = self.make_recipe(author_data={'first_name': 'Thyago2'}, category_data={'name': 'café da manhã'}, preparation_time=15)
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertIn('15 Minutos', content)
        self.assertIn('5 Porções', content)
        self.assertIn('café da manhã', content)
        self.assertEqual(len(response_context_recipes), 1) 
    


    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)
        
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        Recipe.objects.all().delete()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertEqual(response.status_code, 404)
        
