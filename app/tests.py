#from django.test import TestCase

# Create your tests here.

from reportlab.pdfgen import canvas

pdf = canvas.Canvas('recibo.pdf', pagesize=(256, 400))

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
'TOTAL ITENS:',
'TOTAL:',
'PAGAMENTO:',
'TROCO:',
'',
'------------------------------------------------------------',
'',
'VOLTE SEMPRE !!',
'',
'------------------------------------------------------------']

formato = 370

i = 14

while i > 0:
  pdf.drawCentredString(128, (formato - 14), recibo[0])
  recibo.pop(0)
  formato = formato - 14
  i = i - 1

i = 5

while i > 0:
  pdf.drawString(16, (formato - 14), recibo[0])
  recibo.pop(0)
  formato = formato - 14
  i = i - 1

i = 5

while i > 0:
  pdf.drawCentredString(128, (formato - 14), recibo[0])
  recibo.pop(0)
  formato = formato - 14
  i = i - 1

pdf.save()
