# Generated by Django 3.1.7 on 2021-07-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images/')),
                ('alt', models.CharField(max_length=255)),
                ('caption', models.TextField()),
            ],
        ),
    ]
