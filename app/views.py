# -*- coding: utf-8 -*-

'''
Criado em 09/2020
@Autor: Paulo https://github.com/alpdias
'''

# bibliotecas Django
from django.views import generic
from django.conf import settings
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# formularios e modelos
from .forms import pessoasForm, estoqueForm, vendasForm
from .models import pessoas, estoque, vendas, empresas

# bibliotecas externas
import os
from .code import *
from pathlib import Path

# Create your views here.

def home(request):

    """
    -> Renderiza a pagina 'home.html'\
    \n:return: Retorna a pagina 'home.html'
    """
    
    return render(request, 'app/home.html')


def about(request):

    """
    -> Renderiza a pagina 'about.html'\
    \n:return: Retorna a pagian 'about.html'
    """
    
    return render(request, 'app/about.html')


def contact(request):

    """
    -> Renderiza a pagina 'contact.html'\
    \n:return: Retorna a pagina 'contact.html'
    """
    
    return render(request, 'app/contact.html')


@login_required
def dashboard(request):

    """
    -> Renderiza a pagina 'dashboard.html'\
    \n:return: Retorna a pagina 'dashboard.html'
    """
    
    return render(request, 'app/dashboard.html')


@login_required
def buy(request):

    """
    -> Renderiza a pagina 'buy.html' e os objetos do model 'vendas'\
    \n:return: Retorna a pagina 'buy.html' com os objetos do model 'vendas' de cada usuario logado
    """
    
    listaVendas = vendas.objects.all().filter(usuario=request.user) # requisicao do objeto com filtro de usuario

    paginas = Paginator(listaVendas, 8) # paginacao do conteudo exibido
    pagina = request.GET.get('page')

    venda = paginas.get_page(pagina)

    return render(request, 'app/buy.html', {'venda': venda})  


@login_required
def sales(request, id):

    """
    -> Renderiza a pagina 'sales.html' com as opçoes de ediçao do model 'vendas'\
    \n:return: Retorna a pagina 'sales.html' de acordo com o  'id' especifico do objeto para ediçao
    """
    
    venda = get_object_or_404(vendas, pk=id) # requisacao do objeto a partir do ID

    form = vendasForm(instance=venda) # pre popular dados no formulario
    
    if request.method == 'POST':
        excluir = request.POST.get('excluir-venda')
        
        if (excluir == 'excluir'):
            venda.delete() # remove o objeto do DB
            
            return redirect('/buy') # redireciona a pagina
        
        else:
            form = vendasForm(request.POST, instance=venda)
            
            if form.is_valid: # verificar a validade do formulario
                form.save()

                return redirect('/buy')
            
            else:
                return render(request, 'app/sales.html', {'form': form, 'venda': venda})
        
    else:
        return render(request, 'app/sales.html', {'form': form, 'venda': venda})  
    

@login_required
def cart(request):

    """
    -> Renderiza a pagina 'cart.html' e realiza o processo de requisiçao no estoque
    \n:return: Retorna o registro de uma nova venda e envia o recibo
    """

    if request.method == 'POST':

        # requisiçoes dentro do metodo POST  -->
        cpfCliente = request.POST.get('cpfCliente-form') 
        valorTotal = request.POST.get('valorTotal-form').replace('.','').replace(',','.')
        tipoPgto = request.POST.get(['tipoPagamento-form'][0])
        valorDesconto = request.POST.get('valorDesconto-form').replace(',','.')
        valorTroco = request.POST.get('valorTroco-form').replace(',','.')
        listaItens = request.POST.get('item-local').split(',')
        listaValores = request.POST.get('valor-local').split(',')
        listaQuantidades = request.POST.get('qtd-local').split(',')
        # requisiçoes dentro do metodo POST <--

        # tratamento de erro -->
        if tipoPgto != 'dinheiro':
            valorTroco = '0'
        
        if valorTroco == '':
            valorTroco = '0,00'

        if valorDesconto == '':
            valorDesconto = '0'
        
        if cpfCliente == '':
            cpfCliente = 'Não Identificado'
        # tratamento de erro <--
        
        valorTotal = (float(valorTotal) - float(valorDesconto)) # calculo do valor total

        removeItens = listaItens
        removeQtd = listaQuantidades
        code.opEstoque(removeItens, removeQtd)

        # tratamento de erro -->
        listaItens = request.POST.get('item-local').split(',')
        listaValores = request.POST.get('valor-local').split(',')
        listaQuantidades = request.POST.get('qtd-local').split(',')
        # tratamento de erro <--

        # atribuicao das listas -->
        listaRecibo = []
        listaRecibo.append(listaItens)
        listaRecibo.append(listaValores)
        listaRecibo.append(listaQuantidades)
        # atribuicao das listas <--

        agora = (str(datetime.now())).replace(' ', '').replace(':','-').replace('.','-')
        nomeRecibo = f'recibo{agora}.pdf'

        usuario = request.user # obtem o usuario atual

        if os.path.isdir(f'app/static/archive/{usuario}'): # verifica a existencia do diretorio de arquivos do usuario
            pass
        
        else:
            code.novoUsuario(usuario) 
        
        caminho = Path(f'static/archive/{usuario}') # caminho do diretorio
        salvoEm = f'{caminho}/' + f'{nomeRecibo}'  # caminho do arquivo salvo

        f = vendas(
            cpf=cpfCliente, 
            valor=valorTotal, 
            pagamento=tipoPgto, 
            comprovante=salvoEm, 
            recibo=nomeRecibo, 
            usuario=usuario
        )  # cria uma novo objeto no model 'vendas'

        f.save()
        
        extrato = vendas.objects.filter(recibo=nomeRecibo).get() # resgata o numero de ID da objeto criado anteriormente
        nExtrato = extrato.id
        
        code.pdf(
            nomeRecibo, 
            usuario, 
            listaRecibo, 
            valorDesconto, 
            valorTotal, 
            tipoPgto, 
            valorTroco, 
            cpfCliente, 
            nExtrato
        )

        return redirect('/buy')
    
    else:
        pass

    return render(request, 'app/cart.html')  


@login_required
def records(request):

    """
    -> Renderiza a pagina 'records.html' e os objetos do model 'pessoas'\
    \n:return: Retorna a pagina 'records.html' com os objetos do model 'pessoas' de cada usuario logado
    """
    
    listaRegistros = pessoas.objects.all().filter(usuario=request.user)

    paginas = Paginator(listaRegistros, 8)
    pagina = request.GET.get('page')

    registros = paginas.get_page(pagina)

    return render(request, 'app/records.html', {'registros': registros})


@login_required
def products(request):

    """
    -> Renderiza a pagina 'products.html' e os objetos do model 'estoque'\
    \n:return: Retorna a pagina 'products.html' com os objetos do model 'estoque' de cada usuario e a requisiçao de pesquisa
    """

    pesquisa = request.GET.get('procurar')

    if pesquisa:
        produtos = estoque.objects.filter(produto__icontains=pesquisa, usuario=request.user) # retorna o valor da pesquisa contido na requisicao

    else:
        listaProdutos = estoque.objects.all().filter(usuario=request.user)

        paginas = Paginator(listaProdutos, 8)
        pagina = request.GET.get('page')

        produtos = paginas.get_page(pagina)

    return render(request, 'app/products.html', {'produtos': produtos})  


@login_required
def stock(request, id):

    """
    -> Renderiza a pagina 'stock.html' e os objetos do model 'estoque' de acordo com o 'id'\
    \n:return: Retorna a pagina 'stock.html' de acordo com o  'id' especifico do objeto para ediçao
    """

    estoques = get_object_or_404(estoque, pk=id)
    estado = estoques.quantidade
        
    if estado == 0: # altera o 'status' do objeto do model 'estoque'
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
    -> Renderiza a pagina 'edit.html' e os objetos do model 'estoque' de acordo com o 'id'\
    \n:return: Retorna a pagina 'edit.html' de acordo com o 'id' especifico do objeto para ediçao
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
    -> Renderiza a pagina 'newp.html' para adiçao de um novo objeto no model 'estoque'\
    \n:return: Retorna a pagina 'newp.html' para a adiçao de novo objeto no model 'estoque'
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
    -> Rederiza a pagina 'people.html' e os objetos do model 'pessoas' de acordo com o 'id'\
    \n:return: Retorna a pagina 'people.html' de acordo com o 'id' especifico do objeto para vizualizar os dados
    """

    pessoa = get_object_or_404(pessoas, pk=id)

    return render(request, 'app/people.html', {'pessoa': pessoa})


@login_required
def newc(request):

    """
    -> Renderiza a pagina 'newc.html' para adiçao de um novo objeto no model 'pessoas'\
    \n:return: Retorna a pagina 'newc.html' para a adiçao de novo objeto no model 'pessoas'
    """
    
    if request.method == 'POST':
        form = pessoasForm(request.POST)
        
        if form.is_valid():
            pessoa = form.save(commit=False) # não salva o objeto direto, podendo adicionar mais dados
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

