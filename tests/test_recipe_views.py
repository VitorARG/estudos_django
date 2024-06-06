from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import Recipetestbase


class RecipeViewsTest(Recipetestbase):
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

    def test_recipe_category_view_functions_is_correct(self):
        view = resolve(reverse('recipes:category',
                               kwargs={'category_id': 1000}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_founde(self):
        responser = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(responser.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        need_title = 'Esse é um test da pagina category'

        self.make_recipe(title=need_title)

        responser = self.client.get(
            reverse('recipes:category', args={1}))
        content = responser.content.decode('utf-8')

        self.assertIn(need_title, content)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        '''testando se o is_published False não Carega a receita em category'''
        # Criando a receita para esse teste
        recipe = self.make_recipe(is_published=False)

        responser = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id}))

        # O status code esperado é o 404
        self.assertEqual(responser.status_code, 404)

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

    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertTemplateUsed(response, 'recipes/pages/search.html')
