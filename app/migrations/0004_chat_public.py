# Generated by Django 3.2 on 2023-05-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20230504_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
