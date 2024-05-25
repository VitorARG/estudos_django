
from django.forms import ValidationError
from parameterized import parameterized

from .test_recipe_base import Recipetestbase


class RecipeModelsTest(Recipetestbase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_fields_max_lenght(self, field, maxlength):
        setattr(self.recipe, field, 'A' * (maxlength + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
