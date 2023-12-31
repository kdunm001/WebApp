# Generated by Django 4.2.7 on 2023-12-31 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0005_timesheet_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='clock_in_latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='clock_in_longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='clock_out_latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='clock_out_longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
