from django.shortcuts import render, redirect
from .models import Sessao, Texto, Card, Modal, Perfil, Link
from django.views.decorators.csrf import csrf_protect

def index(request):
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

@csrf_protect
def email(request):
    if request.POST:
        print("nome\n " + request.POST.get('nome'))
        print("email:\n " + request.POST.get('email'))
        print("assunto:\n " + request.POST.get('assunto'))
        print("texto:\n " + request.POST.get('texto'))
        return redirect(index)