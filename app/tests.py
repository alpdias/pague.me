#from django.test import TestCase

# Create your tests here.

listaItens = []
totalItens = 0
totalValor = 0
formaPagamento = 'DINHEIRO'
valorPagamento = 0
valorTroco = 0

layout01 = '-'
layout02 = ' '

recibo = f'\
\n{layout01 * 40}\
\nEMPRESA ABC LTDA\
\nRUA NADA, 1000\
\nSAO PAULO - SP\
\n\
\nCNPJ 00.000.000/0000-00\
\n{layout01 * 40}\
\nEXTRATO N. 0001\
\nRECIBO DE COMPRA E VENDA\
\n{layout01 * 40}\
\n\
\n{listaItens}\
\n\
\nTOTAL ITENS:{layout02 * 19}{totalItens}\
\nTOTAL:{layout02 * 25}{totalValor}\
\nPAGAMENTO:{layout02}{formaPagamento}{layout02 * 12}{valorPagamento}\
\nTROCO:{layout02 * 25}{valorTroco}\
\n\
\n{layout01 * 40}\
\n\
\nVOLTE SEMPRE !!\
\n\
\n{layout01 * 40}'

print(recibo)
