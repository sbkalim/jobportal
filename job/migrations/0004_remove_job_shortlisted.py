# Generated by Django 4.2.4 on 2023-08-21 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0003_job_shortlisted"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="shortlisted",
        ),
    ]