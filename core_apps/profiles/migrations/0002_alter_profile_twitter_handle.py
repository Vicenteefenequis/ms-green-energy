# Generated by Django 4.1.7 on 2023-08-10 20:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="twitter_handle",
            field=models.CharField(
                blank=True, max_length=20, verbose_name="twitter handle"
            ),
        ),
    ]
