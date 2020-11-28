# Generated by Django 3.1.3 on 2020-11-27 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='vendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(default='Não Identificado', max_length=255, verbose_name='Cliente')),
                ('cpf', models.CharField(blank=True, max_length=14, verbose_name='CPF')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=999, verbose_name='Valor')),
                ('pagamento', models.CharField(max_length=8, verbose_name='Pagamento')),
                ('comprovante', models.FileField(upload_to='', verbose_name='Comprovante')),
                ('recibo', models.CharField(max_length=255, verbose_name='Recibo')),
                ('status', models.CharField(choices=[('aberto', 'aberto'), ('fechado', 'fechado')], default='aberto', max_length=7)),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'venda',
                'verbose_name_plural': 'vendas',
                'ordering': ['-criado'],
            },
        ),
        migrations.CreateModel(
            name='pessoas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True, verbose_name='Nome')),
                ('telefone', models.CharField(blank=True, max_length=15, verbose_name='Telefone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('cpf', models.CharField(blank=True, max_length=14, verbose_name='CPF')),
                ('endereco', models.CharField(blank=True, max_length=255, verbose_name='Endereço')),
                ('observacao', models.CharField(blank=True, max_length=255, verbose_name='Observações')),
                ('status', models.CharField(choices=[('ativo', 'ativo'), ('inativo', 'inativo')], max_length=7)),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'cadastro',
                'verbose_name_plural': 'cadastros',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=255, unique=True, verbose_name='Produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=999, verbose_name='Preço')),
                ('custo', models.DecimalField(decimal_places=2, max_digits=999, verbose_name='Custo')),
                ('quantidade', models.IntegerField(blank=True, default=0, verbose_name='Quantidade')),
                ('aviso', models.IntegerField(blank=True, default=0, verbose_name='Aviso')),
                ('descricao', models.CharField(blank=True, max_length=255, verbose_name='Descrição')),
                ('fornecedor', models.CharField(blank=True, max_length=255, verbose_name='Fornecedor')),
                ('codigo', models.CharField(default='Lk4jGG$g', max_length=8, unique=True, verbose_name='Código')),
                ('status', models.CharField(choices=[('disponivel', 'disponível'), ('esgotado', 'esgotado')], max_length=10)),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'produto',
                'verbose_name_plural': 'produtos',
                'ordering': ['produto'],
            },
        ),
        migrations.CreateModel(
            name='empresas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=255, verbose_name='Empresa')),
                ('cnpj', models.CharField(max_length=18, verbose_name='CNPJ')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('cidadeEstado', models.CharField(max_length=255, verbose_name='cidade/Estado')),
                ('observacao', models.CharField(blank=True, max_length=255, verbose_name='Observações')),
                ('frase', models.CharField(default='VOLTE SEMPRE!!', max_length=255, verbose_name='Rodapé')),
                ('porta', models.IntegerField(verbose_name='Porta')),
                ('servidor', models.CharField(max_length=255, verbose_name='Servidor')),
                ('usuarioServidor', models.CharField(max_length=255, verbose_name='Usuário')),
                ('senhaServidor', models.CharField(max_length=255, verbose_name='Senha')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('status', models.CharField(choices=[('ativo', 'ativo'), ('inativo', 'inativo')], max_length=7)),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'empresa',
                'verbose_name_plural': 'empresas',
                'ordering': ['empresa'],
            },
        ),
    ]
