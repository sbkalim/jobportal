# Generated by Django 4.2.4 on 2023-08-30 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0009_alter_job_city"),
    ]

    operations = [
        migrations.DeleteModel(
            name="City",
        ),
    ]
