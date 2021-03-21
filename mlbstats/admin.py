from django.contrib.admin import ModelAdmin, register
from .models import Player


@register(Player)
class PersonAdmin(ModelAdmin):
    pass
