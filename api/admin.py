from django.contrib import admin

from .models import Specialization, Visit, Service, Doctor, Patient

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Visit)
admin.site.register(Specialization)