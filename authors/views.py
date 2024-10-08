from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RegisterForm


# Create your views here.
def register_view(request):
    resgister_form_data = request.session.get('resgister_form_data', None)
    form = RegisterForm(resgister_form_data)

    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })


def register_create(request):
    if not request.POST:
        raise Http404

    POST = request.POST
    request.session['resgister_form_data'] = POST

    form = RegisterForm(request.POST)

    return redirect('authors:register')
