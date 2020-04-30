from django.shortcuts import render
from .models import Sessao, Texto, Card, Modal

def index(request):
    template = 'index.html'
    sessoes = Sessao.objects.all()
    textos = Texto.objects.all()
    cards = Card.objects.all()
    modals = Modal.objects.all()
    context = {
        "sessoes" : sessoes,
        "textos" : textos,
        "cards": cards,
        "modals": modals
    }
    return render(request, template, context)