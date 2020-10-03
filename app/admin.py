from django.contrib import admin

# Register your models here.

from .models import app

class appAdmin(admin.ModelAdmin):

    """
    ->
    :return:
    """

    list_display = ['nome', 'email', 'telefone', 'status']
    search_fields = ['nome', 'status']


admin.site.register(app, appAdmin)
