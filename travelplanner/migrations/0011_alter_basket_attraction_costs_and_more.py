# Generated by Django 4.2.6 on 2023-10-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelplanner', '0010_alter_flight_visa_duration_alter_flight_visa_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='attraction_costs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='hotel_costs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_date',
            field=models.IntegerField(),
        ),
    ]
