from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from recipes.models import Category, Recipe

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A'*75
        
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
    