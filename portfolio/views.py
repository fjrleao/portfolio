from django.shortcuts import render
from .models import Sessao, Texto, Card

def index(request):
    template = 'index.html'
    sessoes = Sessao.objects.all()
    textos = Texto.objects.all()
    cards = Card.objects.all()
    context = {
        "sessoes" : sessoes,
        "textos" : textos,
        "cards": cards
    }
    return render(request, template, context)