from django.http import Http404
from django.shortcuts import get_list_or_404, render

from util.recipes.factory import make_recipe

from .models import Recipe


def home(request):  # pylint: disable=unused-argument
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id, is_published=True
    ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |'
    })


def recipe(request, id):  # pylint: disable=unused-argument
    recipe = Recipe.objects.filter(
        pk=id,
        is_published=True
    ).order_by('-id').first
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe(),
        'is_detail_page': True,
    })
