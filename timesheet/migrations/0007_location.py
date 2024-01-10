# Generated by Django 4.2.7 on 2024-01-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0006_timesheet_clock_in_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]
