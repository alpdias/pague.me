#from django.test import TestCase

# Create your tests here.

from reportlab.pdfgen import canvas

item = ['item 00', 'item 01', 'item 02', 'item 03', 'item 04', 'item 05']
quantidade = ['02', '01', '05', '08', '11', '15']
valor = [12, 50, 25, 90, 10, 2]

qtd = len(item)

pdf = canvas.Canvas('recibo.pdf', pagesize=(256, (400 + (qtd * 14))))

recibo = ['------------------------------------------------------------',
'EMPRESA ABC LTDA',
'RUA NADA, 1000',
'SAO PAULO - SP',
'------------------------------------------------------------',
'CNPJ 00.000.000/0000-00',
'------------------------------------------------------------',
'EXTRATO N. 0001',
'RECIBO DE COMPRA E VENDA',
'00/00/0000',
'------------------------------------------------------------',
'',
'ITEM | QTD | VALOR R$',
'',
'',
f'TOTAL ITENS: {qtd}',
'TOTAL:',
'PAGAMENTO:',
'TROCO:',
'',
'------------------------------------------------------------',
'',
'VOLTE SEMPRE !!',
'',
'------------------------------------------------------------']

formato = (380 + (qtd * 14))

#cabecalho
i = 14

while i > 0:
    pdf.drawCentredString(128, (formato - 14), recibo[0])
    recibo.pop(0)
    formato = formato - 14
    i = i - 1
#cabecalho

#itens
i = qtd

while i > 0:
    pdf.drawString(16, (formato - 14), f'{item[0]}  |  {quantidade[0]}  |  {valor[0]}')
    item.pop(0)
    quantidade.pop(0)
    valor.pop(0)
    formato = formato - 14
    i = i - 1
#itens

#totalizador
i = 6

while i > 0:
    pdf.drawString(16, (formato - 14), recibo[0])
    recibo.pop(0)
    formato = formato - 14
    i = i - 1
#totalizador

#rodape
i = 5

while i > 0:
    pdf.drawCentredString(128, (formato - 14), recibo[0])
    recibo.pop(0)
    formato = formato - 14
    i = i - 1
#rodape

pdf.save()
