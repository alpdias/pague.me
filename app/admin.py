from django.contrib import admin

# Register your models here.

from .models import pessoas, estoque

class pessoasAdmin(admin.ModelAdmin):

    """
    ->
    :return:
    """

    list_display = ['nome', 'telefone', 'email', 'status']
    search_fields = ['nome', 'status']

    
class estoqueAdmin(admin.ModelAdmin):

    """
    ->
    :return:
    """

    list_display = ['produto', 'preco', 'quantidade', 'status']
    search_fields = ['produto', 'status']


admin.site.register(app, pessoasAdmin, estoqueAdmin)
