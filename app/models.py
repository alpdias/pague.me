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
    nome = models.CharField('Nome', max_length=255, unique=True)
    telefone = models.CharField('Telefone', max_length=15, blank=True)
    email = models.EmailField('E-mail', blank=True)
    cpf = models.CharField('CPF', max_length=14, blank=True)
    endereco = models.CharField('Endereço', max_length=255, blank=True)
    observacao = models.CharField('Observações', max_length=255, blank=True)
    status = models.CharField(
        max_length = 7, 
        choices = STATUS
    )
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
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

        verbose_name = 'cadastro'
        verbose_name_plural = 'cadastros'
        ordering = ['nome'] 
 

class estoque(models.Model):

    """
    ->
    :return:
    """

    STATUS = (
        ('disponivel', 'disponível'), 
        ('esgotado', 'esgotado'),
    )
    produto = models.CharField('Produto', max_length=255, unique=True)
    preco = models.DecimalField('Preço', max_digits=999, decimal_places=2)
    custo = models.DecimalField('Custo', max_digits=999, decimal_places=2)
    quantidade = models.IntegerField('Quantidade', blank=True, default=0)
    aviso = models.IntegerField('Aviso', blank=True, default=0)
    descricao = models.CharField('Descrição', max_length=255, blank=True)
    fornecedor = models.CharField('Fornecedor', max_length=255, blank=True)
    status = models.CharField(
        max_length = 10, 
        choices = STATUS
    )
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
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
    cliente = models.CharField('Cliente', max_length=255, default='Cliente')
    valor = models.DecimalField('Valor', max_digits=999, decimal_places=2)
    pagamento = models.CharField('Pagamento', max_length=8)
    comprovante = models.FileField('Comprovante')
    recibo = models.CharField('Recibo', max_length=255)
    status = models.CharField(
        max_length = 7, 
        choices = STATUS,
        default='aberto'
    )
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
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
    empresa = models.CharField('Empresa', max_length=255)
    cnpj = models.CharField('CNPJ', max_length=18)
    endereco = models.CharField('Endereço', max_length=255)
    cidadeEstado = models.CharField('cidade/Estado', max_length=255)
    observacao = models.CharField('Observações', max_length=255, blank=True)
    frase = models.CharField('Rodapé', max_length=255, default='VOLTE SEMPRE!!')
    porta = models.IntegerField('Porta')
    servidor = models.CharField('Servidor', max_length=255)
    usuarioServidor = models.CharField('Usuário', max_length=255)
    senhaServidor = models.CharField('Senha', max_length=255)
    email = models.EmailField('E-mail')
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
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

        return self.empresa


    class Meta:

        """
        ->
        :return:
        """

        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'
        ordering = ['empresa'] 
