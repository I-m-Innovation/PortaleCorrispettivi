# Generated by Django 5.1 on 2024-08-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortaleCorrispettivi', '0008_datimensili_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='linkportale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portale', models.CharField(default='-', max_length=200, verbose_name='Nome portale')),
                ('tag', models.CharField(default='-', max_length=50, verbose_name='tag portale')),
                ('link', models.CharField(default='-', max_length=250, verbose_name='link-portale')),
            ],
            options={
                'verbose_name': 'Link Portale',
                'verbose_name_plural': 'Link Portali',
            },
        ),
    ]
