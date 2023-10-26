# Generated by Django 4.2.6 on 2023-10-26 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelplanner', '0011_alter_basket_attraction_costs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='attraction_costs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='basket',
            name='hotel_costs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_date',
            field=models.DateTimeField(),
        ),
    ]
