from django.contrib import admin
from portfolio.models import Card, Modal, Sessao, Texto

@admin.register(Sessao)
class SessaoAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    search_fields = ['titulo']
    prepopulated_fields = {
        'slug': ('titulo', )
        }

@admin.register(Texto)
class TextoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'sessao']
    search_fields = ['titulo']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'sessao']
    search_fields = ['titulo']

@admin.register(Modal)
class ModalAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'card']
    search_fields = ['titulo']