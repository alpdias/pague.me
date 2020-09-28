from django.db import models

# Create your models here.

class app(models.Model):

    STATUS = (
        ('ativo', 'ATIVO'),
        ('inativo', 'INATIVO'),
    )

    nome = models.CharField(max_length = 255)
    email = models.EmailField()
    telefone = models.CharField(max_length = 14)
    endereco = models.TextField()
    status = models.CharField(
        max_length = 7,
        choices = STATUS
    )
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
