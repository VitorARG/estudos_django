from django.shortcuts import render


def home(request):  # pylint: disable=unused-argument
    return render(request, 'recipes/pages/home.html')


def recipe(request, id):  # pylint: disable=unused-argument
    return render(request, 'recipes/pages/recipe-view.html')
