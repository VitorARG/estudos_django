from django.shortcuts import render


def home(request):  # pylint: disable=unused-argument
    return render(request, 'recipes/home.html', context={'name': 'Vitor'})
