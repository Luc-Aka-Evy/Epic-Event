# Generated by Django 4.0.5 on 2022-06-08 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=128)),
                ("adress", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=255)),
                ("type", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Contract",
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
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("updated_time", models.DateTimeField()),
                ("signed", models.BooleanField(default=False)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.company"
                    ),
                ),
                (
                    "user_saler",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="saler",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Location",
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
                ("adress", models.CharField(max_length=255)),
                ("postcode", models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
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
                ("description", models.CharField(max_length=2048)),
                ("start", models.DateTimeField()),
                ("end", models.DateTimeField()),
                ("time_created", models.DateTimeField(auto_now_add=True)),
                (
                    "contract",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.contract"
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.location"
                    ),
                ),
                (
                    "user_support",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="support",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
