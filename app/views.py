from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    """
    ->
    :return:
    """
    
    return render(request, 'app/home.html')


@login_required
def register(request):

    """
    ->
    :return:
    """
    
    return render(request, 'app/register.html')


@login_required
def dashboard(request):

    """
    ->
    :return:
    """
    
    return render(request, 'app/dashboard.html')
