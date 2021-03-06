# Generated by Django 3.0 on 2021-08-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación', verbose_name='creado')),
                ('modificado', models.DateTimeField(auto_now=True, help_text='Fecha de modificación', verbose_name='modificado')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
