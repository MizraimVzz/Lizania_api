# Generated by Django 4.2.6 on 2023-11-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
    ]
