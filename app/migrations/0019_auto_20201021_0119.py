# Generated by Django 3.1.2 on 2020-10-21 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20201021_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='comprovante',
            field=models.FileField(blank=True, upload_to='static/archve/pdf/', verbose_name='Comprovante'),
        ),
    ]
