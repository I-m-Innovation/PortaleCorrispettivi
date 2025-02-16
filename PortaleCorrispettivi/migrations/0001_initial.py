# Generated by Django 5.1 on 2024-08-13 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impianto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(help_text="Identifica l'impianto", max_length=50, unique=True, verbose_name='Nickname')),
                ('societa', models.CharField(blank=True, help_text='Fiscale impianto', max_length=150, null=True, verbose_name='Società')),
                ('nome_impianto', models.CharField(help_text="Nome dell'impianto", max_length=150, verbose_name='Nome')),
                ('tag', models.CharField(help_text='Tag di abbreviazione', max_length=10, verbose_name='Tag')),
                ('tipo', models.CharField(help_text="Tipologia dell'impianto elettrico", max_length=150, verbose_name='Tipo')),
                ('lat', models.FloatField(blank=True, help_text='Latitudine', null=True, verbose_name='Latitudine')),
                ('lon', models.FloatField(blank=True, help_text='Longitudine', null=True, verbose_name='Longitudine')),
                ('localita', models.CharField(blank=True, help_text='Località', max_length=150, null=True, verbose_name='Località')),
                ('potenza_installata', models.FloatField(blank=True, help_text='Potenza installata', null=True, verbose_name='Potenza')),
                ('unita_misura', models.CharField(blank=True, help_text='Unita misura portata (mc/s o l/s)', max_length=150, null=True, verbose_name='Unita misura')),
                ('portata_concessione', models.FloatField(blank=True, help_text='Portata di concessione', null=True, verbose_name='Portata')),
                ('salto', models.FloatField(blank=True, help_text='Salto impianto', null=True, verbose_name='Salto')),
                ('potenza_business_plan', models.FloatField(blank=True, default=0, help_text='Potenza da Business Plan', null=True, verbose_name='Potenza Business Plan')),
                ('inizio_esercizio', models.DateField(blank=True, help_text='Data inizio esercizio', null=True, verbose_name='Entrata in esercizio')),
                ('lettura_dati', models.CharField(blank=True, help_text='Tipo lettura dati impianti', max_length=50, null=True, verbose_name='Lettura dati')),
                ('proprieta', models.BooleanField(default=False, help_text="Indica se l'impianto è di propietà Zilio", verbose_name='Proprietà')),
            ],
            options={
                'verbose_name': 'Impianto',
                'verbose_name_plural': 'Impianti',
            },
        ),
    ]
