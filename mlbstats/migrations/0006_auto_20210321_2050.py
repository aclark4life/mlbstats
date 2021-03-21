# Generated by Django 3.1.7 on 2021-03-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlbstats', '0005_player_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='hc_x',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='player',
            name='hc_y',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
