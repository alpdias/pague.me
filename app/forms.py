# -*- coding: utf-8 -*-

'''
Criado em 09/2020
@Autor: Paulo https://github.com/alpdias
'''

from django import forms
from .models import pessoas, estoque, vendas
    
class pessoasForm(forms.ModelForm):
  
  class Meta:
    model = pessoas
    fields = ('nome', 'telefone', 'email', 'cpf', 'endereco', 'observacao', 'status')  
    
    
class estoqueForm(forms.ModelForm):
  
  class Meta:
    model = estoque
    fields = ('produto', 'preco', 'custo', 'quantidade', 'aviso', 'descricao', 'fornecedor', 'status')
    
    
class vendasForm(forms.ModelForm):
  
  class Meta:
    model = vendas
    fields = ('cliente', 'cpf', 'valor', 'pagamento', 'recibo', 'status')  
    
