# Generated by Django 4.2.6 on 2023-12-13 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='calle_y_numero',
            new_name='calle',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='pais',
        ),
        migrations.AddField(
            model_name='evento',
            name='numero',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
