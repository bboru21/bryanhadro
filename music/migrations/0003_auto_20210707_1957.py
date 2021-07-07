# Generated by Django 3.1.7 on 2021-07-07 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210707_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='category',
        ),
        migrations.AddField(
            model_name='song',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='songs', to='music.Category'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', to='music.artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='youtube_video_link',
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
    ]