from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
def register(request):

    """
    ->
    :return:
    """
    
    return render(request, 'app/register.html')

