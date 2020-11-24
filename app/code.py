# -*- coding: utf-8 -*-

'''
Criado em 09/2020
@Autor: Paulo https://github.com/alpdias
'''

# formularios e modelos
from .models import estoque, empresas

# bibliotecas externas
import os
import locale
import smtplib
from pathlib import Path
from datetime import date
from datetime import datetime

# tratamento de e-mail
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# tratamento de PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def opEstoque(itens, quantidades):
            
    """
    -> Realiza a operaçao de 'delete' e mudança de estado do objeto dentro do model 'estoque'
    """

    i = len(itens)

    while i > 0:

        nomeProduto = itens[0]
        qtd = int(quantidades[0])

        operacao = estoque.objects.filter(produto=nomeProduto).get()
        operacao.quantidade -= qtd # diminui o valor do objeto dentro do DB
        operacao.save() # salva a operaçao

        itens.pop(0)
        quantidades.pop(0)

        i = i - 1

        estado = operacao.quantidade

        if estado == 0:
            operacao.status = 'esgotado' # muda o 'status' do objeto no DB
            operacao.save()

        else:
            pass
          
          
def novoUsuario(nome):

    """
    -> Criar um novo diretorio para o usuario\
    \n:return: Novo diretorio de arquivo em 'static'
    """

    dir = f'app/static/archive/{nome}'       
    os.mkdir(dir)
    

def enviarRecibo(recibo, usuario):
    
    """
    -> Enviar um e-mail a partir do servidor SMTP especifico de cada usuario
    """
    
    empresa = empresas.objects.filter(usuario=usuario).get() # dados do servidor do usuario
    
    # configuraçoes do servidor -->
    porta = empresa.porta
    smtpServidor = empresa.servidor
    login = empresa.usuarioServidor
    pwd = empresa.senhaServidor
    # configuraçoes do servidor <--

    # especificoes do e-mail -->
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

    encoders.encode_base64(email) # codificao do anexo do e-mail

    email.add_header(
        'Content-Disposition',
        f'attachment; filename={"recibo.pdf"}',
    ) # anexo ao e-mail

    mensagem.attach(email)
    texto = mensagem.as_string()
     # especificoes do e-mail <--
    
    with smtplib.SMTP(smtpServidor, porta) as server: # envio do e-mail pelo servidor

        server.starttls()
        server.login(login, pwd)
        server.sendmail(de, para, texto)

        server.quit()


def tratamento(numero=0):
    
    """
    -> Funcao para tratar o numero de acordo com o padrao do local\
    \n:param numero: Numero para ser formatado\
    \n:return: Numero formatado
    """

    locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8") # tratamento de numero no padrao brasileiro
    
    return locale.currency(numero, grouping=True)


def pdf(nome, usuario, vendas, desconto, total, pagamento, troco, cpf, extrato):
    
    """
    -> Cria um arquivo de pdf\
    \n:return: Retorna um arquivo de pdf para envio
    """
    
    empresa = empresas.objects.filter(usuario=usuario).get() 
    
    # datas -->
    data = date.today()
    d = data.day
    m = data.month
    a = data.year
    atual = f'{d}/{m}/{a}'
    # datas <--
    
    # listas -->
    itens = vendas[0]
    qtd = vendas[2]
    valor = vendas[1]
    # listas -->
    
    totalItens = 0
    
    for i in qtd:
        totalItens = totalItens + int(i)

    estilo = getSampleStyleSheet() # estilos do criador de pdf
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

    # cabecalho -->
    i = len(cabecalho)

    while i > 0:

        recibo.append(Paragraph(cabecalho[0], centro))
        cabecalho.pop(0)

        i = i - 1
    # cabecalho <--

    # conteudo -->
    i = len(conteudo)

    while i > 0:

        recibo.append(Paragraph(f'&nbsp;&nbsp;&nbsp;{conteudo[0]}'))
        conteudo.pop(0)

        i = i - 1
    #conteudo <--

    # corpo -->
    i = len(corpo)

    while i > 0:

        recibo.append(Paragraph(corpo[0]))
        corpo.pop(0)

        i = i - 1
    # corpo <--

    # rodape -->
    i = len(rodape)

    while i > 0:

        recibo.append(Paragraph(rodape[0], centro))
        rodape.pop(0)

        i = i - 1
    #rodape <--
    
    caminho = Path(f'app/static/archive/{usuario}')
    salvarEm = f'{caminho}/' + f'{nome}'

    pdf = SimpleDocTemplate(
        salvarEm, 
        pagesize=(226, ((len(recibo) * 14) - 18)), 
        leftMargin=1.5, 
        rightMargin=1.5, 
        topMargin=10, 
        bottomMargin=10
    ) # cria e configura o pdf

    pdf.build(recibo) # salva o pdf
    
    enviarRecibo(salvarEm, usuario) # envia o pdf

  