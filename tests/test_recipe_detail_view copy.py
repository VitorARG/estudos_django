from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import Recipetestbase


class RecipeDetailViewsTest(Recipetestbase):
    def test_recipe_detail_view_functions_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_datail_view_returns_404_if_no_recipes_founde(self):
        responser = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(responser.status_code, 404)

    def test_recipe_detail_template_loads_recipes(self):
        need_title = 'essa é a pagina de detalhe - isso carrega uma receita'

        self.make_recipe(title=need_title)

        responser = self.client.get(
            reverse('recipes:recipe', args={1}))
        content = responser.content.decode('utf-8')

        self.assertIn(need_title, content)

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        '''testando se o is_published False não Carega a receita em category'''
        # Criando a receita para esse teste
        recipe = self.make_recipe(is_published=False)

        responser = self.client.get(
            reverse('recipes:recipe', args={recipe.id}))

        # O status code esperado é o 404
        self.assertEqual(responser.status_code, 404)
