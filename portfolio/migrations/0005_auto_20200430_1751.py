# Generated by Django 3.0.5 on 2020-04-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200430_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texto',
            name='titulo',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
