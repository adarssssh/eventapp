# Generated by Django 4.2.17 on 2024-12-07 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PhoneOTP",
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
                ("phone", models.CharField(max_length=17, unique=True)),
                ("otp", models.CharField(max_length=6)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("attempts", models.IntegerField(default=0)),
                ("is_verified", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ServiceProviderProfile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="service_provider_profile",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("company_name", models.CharField(max_length=200)),
                ("service_types", models.JSONField(default=list)),
                ("location", models.CharField(max_length=300)),
            ],
        ),
    ]
