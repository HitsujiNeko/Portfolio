# Generated by Django 5.1.6 on 2025-04-30 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0010_app_image_alter_profile_education_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="about_me",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="hobbies",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="interests",
        ),
    ]
