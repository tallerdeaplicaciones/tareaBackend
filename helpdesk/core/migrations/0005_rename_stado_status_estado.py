# Generated by Django 4.2.5 on 2023-10-24 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_status_alter_speciality_name_alter_tech_last_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='stado',
            new_name='estado',
        ),
    ]