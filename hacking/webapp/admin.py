from django.contrib import admin
from .models import Program, Event, Subscriber

# Register your models here.
admin.site.register(Program)
admin.site.register(Event)
admin.site.register(Subscriber)
