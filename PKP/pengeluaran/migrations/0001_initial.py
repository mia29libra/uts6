# Generated by Django 5.0.4 on 2024-05-04 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pengeluaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_pengeluaran', models.CharField(max_length=50)),
                ('belanja_bulanan', models.CharField(max_length=50)),
                ('tagihan', models.CharField(max_length=50)),
                ('pembelian_lainnya', models.CharField(max_length=50)),
            ],
        ),
    ]
