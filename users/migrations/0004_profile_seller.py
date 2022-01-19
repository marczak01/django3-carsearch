# Generated by Django 3.2.5 on 2022-01-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='seller',
            field=models.CharField(choices=[('All', 'All'), ('Dealer', 'Dealer'), ('Private', 'Private')], max_length=200, null=True),
        ),
    ]