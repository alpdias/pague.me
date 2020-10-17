from django.db import models

# Create your models here.

class pessoas(models.Model):

    """
    ->
    :return:
    """

    STATUS = (
        ('ativo', 'ATIVO'),
        ('inativo', 'INATIVO'),
    )
    nome = models.CharField('Nome', max_length = 255)
    telefone = models.CharField('Telefone', max_length = 14)
    email = models.EmailField('E-mail')
    endereco = models.CharField('Endereço', max_length = 255)
    observacao = models.TextField('Observações')
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
 

class estoque(models.Model):

    """
    ->
    :return:
    """

    STATUS = (
        ('disponivel', 'DISPONIVEL'),
        ('esgotado', 'ESGOTADO'),
    )
    produto = models.CharField('Produto', max_length = 255)
    preco = models.DecimalField('Preço', max_digits=999, decimal_places=2)
    custo = models.DecimalField('Custo', max_digits=999, decimal_places=2)
    quantidade = models.IntegerField('Quantidade')
    descricao = models.TextField('Descrição')
    status = models.CharField(
        max_length = 10,
        choices = STATUS
    )

    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):

        """
        ->
        :return:
        """

        return self.produto


    class Meta:

        """
        ->
        :return:
        """

        verbose_name = 'PRODUTO'
        verbose_name_plural = 'PRODUTOS'
        ordering = ['produto'] 
        
