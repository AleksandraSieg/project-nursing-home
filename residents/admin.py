from django.contrib import admin
from .models import Resident
from .models import MedicationSchedule

# Register your models here.
admin.site.register(Resident)
admin.site.register(MedicationSchedule)