# Generated by Django 4.2.4 on 2023-08-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="required_skills",
            field=models.TextField(default="Ex: Python, Django"),
        ),
    ]