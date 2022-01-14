# Generated by Django 3.2.5 on 2022-01-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0006_auto_20220107_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='bezwypadkowe',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='color',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='first_owner',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='manual_auto',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='mileage',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='num_of_doors',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='poj_skok',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='power',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='seller',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='uszkodzone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='wariant',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='year_of_production',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
