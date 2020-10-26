from django import forms
from .models import pessoas, estoque

class pessoasForm(forms.ModelForm):
  
  class Meta:
    model = pessoas
    fields = ('nome', 'telefone', 'email', 'cpf', 'endereco', 'observacao', 'status')  
    
    
class estoqueForm(forms.ModelForm):
  
  class Meta:
    model = estoque
    fields = ('produto', 'preco', 'custo', 'quantidade', 'descricao', 'fornecedor', 'status')
    
  
