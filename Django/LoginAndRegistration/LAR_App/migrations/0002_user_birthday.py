# Generated by Django 2.2 on 2022-06-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LAR_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default='1999-01-01'),
        ),
    ]
