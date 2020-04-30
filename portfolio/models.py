from django.db import models

class Sessao(models.Model):

    titulo = models.CharField(max_length=25, null=False, unique=True)
    icone_menu = models.CharField(max_length=512)
    imagem_parallax = models.CharField(max_length=512)
    form_contato = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Sessoes'

class Texto(models.Model):

    titulo = models.CharField(max_length=120)
    conteudo = models.TextField(null=False)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Card(models.Model):

    titulo = models.CharField(max_length=120, null=False)
    conteudo = models.TextField(max_length=255, null=False)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Modal(models.Model):
    titulo = models.CharField(max_length=25, null=False, unique=True)
    conteudo = models.TextField(null=False)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.titulo
