# Generated by Django 5.0.1 on 2024-09-02 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0002_hospitalreport_delete_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalreport',
            name='average_appointment_duration',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='hospitalreport',
            name='total_expenses',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]