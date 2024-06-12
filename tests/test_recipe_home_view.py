from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import Recipetestbase


class RecipeHomeViewsTest(Recipetestbase):
    def test_recipe_home_view_functions_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        responser = self.client.get(reverse('recipes:home'))
        self.assertEqual(responser.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        responser = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(responser, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        responser = self.client.get(reverse('recipes:home'))
        self.assertIn('Não encontramos nenhuma receita',
                      responser.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
        # Criando uma receita para esse teste
        self.make_recipe(author_data={'first_name': 'matheus'})

        responser = self.client.get(reverse('recipes:home'))
        content = responser.content.decode('utf-8')
        response_context_recipes = responser.context['recipes']

        # checando se a receita foi criada
        self.assertIn('Recipe Title',  content)
        self.assertIn('10 minutos', content)
        self.assertIn('matheus', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        '''testando se o is_published False não Carega a receita'''
        # Criando a receita para esse teste
        self.make_recipe(is_published=False)

        responser = self.client.get(reverse('recipes:home'))
        content = responser.content.decode('utf-8')

        # checando se a receita existe
        self.assertIn('Não encontramos nenhuma receita',  content)
