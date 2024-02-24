from django.http import HttpResponse
from django.shortcuts import render


def home(request):  # pylint: disable=unused-argument
    return render(request, 'recipes/home.html', context={'name': 'Vitor'})


def sobre(request):  # pylint: disable=unused-argument
    return render(request, 'temp.html', context={'name': 'Vitor'})


def contato(request):  # pylint: disable=unused-argument
    return HttpResponse('contato 3')
