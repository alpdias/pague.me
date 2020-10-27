from django import forms
from .models import pessoas, estoque, vendas
from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordField

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label = 'usuario',
        widget = forms.TextInput(attrs={'autofocus': True})
    )
    password = PasswordField(label = 'senha')

    
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
    
