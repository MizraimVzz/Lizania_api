# Generated by Django 4.2.6 on 2023-11-30 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ap_materno',
            field=models.CharField(default='Apellido Materno', max_length=50),
        ),
    ]
