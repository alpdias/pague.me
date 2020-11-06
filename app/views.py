# -*- coding: utf-8 -*-

'''
Criado em 09/2020
@Autor: Paulo https://github.com/alpdias
'''

from django.views import generic
from django.conf import settings
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import pessoasForm, estoqueForm, vendasForm
from .models import pessoas, estoque, vendas, empresas
import os
import locale
import smtplib
from pathlib import Path
from datetime import date
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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

    paginas = Paginator(listaVendas, 6)
    pagina = request.GET.get('page')

    venda = paginas.get_page(pagina)

    return render(request, 'app/buy.html', {'venda': venda})  


@login_required
def sales(request, id):

    """
    ->
    :return:
    """
    
    venda = get_object_or_404(vendas, pk=id)

    form = vendasForm(instance=venda)
    
    if request.method == 'POST':

        excluir = request.POST.get('excluir-venda')
        
        if (excluir == 'excluir'):

            venda.delete()
            return redirect('/buy')
        
        else:

            form = vendasForm(request.POST, instance=venda)
            
            if form.is_valid:

                form.save()

                return redirect('/buy')
            
            else:

                return render(request, 'app/sales.html', {'form': form, 'venda': venda})
        
    else:

        return render(request, 'app/sales.html', {'form': form, 'venda': venda})  


def opEstoque(itens, quantidades):
    
    """
    ->
    :return:
    """

    i = len(itens)

    while i > 0:

        nomeProduto = itens[0]
        qtd = int(quantidades[0])

        operacao = estoque.objects.filter(produto=nomeProduto).get()
        operacao.quantidade -= qtd
        operacao.save()

        itens.pop(0)
        quantidades.pop(0)

        i = i - 1
    
        estado = operacao.quantidade
        
        if estado == 0:

            operacao.status = 'esgotado'
            operacao.save()

        else:
            pass
    

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

        cpfCliente = request.POST.get('cpfCliente-form')
        valorTotal = request.POST.get('valorTotal-form').replace('.','').replace(',','.')
        tipoPgto = request.POST.get(['tipoPagamento-form'][0])
        valorDesconto = request.POST.get('valorDesconto-form').replace(',','.')
        valorTroco = request.POST.get('valorTroco-form').replace(',','.')
        listaItens = request.POST.get('item-local').split(',')
        listaValores = request.POST.get('valor-local').split(',')
        listaQuantidades = request.POST.get('qtd-local').split(',')

        if tipoPgto != 'dinheiro':
            valorTroco = '0'
        
        if valorTroco == '':
            valorTroco = '0,00'

        if valorDesconto == '':
            valorDesconto = '0'
        
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

        agora = (str(datetime.now())).replace(' ', '').replace(':','-').replace('.','-')

        nomeRecibo = f'recibo{agora}.pdf'

        usuario = request.user

        if os.path.isdir(f'app/static/archive/{usuario}'):
            pass
        
        else:

            novoUsuario(usuario)
        
        caminho = Path(f'static/archive/{usuario}')
        salvoEm = f'{caminho}/' + f'{nomeRecibo}'  

        f = vendas(cpf=cpfCliente, valor=valorTotal, pagamento=tipoPgto, comprovante=salvoEm, recibo=nomeRecibo, usuario=usuario)
        f.save()
        
        extrato = vendas.objects.filter(recibo=nomeRecibo).get()
        nExtrato = extrato.id

        if cpfCliente == '':
            cpfCliente = 'Não Identificado'
        
        pdf(nomeRecibo, usuario, listaRecibo, valorDesconto, valorTotal, tipoPgto, valorTroco, cpfCliente, nExtrato)

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
    
    listaRegistros = pessoas.objects.all().filter(usuario=request.user)

    paginas = Paginator(listaRegistros, 8)
    pagina = request.GET.get('page')

    registros = paginas.get_page(pagina)

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

        listaProdutos = estoque.objects.all().filter(usuario=request.user)

        paginas = Paginator(listaProdutos, 8)
        pagina = request.GET.get('page')

        produtos = paginas.get_page(pagina)

    return render(request, 'app/products.html', {'produtos': produtos})  


@login_required
def stock(request, id):

    """
    ->
    :return:
    """

    estoques = get_object_or_404(estoque, pk=id)

    estado = estoques.quantidade
        
    if estado == 0:

        estoques.status = 'esgotado'
        estoques.save()

    elif estado > 0:
    
        estoques.status = 'disponivel'
        estoques.save()

    else:
        pass

    return render(request, 'app/stock.html', {'estoques': estoques})


@login_required
def edit(request, id):

    """
    ->
    :return:
    """
    
    estoques = get_object_or_404(estoque, pk=id)

    form = estoqueForm(instance=estoques)
    
    if request.method == 'POST':

        excluir = request.POST.get('excluir-produto')
        
        if (excluir == 'excluir'):

            estoques.delete()
            return redirect('/products')

        form = estoqueForm(request.POST, instance=estoques)
        
        if form.is_valid:
            
            form.save()
            return redirect('/products')
        
        else:

            return render(request, 'app/edit.html', {'form': form, 'estoques': estoques})
        
    else:

        return render(request, 'app/edit.html', {'form': form, 'estoques': estoques}) 


@login_required
def newp(request):
    
    """
    ->
    :return:
    """
    
    if request.method == 'POST':

        form = estoqueForm(request.POST)
        
        if form.is_valid():

            produto = form.save(commit=False)
            produto.usuario = request.user
            produto.save()
            
            return redirect('/products')
            
    else:

        form = estoqueForm()

    return render(request, 'app/newp.html', {'form': form})


@login_required
def people(request, id):

    """
    ->
    :return:
    """

    pessoa = get_object_or_404(pessoas, pk=id)

    return render(request, 'app/people.html', {'pessoa': pessoa})


@login_required
def newc(request):

    """
    ->
    :return:
    """
    
    if request.method == 'POST':

        form = pessoasForm(request.POST)
        
        if form.is_valid():

            pessoa = form.save(commit=False)
            pessoa.usuario = request.user
            pessoa.save()
            
            return redirect('/records')
        
    else:

        form = pessoasForm()
    
    return render(request, 'app/newc.html', {'form': form})  


"""
class register(generic.CreateView):
    
    # view para registrar um novo usuario
    
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
"""

def enviarRecibo(recibo, usuario):
    
    """
    ->
    :return:
    """
    
    empresa = empresas.objects.filter(usuario=usuario).get()
    
    porta = empresa.porta
    smtpServidor = empresa.servidor
    login = empresa.usuarioServidor
    pwd = empresa.senhaServidor

    assunto = 'pague.me | nova venda realizada !!'
    de = empresa.email
    para = empresa.email

    mensagem = MIMEMultipart()

    mensagem['From'] = de
    mensagem['To'] = para
    mensagem['Subject'] = assunto

    corpo = 'Olá, você acaba de realizar uma nova venda e aqui está o seu recibo de venda!\
    \nhttp://pague-me.herokuapp.com/'
    mensagem.attach(MIMEText(corpo, "plain"))

    arquivo = recibo

    with open(arquivo, 'rb') as attachment:

        email = MIMEBase('application', 'octet-stream')
        email.set_payload(attachment.read())

    encoders.encode_base64(email)

    email.add_header(
        'Content-Disposition',
        f'attachment; filename={"recibo.pdf"}',
    )

    mensagem.attach(email)
    texto = mensagem.as_string()
    
    with smtplib.SMTP(smtpServidor, porta) as server:

        server.starttls()
        server.login(login, pwd)
        server.sendmail(de, para, texto)

        server.quit()


def tratamento(numero=0):
    
    """
    -> Funcao para tratar o numero de acordo com o padrao do local
    :param numero: Numero para ser formatado
    :return: Numero formatado
    """

    locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8") 
    
    return locale.currency(numero, grouping=True)


def pdf(nome, usuario, vendas, desconto, total, pagamento, troco, cpf, extrato):
    
    """
    ->
    :return:
    """
    
    empresa = empresas.objects.filter(usuario=usuario).get()
    
    data = date.today()
    d = data.day
    m = data.month
    a = data.year
    atual = f'{d}/{m}/{a}'
       
    itens = vendas[0]
    qtd = vendas[2]
    valor = vendas[1]
    totalItens = 0
    
    for i in qtd:

        totalItens = totalItens + int(i)

    estilo = getSampleStyleSheet()
    centro = estilo['Normal']
    centro.alignment = 1
    
    recibo = []

    cabecalho = ['--------------------------------------------------------------',
    f'{empresa.empresa}',
    f'{empresa.endereco}',
    f'{empresa.cidadeEstado}',
    '--------------------------------------------------------------',
    f'CNPJ:&nbsp;{empresa.cnpj}',
    '--------------------------------------------------------------',
    f'EXTRATO N. {extrato}',
    'RECIBO DE COMPRA E VENDA',
    f'{atual}',
    f'CLIENTE:&nbsp;&nbsp;{cpf}',             
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
    f'&nbsp;&nbsp;&nbsp;TOTAL ITENS:&nbsp;&nbsp;{totalItens}',
    f'&nbsp;&nbsp;&nbsp;DESCONTO:&nbsp;&nbsp;{tratamento(float(desconto))}',
    f'&nbsp;&nbsp;&nbsp;TOTAL:&nbsp;&nbsp;{tratamento(float(total))}',
    f'&nbsp;&nbsp;&nbsp;PAGAMENTO:&nbsp;&nbsp;{pagamento.upper()}',
    f'&nbsp;&nbsp;&nbsp;TROCO:&nbsp;&nbsp;{tratamento(float(troco))}',
    '&nbsp;']

    rodape = ['--------------------------------------------------------------',
    f'{empresa.frase}',
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

        recibo.append(Paragraph(f'&nbsp;&nbsp;&nbsp;{conteudo[0]}'))
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

    pdf = SimpleDocTemplate(salvarEm, pagesize=(226, ((len(recibo) * 14) - 18)), leftMargin=1.5, rightMargin=1.5, topMargin=10, bottomMargin=10)
    pdf.build(recibo)
    
    enviarRecibo(salvarEm, usuario)


    
