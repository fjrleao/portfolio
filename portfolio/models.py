from django.db import models
from ckeditor.fields import RichTextField

class Sessao(models.Model):

    titulo = models.CharField(max_length=25, null=False, unique=True)
    icone_menu = models.CharField(max_length=512)
    imagem_parallax = models.CharField(max_length=512)
    slug = models.SlugField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Sessoes'

class Texto(models.Model):

    titulo = models.CharField(max_length=120, null=True, blank=True)
    conteudo = RichTextField()
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)

    def __str__(self):
        return self.conteudo

class Card(models.Model):

    titulo = models.CharField(max_length=120, null=False)
    conteudo = RichTextField()
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.titulo

class Modal(models.Model):

    titulo = models.CharField(max_length=25, null=False, unique=False)
    conteudo = RichTextField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.titulo

class Perfil(models.Model):

    nome = models.CharField(max_length=255, null=False)
    foto = models.CharField(max_length=660, null=False)
    favicon = models.CharField(max_length=660, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Perfis'

class Link(models.Model):

    TIPO = [
        ('TX','TEXTO'),
        ('IC', 'ICONE')
    ]

    nome = models.CharField(max_length=25, null=False)
    tipo = models.CharField(max_length=3, choices=TIPO, default='IC')
    referencia = models.CharField(max_length=255, null=False)
    link = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome
