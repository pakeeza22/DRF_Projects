# Generated by Django 3.2.9 on 2021-11-17 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='passby',
            field=models.CharField(default='teacher', max_length=200),
            preserve_default=False,
        ),
    ]