# Generated by Django 4.2 on 2023-07-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="video",
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
                ("AreaName", models.CharField(max_length=255)),
                ("file_name", models.CharField(max_length=255)),
                ("file_path", models.CharField(max_length=255)),
            ],
        ),
    ]
