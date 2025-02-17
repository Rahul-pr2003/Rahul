# Generated by Django 5.1.3 on 2025-01-13 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0010_video"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shorts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(help_text="Title of the video", max_length=255),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Brief description of the video",
                        null=True,
                    ),
                ),
                (
                    "video_file",
                    models.FileField(
                        help_text="Upload the video file", upload_to="pic"
                    ),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        help_text="Upload a thumbnail image",
                        null=True,
                        upload_to="pic",
                    ),
                ),
                (
                    "uploaded_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Timestamp when the video was uploaded",
                    ),
                ),
            ],
        ),
    ]
