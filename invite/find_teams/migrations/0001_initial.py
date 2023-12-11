# Generated by Django 4.2.7 on 2023-12-11 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("find_members", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lamaran",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Accepted", "Accepted"),
                            ("Pending", "Pending"),
                            ("Denied", "Denied"),
                        ],
                        default="Pending",
                        max_length=10,
                    ),
                ),
                ("nama", models.CharField(max_length=255)),
                ("universitas", models.CharField(max_length=255)),
                ("jurusan", models.CharField(max_length=255)),
                ("keahlian", models.CharField(max_length=255)),
                ("cover_letter", models.TextField(blank=True)),
                ("tautan_portofolio", models.CharField(max_length=255)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "lowongan",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="find_members.lowonganregu",
                    ),
                ),
                (
                    "penerima",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_penerima",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "pengirim",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_pengirim",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
