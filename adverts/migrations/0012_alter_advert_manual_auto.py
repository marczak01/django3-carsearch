# Generated by Django 3.2.5 on 2022-01-09 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0011_alter_advert_year_of_production'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='manual_auto',
            field=models.CharField(choices=[('M', 'Manual'), ('A', 'Automatic')], default='A', max_length=200, null=True),
        ),
    ]
