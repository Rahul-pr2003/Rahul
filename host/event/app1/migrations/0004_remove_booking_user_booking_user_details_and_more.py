# Generated by Django 5.1.3 on 2025-01-08 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0003_alter_booking_options_remove_booking_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="user",
        ),
        migrations.AddField(
            model_name="booking",
            name="user_details",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bookings",
                to="app1.userregister",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="adminbooking",
            name="caterer_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("confirmed", "Confirmed"),
                    ("canceled", "Canceled"),
                    ("completed", "Completed"),
                ],
                default="pending",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="adminbooking",
            name="entertainer_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("confirmed", "Confirmed"),
                    ("canceled", "Canceled"),
                    ("completed", "Completed"),
                ],
                default="pending",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="adminbooking",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("confirmed", "Confirmed"),
                    ("canceled", "Canceled"),
                    ("completed", "Completed"),
                ],
                default="pending",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="adminbooking",
            name="tailor_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("confirmed", "Confirmed"),
                    ("canceled", "Canceled"),
                    ("completed", "Completed"),
                ],
                default="pending",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bookings",
                to="app1.events",
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("confirmed", "Confirmed"),
                    ("canceled", "Canceled"),
                    ("completed", "Completed"),
                ],
                default="pending",
                max_length=10,
            ),
        ),
    ]
