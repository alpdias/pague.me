from django.test import TestCase

# Create your tests here.

from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def pdf(nomeRecibo, listaVenda, totalVenda, pagamentoTipo, valorTroco):
    
    item = listaVenda[0]
    quantidade = listaVenda[2]
    valor = listaVenda[1]

    qtd = len(item)
    total = totalVenda
    pagamento = pagamentoTipo.upper()
    troco = valorTroco
    
    caminho = Path('app/static/archive')
    salvarEm = f'{caminho}/' + f'{nomeRecibo}'

    pdf = SimpleDocTemplate(salvarEm, pagesize=(256, (400 + (qtd * 14))), leftMargin=2.2, rightMargin=2.2, topMargin=10, bottomMargin=10)

    styles = getSampleStyleSheet()

    recibo = []

    conteudo =['-----------------------------------------------------------------------', 'EMPRESA ABC LTDA', 'RUA NADA, 1000', 'SAO PAULO - SP',
    '-----------------------------------------------------------------------',
    'CNPJ 00.000.000/0000-00',
    '-----------------------------------------------------------------------',
    'EXTRATO N. 0001', 'RECIBO DE COMPRA E VENDA', '00/00/0000', '-----------------------------------------------------------------------', 'ITEM | QTD | VALOR R$', '-----------------------------------------------------------------------', '-----------------------------------------------------------------------', 'VOLTE SEMPRE !!', '-----------------------------------------------------------------------']
    
    i = 16
    while i > 0:
      recibo.append(Paragraph(conteudo[0], styles["Normal"]))
      conteudo.pop(0)
      i = i - 1

    pdf.build(recibo)
    

valorTotal = 100
tipoPgto = 'dinheiro'
valorTroco = 20
listaItens = ['paralelepipedoooooooooooooooooooooooooooooooooooooo', 'pasteloooooooooooooooooooooooooooooooooooooooooooooooooooooooooo', 'queijooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo']
listaValores = [1.000,120,350]
listaQuantidades = [2,3,1]

listaRecibo = []

listaRecibo.append(listaItens)
listaRecibo.append(listaValores)
listaRecibo.append(listaQuantidades)
nomeRecibo = 'recibo.pdf'

item = listaRecibo[0]

pdf(nomeRecibo, listaRecibo, valorTotal, tipoPgto, valorTroco)
