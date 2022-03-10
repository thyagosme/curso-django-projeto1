
from unittest import skip

from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def tearDown(self) -> None:
        del self.recipe
        return super().tearDown()
    
    def make_recipe_no_defaults(self):
        recipe = Recipe( 
            category= self.make_category(name = 'Test Default Category'),
            author= self.make_author(username='newuser'),
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug-for-no-default',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
           )
        return recipe
    
    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    #@skip('Teste falhando porque foi setado slug unico!!!')
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
      
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A'*75
        
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
    
    #@skip('Teste falhando porque foi setado slug unico!!!')
    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        recipe.full_clean()
        recipe.save()
      
        self.assertFalse(recipe.preparation_steps_is_html)
        
    #@skip('Teste falhando porque foi setado slug unico!!!')
    def test_recipe_is_publeshed_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        recipe.full_clean()
        recipe.save()
        x = recipe.is_published
        self.assertFalse(recipe.is_published)

    def test_recipe_string_representation(self):
        needed = 'Testing Representation'
        self.recipe.title = needed
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe), needed,
            msg=f'Recipe string representation must be '
                f'"{needed}" but "{str(self.recipe)}" was received.'
        )
