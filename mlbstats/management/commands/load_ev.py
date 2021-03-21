from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Load data from exit_velocty.csv"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("Successfully loaded data from exit_velocity.csv")
        )
