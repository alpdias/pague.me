from django import forms
from .models import pessoas, estoque, vendas

class pessoasForm(forms.ModelForm):
  
  class Meta:
    model = pessoas
    fields = ('nome', 'telefone', 'email', 'cpf', 'endereco', 'observacao', 'status')  
    
    
class estoqueForm(forms.ModelForm):
  
  class Meta:
    model = estoque
    fields = ('produto', 'preco', 'custo', 'quantidade', 'descricao', 'fornecedor', 'status')
    
    
class vendasForm(forms.ModelForm):
  
  class Meta:
    model = vendas
    fields = ('cliente', 'valor', 'pagamento', 'comprovante', 'recibo', 'status')  
    
