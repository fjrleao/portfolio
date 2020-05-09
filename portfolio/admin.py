from django.contrib import admin
from portfolio.models import Card, Modal, Sessao, Texto, Perfil, Link

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
    search_fields = ['titulo', 'conteudo']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'sessao']
    search_fields = ['titulo']
    prepopulated_fields = {
        'slug': ('titulo', )
        }

@admin.register(Modal)
class ModalAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'card']
    search_fields = ['titulo']
    prepopulated_fields = {
        'slug': ('titulo', )
        }

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['nome']