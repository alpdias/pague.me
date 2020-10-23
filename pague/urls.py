  
# -*- coding: utf-8 -*-

'''
Criado em 09/2020
@Autor: Paulo https://github.com/alpdias
'''

"""pague URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from app.views import home, about, contact, dashboard, cart, buy, sales, products, stock, records, people, register
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
    path('cart/', cart, name='cart'),
    path('buy/', buy, name='buy'),
    path('sales/<int:id>', sales, name='sales'),
    path('products/', products, name='products'),
    path('stock/<int:id>', stock, name='stock'),
    path('records/', records, name='records'),
    path('people/<int:id>', people, name='people'),
    path('register/', views.register.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
