# Generated by Django 4.1.7 on 2023-04-13 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="Member",
        ),
    ]
