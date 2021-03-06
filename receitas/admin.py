from django.contrib import admin
from .models import Receitas


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_per_page = 10


admin.site.register(Receitas, ListandoReceitas)

# Register your models here.
