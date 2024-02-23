from django.http import HttpResponse

# from django.shortcuts import render


def home(request):  # pylint: disable=unused-argument
    return HttpResponse('home 1')


def sobre(request):  # pylint: disable=unused-argument
    return HttpResponse('Sobre 2')


def contato(request):  # pylint: disable=unused-argument
    return HttpResponse('contato 3')
