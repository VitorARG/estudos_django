from django.shortcuts import render

from util.recipes.factory import make_recipe


def home(request):  # pylint: disable=unused-argument
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):  # pylint: disable=unused-argument
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe
    })
