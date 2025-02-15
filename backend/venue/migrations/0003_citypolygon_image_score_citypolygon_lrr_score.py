# Generated by Django 4.2.17 on 2025-01-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("venue", "0002_remove_citypolygon_image_score_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="citypolygon",
            name="image_score",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name="citypolygon",
            name="lrr_score",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
