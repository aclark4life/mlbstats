from django.db import models


class Player(models.Model):
    """
    Model exit_velocity.csv from https://baseballsavant.mlb.com/statcast_field

    E.g.

    last_name, first_name,player_id,attempts,avg_hit_angle,anglesweetspotpercent,max_hit_speed,avg_hit_speed,fbld,gb,max_distance,avg_distance,avg_hr_distance,ev95plus,ev95per-swing,ev95percent,barrels,brl_percent,brl_pa

    Tatis Jr., Fernando,665487,164,8.7,32.3,113.4,95.9,100.2,91.6,458,176,410,102,22.1,62.2,32,19.5,12.5
    """

    last_name = models.CharField(max_length=255, default="")
    first_name = models.CharField(max_length=255, default="")
    player_id = models.IntegerField(default=0)
    attempts = models.IntegerField(default=0)
    avg_hit_angle = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    anglesweetspotpercent = models.DecimalField(
        max_digits=3, decimal_places=1, default=0
    )
    max_hit_speed = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    avg_hit_speed = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    fbld = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    gb = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    max_distance = models.IntegerField(default=0)
    avg_distance = models.IntegerField(default=0)
    avg_hr_distance = models.IntegerField(default=0)
    ev95plus = models.IntegerField(default=0)
    ev95per_swing = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    ev95percent = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    barrels = models.IntegerField(default=0)
    brl_percent = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    brl_pa = models.DecimalField(max_digits=3, decimal_places=1, default=0)
