# Generated by Django 4.2.4 on 2023-08-28 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0006_alter_job_salary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="required_skills",
            field=models.TextField(),
        ),
    ]
