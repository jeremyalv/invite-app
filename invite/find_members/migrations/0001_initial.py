# Generated by Django 4.2.7 on 2023-12-08 05:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import find_members.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TautanMediaSosialLowongan",
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
                ("website", models.CharField(blank=True, max_length=250)),
                ("instagram", models.CharField(blank=True, max_length=250)),
                ("twitter", models.CharField(blank=True, max_length=250)),
                ("linkedin", models.CharField(blank=True, max_length=250)),
                ("github", models.CharField(blank=True, max_length=250)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="LowonganRegu",
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
                ("nama_regu", models.CharField(max_length=255)),
                (
                    "deskripsi_lowongan_regu",
                    models.TextField(
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            django.core.validators.MaxLengthValidator(2000),
                        ]
                    ),
                ),
                (
                    "foto_lowongan_regu",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=find_members.models.LowonganRegu.vacancy_directory_path,
                    ),
                ),
                ("nama_lomba", models.CharField(max_length=255)),
                ("bidang_lomba", models.CharField(max_length=255)),
                ("tanggal_lomba", models.DateTimeField(blank=True, null=True)),
                (
                    "expiry",
                    models.DateTimeField(default=find_members.models.get_n_days_future),
                ),
                ("jumlah_anggota_sekarang", models.PositiveIntegerField(default=0)),
                ("total_anggota_dibutuhkan", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ketua",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tautan_medsos_regu",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="find_members.tautanmediasosiallowongan",
                    ),
                ),
            ],
        ),
    ]
