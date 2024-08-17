# Generated by Django 5.1 on 2024-08-16 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortaleCorrispettivi', '0004_diarioletture_cartella'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cashflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percorso', models.CharField(max_length=150, verbose_name='Percorso file')),
                ('impianto', models.ForeignKey(help_text='Relativo Impianto', on_delete=django.db.models.deletion.CASCADE, to='PortaleCorrispettivi.impianto', verbose_name='Impianto')),
            ],
            options={
                'verbose_name': 'File CashFlow',
                'verbose_name_plural': 'File CashFlow',
            },
        ),
        migrations.CreateModel(
            name='DatiMensili',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percorso', models.CharField(max_length=150, verbose_name='Percorso file')),
                ('impianto', models.ForeignKey(help_text='Relativo Impianto', on_delete=django.db.models.deletion.CASCADE, to='PortaleCorrispettivi.impianto', verbose_name='Impianto')),
            ],
            options={
                'verbose_name': 'File dati mensili',
                'verbose_name_plural': 'File dati mensili',
            },
        ),
    ]
