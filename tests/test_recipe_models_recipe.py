
from django.forms import ValidationError

from .test_recipe_base import Recipetestbase


class RecipeModelsTest(Recipetestbase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_fields_max_lenght(self):
        fields = [
            ('title', 65),
            ('description', 65),
            (' preparation_time_unit', 65),
            (' servings_unit', 65),
        ]
        for field, maxlengt in fields:
            setattr(self.recipe, field, 'a' * (maxlengt + 1))
            with self.assertRaises(ValidationError):
                self.recipe.full_clean()
