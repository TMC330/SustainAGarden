# Generated by Django 4.2.11 on 2024-03-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("challenges", "0004_alter_transport_challenge_distance_covered"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_image",
            field=models.ImageField(default="default.jpg", upload_to="profile_images/"),
        ),
    ]