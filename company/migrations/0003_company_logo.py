# Generated by Django 4.2.4 on 2023-08-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="company_logos/"),
        ),
    ]