import csv

from django.core.management.base import BaseCommand, CommandError

from mlbstats.models import Player


class Command(BaseCommand):
    help = "Load data from exit_velocity.csv"

    def handle(self, *args, **options):
        ev_csv = open("exit_velocity.csv")
        for row in csv.reader(ev_csv):
            (
                last_name,
                first_name,
                player_id,
                attempts,
                avg_hit_angle,
                anglesweetspotpercent,
                max_hit_speed,
                avg_hit_speed,
                fbld,
                gb,
                max_distance,
                avg_distance,
                avg_hr_distance,
                ev95plus,
                ev95per_swing,
                ev95percent,
                barrels,
                brl_percent,
                brl_pa,
            ) = row
            player = Player(
                last_name=last_name,
                first_name=first_name,
                player_id=player_id,
                attempts=attempts,
                avg_hit_angle=avg_hit_angle,
                anglesweetspotpercent=anglesweetspotpercent,
                # max_hit_speed=max_hit_speed,
                avg_hit_speed=avg_hit_speed,
                # fbld=fbld,
                gb=gb,
                max_distance=max_distance,
                avg_distance=avg_distance,
                avg_hr_distance=avg_hr_distance,
                ev95plus=ev95plus,
                ev95per_swing=ev95per_swing,
                ev95percent=ev95percent,
                barrels=barrels,
                brl_percent=brl_percent,
                brl_pa=brl_pa,
            )
            player.save()
        self.stdout.write(
            self.style.SUCCESS("Successfully loaded data from exit_velocity.csv")
        )
