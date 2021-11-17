from django.contrib import admin
from .models import *

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'preco_real', 'estoque')


admin.site.register(Tag, TagAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
