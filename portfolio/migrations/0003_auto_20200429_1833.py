# Generated by Django 3.0.5 on 2020-04-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200429_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='conteudo',
            field=models.TextField(max_length=255),
        ),
    ]
