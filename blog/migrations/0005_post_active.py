# Generated by Django 3.2.9 on 2021-12-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211213_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
