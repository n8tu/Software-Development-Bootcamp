# Generated by Django 2.2.4 on 2022-06-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersShellApp', '0002_auto_20220614_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
