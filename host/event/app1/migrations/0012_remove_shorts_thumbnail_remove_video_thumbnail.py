# Generated by Django 5.1.3 on 2025-01-13 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0011_shorts"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shorts",
            name="thumbnail",
        ),
        migrations.RemoveField(
            model_name="video",
            name="thumbnail",
        ),
    ]
