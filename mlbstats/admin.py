from django.contrib.admin import ModelAdmin, register
from .models import Player


@register(Player)
class PersonAdmin(ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        "events",
        "player_id",
        "attempts",
        "avg_hit_angle",
        "anglesweetspotpercent",
        "max_hit_speed",
        "avg_hit_speed",
        "fbld",
        "gb",
        "max_distance",
        "avg_distance",
        "avg_hr_distance",
        "ev95plus",
        "ev95per_swing",
        "ev95percent",
        "barrels",
        "brl_percent",
        "brl_pa",
        "hc_x",
        "hc_y",
        "launch_speed",
    )
