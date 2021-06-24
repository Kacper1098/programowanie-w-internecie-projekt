from django.contrib import admin
from .models import Visit, Patient, Facility, Doctor, Schedule

admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Facility)
admin.site.register(Doctor)
admin.site.register(Schedule)

