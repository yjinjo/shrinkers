# Generated by Django 4.2 on 2023-04-29 04:59

from django.db import migrations, models
import shortener.models


class Migration(migrations.Migration):

    dependencies = [
        ("shortener", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="url_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="shortenedurls",
            name="prefix",
            field=models.CharField(
                default=shortener.models.ShortenedUrls.rand_letter, max_length=50
            ),
        ),
    ]
