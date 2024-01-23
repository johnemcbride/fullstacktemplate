# Generated by Django 4.2.9 on 2024-01-23 23:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date created"
            ),
        ),
    ]