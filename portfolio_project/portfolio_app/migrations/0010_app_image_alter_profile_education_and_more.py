# Generated by Django 5.1.6 on 2025-04-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0009_profile_blog_profile_github_profile_hobbies_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="app",
            name="image",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="education",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="profile",
            name="location",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="profile",
            name="name",
            field=models.CharField(max_length=20),
        ),
    ]
