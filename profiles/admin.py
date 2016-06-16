from django.contrib import admin

# Register your models here.
from .models import Human, Pet


admin.site.register(Human)
admin.site.register(Pet)