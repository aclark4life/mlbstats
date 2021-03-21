from django.contrib.admin import ModelAdmin, register
from .models import Person


@register(Person)
class PersonAdmin(ModelAdmin):
    pass
