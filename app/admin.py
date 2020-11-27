# -*- coding: utf-8 -*-

'''
Criado em 09/2020
@Autor: Paulo https://github.com/alpdias
'''

from django.contrib import admin

# Register your models here.

from .models import pessoas, estoque, vendas, empresas

class pessoasAdmin(admin.ModelAdmin):

    """
    -> Definiçao do 'display' das tabelas no admin do site\
    """

    list_display = ['nome', 'telefone', 'email', 'status']
    search_fields = ['nome', 'status']

    
admin.site.register(pessoas, pessoasAdmin)

class estoqueAdmin(admin.ModelAdmin):

    """
    -> Definiçao do 'display' das tabelas no admin do site\
    """

    list_display = ['produto', 'codigo', 'preco', 'quantidade', 'status']
    search_fields = ['produto', 'fornecedor', 'status']


admin.site.register(estoque, estoqueAdmin)

class vendasAdmin(admin.ModelAdmin):

    """
    -> Definiçao do 'display' das tabelas no admin do site\
    """

    list_display = ['cliente', 'valor', 'pagamento', 'status', 'criado']
    search_fields = ['valor', 'status', 'criado']


admin.site.register(vendas, vendasAdmin)

class empresasAdmin(admin.ModelAdmin):

    """
    -> Definiçao do 'display' das tabelas no admin do site\
    """

    list_display = ['empresa', 'cnpj', 'status', 'criado']
    search_fields = ['empresa', 'criado']


admin.site.register(empresas, empresasAdmin)

