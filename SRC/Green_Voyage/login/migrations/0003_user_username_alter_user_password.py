# Generated by Django 4.1.7 on 2023-04-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='john doe', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
