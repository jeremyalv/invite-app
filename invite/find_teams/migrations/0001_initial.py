# Generated by Django 4.2.7 on 2023-12-01 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('find_members', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lamaran',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Denied', 'Denied')], default='Pending', max_length=10)),
                ('nama', models.CharField(max_length=255)),
                ('universitas', models.CharField(max_length=255)),
                ('jurusan', models.CharField(max_length=255)),
                ('keahlian', models.CharField(max_length=255)),
                ('cover_letter', models.TextField(blank=True)),
                ('tautan_portofolio', models.CharField(max_length=255)),
                ('lowongan', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='find_members.lowonganregu')),
                ('penerima', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_penerima', to=settings.AUTH_USER_MODEL)),
                ('pengirim', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_pengirim', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
