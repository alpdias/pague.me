# Generated by Django 3.1.2 on 2020-10-20 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20201020_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='cliente',
            field=models.CharField(max_length=255, verbose_name='Cliente'),
        ),
    ]
