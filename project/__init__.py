import unittest


def suite():   
    return unittest.TestLoader().discover("recipe.tests", pattern="test*.py")
