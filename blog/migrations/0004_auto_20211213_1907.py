# Generated by Django 3.2.9 on 2021-12-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210320_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, default=None, related_name='posts', to='blog.PostCategory'),
        ),
    ]