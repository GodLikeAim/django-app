# Generated by Django 5.0.7 on 2024-09-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_footersettings_address_footersettings_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("title", models.CharField(max_length=100, verbose_name="Başlık")),
                ("description", models.TextField(verbose_name="Açıklama")),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Oluşturma Tarihi"
                    ),
                ),
                (
                    "service_img",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="service_images/",
                        verbose_name="Hizmet Fotoğrafı",
                    ),
                ),
            ],
        ),
    ]
