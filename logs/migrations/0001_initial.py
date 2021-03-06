# Generated by Django 3.2.11 on 2022-04-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Log",
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
                ("host", models.CharField(max_length=150, verbose_name="host")),
                ("request_time", models.DateTimeField(verbose_name="request_time")),
                (
                    "request_line",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="request_line",
                    ),
                ),
                (
                    "remote_logname",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="remote_logname",
                    ),
                ),
                (
                    "remote_user",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="remote_user",
                    ),
                ),
                ("referer", models.CharField(max_length=150, verbose_name="referer")),
                (
                    "user_agent",
                    models.CharField(max_length=150, verbose_name="user_agent"),
                ),
                (
                    "final_status",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="final_status"
                    ),
                ),
                ("bytes_sent", models.PositiveIntegerField(verbose_name="bytes_sent")),
            ],
            options={
                "verbose_name": "????????",
                "verbose_name_plural": "????????",
            },
        ),
    ]
