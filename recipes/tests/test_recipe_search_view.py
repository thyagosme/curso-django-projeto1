from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeSearchViewTest(RecipeTestBase):
    

    def test_recipe_search_view_function_is_correct(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func, views.search)


    def test_recipe_search_loads_the_correct_template(self):
        """It were created a view function search and the search.html file"""
        response = self.client.get(reverse('recipes:search' ) +'?q=valor')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        response = self.client.get(
            reverse('recipes:search')
        )
        self.assertEqual(response.status_code, 404)
        
    def test_recipe_search_term_is_on_page_title_and_scaped(self):
        url = reverse('recipes:search')+'?q=<Teste>'
        response = self.client.get(url)
        content = response.content.decode('utf-8')
        self.assertIn('Search for &quot;&lt;Teste&gt;&quot;', content)
