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
    nome = models.CharField('Nome', max_length=255)
    telefone = models.CharField('Telefone', max_length=14, blank=True)
    email = models.EmailField('E-mail', blank=True)
    cpf = models.CharField('CPF', max_length=14, blank=True)
    endereco = models.CharField('Endereço', max_length=255, blank=True)
    observacao = models.TextField('Observações', blank=True)
    status = models.CharField(
        max_length = 7, 
        choices = STATUS
    )
    criado = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado = models.DateTimeField('Atualizado em', auto_now=True)

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
    produto = models.CharField('Produto', max_length=255)
    preco = models.DecimalField('Preço', max_digits=999, decimal_places=2)
    custo = models.DecimalField('Custo', max_digits=999, decimal_places=2)
    quantidade = models.IntegerField('Quantidade')
    descricao = models.TextField('Descrição', blank=True)
    status = models.CharField(
        max_length = 10, 
        choices = STATUS
    )
    criado = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado = models.DateTimeField('Atualizado em', auto_now=True)

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
 

class vendas(models.Model):

    """
    ->
    :return:
    """
    
    STATUS = (
        ('aberto', 'ABERTO'),
        ('fechado', 'FECHADO'),
    )
    cliente = models.CharField('Cliente', max_length=255, blank=True)
    valor = models.DecimalField('Valor', max_digits=999, decimal_places=2)
    pagamento = models.CharField('Pagamento', max_length=8)
    comprovante = models.FileField(
        upload_to = 'static/archve/', 
        verbose_name = 'Comprovante',
        blank=True
    )
    recibo = models.CharField('Recibo', max_length=255, blank=True)
    status = models.CharField(
        max_length = 7, 
        choices = STATUS,
        default='aberto'
    )
    criado = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):

        """
        ->
        :return:
        """

        return str(self.criado) if self.criado else ''


    class Meta:

        """
        ->
        :return:
        """

        verbose_name = 'VENDA'
        verbose_name_plural = 'VENDAS'
        ordering = ['-criado'] 
