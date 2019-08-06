from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length = 100)
    dtCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField()

    def __str__(self):
        return self.descricao


class Filme(models.Model):
    nome = models.CharField(max_length=50)
    notaImdb = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome