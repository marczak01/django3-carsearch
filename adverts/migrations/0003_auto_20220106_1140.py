# Generated by Django 3.2.5 on 2022-01-06 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0002_auto_20220106_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='vote_ratio',
        ),
        migrations.RemoveField(
            model_name='advert',
            name='vote_total',
        ),
    ]
