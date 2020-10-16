from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import app

# Create your views here.

def home(request):

    """
    ->
    :return:
    """
    
    return render(request, 'app/home.html')


def about(request):

    """
    ->
    :return:
    """
    
    return render(request, 'app/about.html')


def contact(request):

    """
    ->
    :return:
    """
    
    return render(request, 'app/contact.html')


@login_required
def dashboard(request):

    """
    ->
    :return:
    """
    
    return render(request, 'app/dashboard.html')


@login_required
def records(request):

    """
    ->
    :return:
    """
    
    registros = app.objects.all()

    return render(request, 'app/records.html', {'registros': registros})


@login_required
def people(request, id):

    """
    ->
    :return:
    """

    pessoas = get_object_or_404(app, pk=id)

    return render(request, 'app/people.html', {'pessoas': pessoas})


@login_required
def products(request):

    """
    ->
    :return:
    """
    
    produtos = app.objects.all()

    return render(request, 'app/products.html', {'produtos': produtos})  


@login_required
def stock(request, id):

    """
    ->
    :return:
    """

    estoque = get_object_or_404(app, pk=id)

    return render(request, 'app/stock.html', {'estoque': estoque})


class register(generic.CreateView):

    """
    ->
    :return:
    """

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

