# Generated by Django 4.2.6 on 2023-10-22 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criticy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('speciality', models.ManyToManyField(related_name='techs', to='core.speciality')),
            ],
        ),
        migrations.CreateModel(
            name='TicketHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('entry', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('criticy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='core.criticy')),
                ('history', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='core.tickethistory')),
                ('tech', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets', to='core.tech')),
            ],
        ),
    ]
