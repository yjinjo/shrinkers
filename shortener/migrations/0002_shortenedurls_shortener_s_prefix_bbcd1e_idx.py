# Generated by Django 4.2 on 2023-04-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortener", "0001_initial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="shortenedurls",
            index=models.Index(
                fields=["prefix", "shortened_url"], name="shortener_s_prefix_bbcd1e_idx"
            ),
        ),
    ]
