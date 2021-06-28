# Generated by Django 3.2.4 on 2021-06-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=100)),
                ('ano', models.IntegerField(max_length=4)),
                ('placa', models.CharField(max_length=10, unique=True)),
                ('cor', models.CharField(max_length=100)),
                ('chassi', models.CharField(max_length=50, unique=True)),
                ('data_compra', models.DateField(auto_now_add=True)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_venda', models.FloatField()),
                ('data_compra', models.DateField(auto_now_add=True)),
                ('comisao', models.FloatField()),
                ('lucro', models.FloatField()),
            ],
        ),
    ]