from django.db import models

# Create your models here.

class app(models.Model):

    """
    ->
    :return:
    """

    STATUS = (
        ('ativo', 'ATIVO'),
        ('inativo', 'INATIVO'),
    )

    nome = models.CharField('Nome', max_length = 255)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length = 14)
    endereco = models.TextField('Endereço')
    status = models.CharField(
        max_length = 7,
        choices = STATUS
    )
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):

        """
        ->
        :return:
        """

        return self.nome


    class Meta:

        """
        ->
        :return:
        """

        verbose_name = 'CADASTRO'
        verbose_name_plural = 'CADASTROS'
        ordering = ['nome'] 