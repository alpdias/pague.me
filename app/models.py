# -*- coding: utf-8 -*-

'''
Criado em 09/2020
@Autor: Paulo https://github.com/alpdias
'''

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class pessoas(models.Model):

    """
    ->
    :return:
    """

    STATUS = (
        ('ativo', 'ativo'), 
        ('inativo', 'inativo'),
    )
    nome = models.CharField('nome', max_length=255, unique=True)
    telefone = models.CharField('telefone', max_length=15, blank=True)
    email = models.EmailField('e-mail', blank=True)
    cpf = models.CharField('cpf', max_length=14, blank=True)
    endereco = models.CharField('endereço', max_length=255, blank=True)
    observacao = models.CharField('observações', max_length=255, blank=True)
    status = models.CharField(
        max_length = 7, 
        choices = STATUS
    )
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    criado = models.DateTimeField('criado em', auto_now_add=True)
    atualizado = models.DateTimeField('atualizado em', auto_now=True)

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

        verbose_name = 'cadastro'
        verbose_name_plural = 'cadastros'
        ordering = ['nome'] 
 

class estoque(models.Model):

    """
    ->
    :return:
    """

    STATUS = (
        ('disponivel', 'disponivel'), 
        ('esgotado', 'esgotado'),
    )
    produto = models.CharField('produto', max_length=255, unique=True)
    preco = models.DecimalField('preço', max_digits=999, decimal_places=2)
    custo = models.DecimalField('custo', max_digits=999, decimal_places=2)
    quantidade = models.IntegerField('quantidade', blank=True, defautl=0)
    aviso = models.IntegerField('aviso', blank=True, defautl=0)
    descricao = models.CharField('descrição', max_length=255, blank=True)
    fornecedor = models.CharField('fornecedor', max_length=255, blank=True)
    status = models.CharField(
        max_length = 10, 
        choices = STATUS
    )
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    criado = models.DateTimeField('criado em', auto_now_add=True)
    atualizado = models.DateTimeField('atualizado em', auto_now=True)

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

        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
        ordering = ['produto'] 
 

class vendas(models.Model):

    """
    ->
    :return:
    """
    
    STATUS = (
        ('aberto', 'aberto'),
        ('fechado', 'fechado'),
    )
    cliente = models.CharField('cliente', max_length=255, blank=True, default='cliente')
    valor = models.DecimalField('valor', max_digits=999, decimal_places=2)
    pagamento = models.CharField('pagamento', max_length=8)
    comprovante = models.FileField('comprovante')
    recibo = models.CharField('recibo', max_length=255)
    status = models.CharField(
        max_length = 7, 
        choices = STATUS,
        default='aberto'
    )
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    criado = models.DateTimeField('criado em', auto_now_add=True)
    atualizado = models.DateTimeField('atualizado em', auto_now=True)

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

        verbose_name = 'venda'
        verbose_name_plural = 'vendas'
        ordering = ['-criado'] 
        
        
class empresas(models.Model):

    """
    ->
    :return:
    """
    
    STATUS = (
        ('ativo', 'ativo'), 
        ('inativo', 'inativo'),
    )
    empresa = models.CharField('empresa', max_length=255)
    cnpj = models.CharField('cnpj', max_length=18)
    endereco = models.CharField('endereço', max_length=255)
    cidadeEstado = models.CharField('cidade/estado', max_length=255)
    observacao = models.CharField('observações', max_length=255, blank=True)
    frase = models.CharField('rodapé', max_length=255, default='VOLTE SEMPRE!!')
    porta = 
    servidor = models.CharField('host', max_length=255)
    usuarioServidor = models.CharField('host usuário', max_length=255)
    senhaServidor = models.CharField('host senha', max_length=255)
    email = models.EmailField('e-mail')
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(
        max_length = 7, 
        choices = STATUS
    )
    criado = models.DateTimeField('criado em', auto_now_add=True)
    atualizado = models.DateTimeField('atualizado em', auto_now=True)

    def __str__(self):

        """
        ->
        :return:
        """

        return self.empresa


    class Meta:

        """
        ->
        :return:
        """

        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'
        ordering = ['empresa'] 
