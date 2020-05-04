from django.shortcuts import render, HttpResponse
from .models import Sessao, Texto, Card, Modal, Perfil, Link

def index(request):
    try:
        template = 'index.html'
        sessoes = Sessao.objects.all()
        textos = Texto.objects.all()
        cards = Card.objects.all()
        modals = Modal.objects.all()
        perfil = Perfil.objects.first()
        links = Link.objects.all()
        context = {
            "sessoes" : sessoes,
            "textos" : textos,
            "cards": cards,
            "modals": modals,
            "perfil": perfil,
            "links" : links
        }
        return render(request, template, context)
    except:
        return HttpResponse('<h3>Erro inesperado, configure seus dados no banco para exibir a página</h3>')

