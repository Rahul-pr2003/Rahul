# Generated by Django 5.1.3 on 2025-01-19 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0013_booking_refund_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="payment_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
