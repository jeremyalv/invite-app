# Generated by Django 4.2.7 on 2023-12-07 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ulasanprofil',
            options={'ordering': ['-updated_at']},
        ),
    ]
