# -*- coding: utf-8 -*-

'''
Criado em 09/2020
@Autor: Paulo https://github.com/alpdias
'''

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator
from .models import pessoas, estoque, vendas
from pathlib import Path
from datetime import datetime
import locale
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Create your views here.

def home(request):

    """
    ->
    :return:
    """
    
    return render(request, 'app/home.html')


def about(request):

    """
    ->
    :return:
    """
    
    return render(request, 'app/about.html')


def contact(request):

    """
    ->
    :return:
    """
    
    return render(request, 'app/contact.html')


@login_required
def dashboard(request):

    """
    ->
    :return:
    """
    
    return render(request, 'app/dashboard.html')


@login_required
def buy(request):

    """
    ->
    :return:
    """
    
    listaVendas = vendas.objects.all().filter(usuario=request.user)

    paginas = Paginator(listaVendas, 8)

    pagina = request.GET.get('page')

    venda = paginas.get_page(pagina)

    return render(request, 'app/buy.html', {'venda': venda})  


@login_required
def sales(request, id):

    """
    ->
    :return:
    """
    
    venda = get_object_or_404(vendas, pk=id).filter(usuario=request.user)

    return render(request, 'app/sales.html', {'venda': venda})  


def opEstoque(itens, quantidades):
    
    """
    ->
    :return:
    """

    i = len(itens)

    while i > 0:

        nomeProduto = itens[0]
        qtd = int(quantidades[0])

        operacao = estoque.objects.get(produto=nomeProduto)
        operacao.quantidade -= qtd
        operacao.save()

        itens.pop(0)
        quantidades.pop(0)

        i = i - 1


def novoUsuario(nome):
    
    """
    ->
    :return:
    """

    dir = f'app/static/archive/{nome}'       
    os.mkdir(dir)
  

@login_required
def cart(request):

    """
    ->
    :return:
    """

    if request.method == 'POST':

        nomeCliente = request.POST.get('nomeCliente-form')
        valorTotal = request.POST.get('valorTotal-form').replace(',','.')
        tipoPgto = request.POST.get(['tipoPagamento-form'][0])
        valorDesconto = request.POST.get('valorDesconto-form').replace(',','.')
        valorTroco = request.POST.get('valorTroco-form').replace(',','.')
        listaItens = request.POST.get('item-local').split(',')
        listaValores = request.POST.get('valor-local').split(',')
        listaQuantidades = request.POST.get('qtd-local').split(',')

        valorTotal = (float(valorTotal) - float(valorDesconto))

        removeItens = listaItens
        removeQtd = listaQuantidades

        opEstoque(removeItens, removeQtd)

        listaItens = request.POST.get('item-local').split(',')
        listaValores = request.POST.get('valor-local').split(',')
        listaQuantidades = request.POST.get('qtd-local').split(',')

        listaRecibo = []
        
        listaRecibo.append(listaItens)
        listaRecibo.append(listaValores)
        listaRecibo.append(listaQuantidades)

        if tipoPgto != 'dinheiro':
            valorTroco = '0'

        if valorDesconto == '':
            valorDesconto = '0'

        agora = (str(datetime.now())).replace(' ', '').replace(':','-').replace('.','-')
        nomeRecibo = f'recibo{agora}.pdf'
        
        usuario = request.user

        if os.path.isdir(f'app/static/archive/{usuario}'):
            pass
        else:
            novoUsuario(usuario)
        
        caminho = Path(f'static/archive/{usuario}')
        salvoEm = f'{caminho}/' + f'{nomeRecibo}'  
       
        f = vendas(cliente=nomeCliente, valor=valorTotal, pagamento=tipoPgto, comprovante=salvoEm, recibo=nomeRecibo, usuario=usuario)

        pdf(nomeRecibo, usuario, listaRecibo, valorDesconto, valorTotal, tipoPgto, valorTroco)

        f.save()

        return redirect('/buy')
    
    else:
        pass

    return render(request, 'app/cart.html')  


@login_required
def records(request):

    """
    ->
    :return:
    """
    
    registros = pessoas.objects.all().filter(usuario=request.user)

    return render(request, 'app/records.html', {'registros': registros})


@login_required
def products(request):

    """
    ->
    :return:
    """

    pesquisa = request.GET.get('procurar')

    if pesquisa:
        produtos = estoque.objects.filter(produto__icontains=pesquisa, usuario=request.user)

    else:
        produtos = estoque.objects.all().filter(usuario=request.user)

    return render(request, 'app/products.html', {'produtos': produtos})  


@login_required
def stock(request, id):

    """
    ->
    :return:
    """

    estoques = get_object_or_404(estoque, pk=id)

    return render(request, 'app/stock.html', {'estoques': estoques})


@login_required
def people(request, id):

    """
    ->
    :return:
    """

    pessoa = get_object_or_404(pessoas, pk=id).filter(usuario=request.user)

    return render(request, 'app/people.html', {'pessoa': pessoa})

    
class register(generic.CreateView):

    """
    ->
    :return:
    """

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def tratamento(numero=0):
    
    """
    -> Funcao para tratar o numero de acordo com o padrao do local
    :param numero: Numero para ser formatado
    :return: Numero formatado
    """

    locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8") 
    
    return locale.currency(numero, grouping=True)


def pdf(nome, usuario, vendas, desconto, total, pagamento, troco):
    
    """
    ->
    :return:
    """
       
    itens = vendas[0]
    qtd = vendas[2]
    valor = vendas[1]

    quantidade = len(itens)
    totalItens = 0
    
    for i in qtd:
        totalItens = totalItens + int(i)

    estilo = getSampleStyleSheet()
    centro = estilo['Normal']
    centro.alignment = 1

    recibo = []

    cabecalho = ['--------------------------------------------------------------',
    'EMPRESA ABC LTDA',
    'RUA NADA, 1000',
    'SAO PAULO - SP',
    '--------------------------------------------------------------',
    'CNPJ 00.000.000/0000-00',
    '--------------------------------------------------------------',
    'EXTRATO N. 0001',
    'RECIBO DE COMPRA E VENDA',
    '00/00/0000',
    '--------------------------------------------------------------',
    'ITEM | QTD | VALOR R$',
    '--------------------------------------------------------------',
    '&nbsp;']

    conteudo = []

    i = len(itens)
    while i > 0:
        conteudo.append(f'&nbsp;{itens[0]}&nbsp;&nbsp;&nbsp;({qtd[0]})&nbsp;&nbsp;&nbsp;{tratamento(float(valor[0]))}')
        itens.pop(0)
        qtd.pop(0)
        valor.pop(0)
        i = i - 1
    
    desconto = desconto.replace(',','.')
    troco = troco.replace(',','.')

    corpo = ['&nbsp;',
    f'TOTAL ITENS:&nbsp;&nbsp;{totalItens}',
    f'DESCONTO:&nbsp;&nbsp;{tratamento(float(desconto))}',
    f'TOTAL:&nbsp;&nbsp;{tratamento(float(total))}',
    f'PAGAMENTO:&nbsp;&nbsp;{pagamento.upper()}',
    f'TROCO:&nbsp;&nbsp;{tratamento(float(troco))}',
    '&nbsp;']

    rodape = ['--------------------------------------------------------------',
    'VOLTE SEMPRE !!',
    '--------------------------------------------------------------']

    # cabecalho
    i = len(cabecalho)
    while i > 0:
        recibo.append(Paragraph(cabecalho[0], centro))
        cabecalho.pop(0)
        i = i - 1
    # cabecalho

    # conteudo
    i = len(conteudo)
    while i > 0:
        recibo.append(Paragraph(conteudo[0]))
        conteudo.pop(0)
        i = i - 1
    #conteudo

    # corpo
    i = len(corpo)
    while i > 0:
        recibo.append(Paragraph(corpo[0]))
        corpo.pop(0)
        i = i - 1
    # corpo

    # rodape
    i = len(rodape)
    while i > 0:
        recibo.append(Paragraph(rodape[0], centro))
        rodape.pop(0)
        i = i - 1
    #rodape
    
    caminho = Path(f'app/static/archive/{usuario}')
    salvarEm = f'{caminho}/' + f'{nome}'

    pdf = SimpleDocTemplate(salvarEm, pagesize=(226, ((len(recibo) * 14) - 18)), leftMargin=2.2, rightMargin=2.2, topMargin=10, bottomMargin=10)

    pdf.build(recibo)

    
