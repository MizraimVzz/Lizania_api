# Generated by Django 4.2.6 on 2023-12-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('horario', models.TimeField()),
                ('calle_y_numero', models.CharField(default=' ', max_length=255)),
                ('colonia', models.CharField(default=' ', max_length=255)),
                ('municipio', models.CharField(default=' ', max_length=255)),
                ('estado', models.CharField(default=' ', max_length=255)),
                ('codigo_postal', models.CharField(blank=True, max_length=10, null=True)),
                ('pais', models.CharField(default='México', max_length=255)),
            ],
        ),
    ]
