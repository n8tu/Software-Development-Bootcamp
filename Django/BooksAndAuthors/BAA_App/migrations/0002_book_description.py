# Generated by Django 2.2.4 on 2022-06-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BAA_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='There is no description for this book'),
        ),
    ]
