# Generated by Django 3.0.5 on 2020-04-30 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20200430_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.CharField(max_length=660),
        ),
    ]
