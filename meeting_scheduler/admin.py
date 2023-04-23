from django.contrib import admin
from meeting_scheduler.models import OffHour, Appointment

# Register your models here.
admin.site.register(OffHour)
admin.site.register(Appointment)
