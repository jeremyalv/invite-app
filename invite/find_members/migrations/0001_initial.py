# Generated by Django 4.2.7 on 2023-11-30 13:16

from django.db import migrations, models
import django.db.models.deletion
import find_members.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user_profile", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TautanMediaSosialLowongan",
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
                ("website", models.CharField(blank=True, max_length=250)),
                ("instagram", models.CharField(blank=True, max_length=250)),
                ("twitter", models.CharField(blank=True, max_length=250)),
                ("linkedin", models.CharField(blank=True, max_length=250)),
                ("github", models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="LowonganRegu",
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
                ("is_active", models.BooleanField(default=True)),
                ("nama_regu", models.CharField(max_length=255)),
                ("deskripsi_lowongan_regu", models.TextField()),
                (
                    "foto_lowongan_regu",
                    models.ImageField(
                        upload_to=find_members.models.LowonganRegu.vacancy_directory_path
                    ),
                ),
                ("nama_lomba", models.CharField(max_length=255)),
                ("bidang_lomba", models.CharField(max_length=255)),
                ("tanggal_lomba", models.DateTimeField()),
                (
                    "expiry",
                    models.DateTimeField(default=find_members.models.get_n_days_future),
                ),
                ("jumlah_anggota_sekarang", models.PositiveIntegerField(default=0)),
                ("total_anggota_dibutuhkan", models.PositiveIntegerField(default=0)),
                (
                    "ketua",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_profile.ketuaregu",
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