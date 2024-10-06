# Create your models here.
from django.db import models
from medications.models import Medication

class Resident(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    room_number = models.CharField(max_length=10)
    medical_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicationSchedule(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='medication_schedules')

    def __str__(self):
        return f"Medication Schedule for {self.resident.first_name} {self.resident.last_name}"

class MedicationEntry(models.Model):
    TIME_OF_DAY_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('late_evening', 'Late Evening'),
    ]

    medication_schedule = models.ForeignKey(MedicationSchedule, on_delete=models.CASCADE, related_name='entries')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    time_of_day = models.CharField(max_length=20, choices=TIME_OF_DAY_CHOICES)
    dosage = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.medication.trade_name} for {self.medication_schedule.resident.first_name} at {self.time_of_day}"