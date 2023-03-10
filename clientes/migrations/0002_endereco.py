# Generated by Django 4.1.4 on 2023-01-21 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('pais', models.CharField(choices=[('BR', 'Brasil'), ('PT', 'Portugal'), ('FR', 'França')], max_length=2)),
            ],
        ),
    ]
