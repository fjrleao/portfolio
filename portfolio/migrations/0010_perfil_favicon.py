# Generated by Django 3.0.5 on 2020-04-30 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20200430_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='favicon',
            field=models.CharField(default=django.utils.timezone.now, max_length=660),
            preserve_default=False,
        ),
    ]