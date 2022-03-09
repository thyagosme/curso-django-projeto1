# scripts/delete_all_questions.py
from polls.models import Question


def run():
    # Fetch all questions
    questions = Question.objects.all()
    # Delete questions
    questions.delete()

#from recipes.tests.test_recipe_base import RecipeTestBase

#print('oi')
# for i in range(1,9):
#     r = RecipeTestBase().make_recipe()
#     r.title = 'Recipe '+i
#     r.save()


#>>> exec(open('create_recipes.py').read())
