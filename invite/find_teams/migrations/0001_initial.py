# Generated by Django 4.2.7 on 2023-11-30 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user_profile", "0001_initial"),
        ("find_members", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lamaran",
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
                (
                    "lowongan",
                    models.OneToOneField(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="find_members.lowonganregu",
                    ),
                ),
                (
                    "penerima",
                    models.OneToOneField(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_profile.ketuaregu",
                    ),
                ),
                (
                    "pengirim",
                    models.OneToOneField(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_profile.pencariregu",
                    ),
                ),
            ],
        ),
    ]
