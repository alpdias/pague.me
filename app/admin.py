  
# -*- coding: utf-8 -*-

'''
Criado em 09/2020
@Autor: Paulo https://github.com/alpdias
'''

from django.contrib import admin

# Register your models here.

from .models import pessoas, estoque, vendas

class pessoasAdmin(admin.ModelAdmin):

    """
    ->
    :return:
    """

    list_display = ['nome', 'telefone', 'email', 'status']
    search_fields = ['nome', 'status']

    
admin.site.register(pessoas, pessoasAdmin)

class estoqueAdmin(admin.ModelAdmin):

    """
    ->
    :return:
    """

    list_display = ['produto', 'preco', 'quantidade', 'status']
    search_fields = ['produto', 'status']


admin.site.register(estoque, estoqueAdmin)

class vendasAdmin(admin.ModelAdmin):

    """
    ->
    :return:
    """

    list_display = ['cliente', 'valor', 'pagamento', 'status', 'criado']
    search_fields = ['valor', 'status', 'criado']


admin.site.register(vendas, vendasAdmin)
