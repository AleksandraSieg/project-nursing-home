from django import forms
from .models import Resident
from .models import MedicationEntry

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ['first_name', 'last_name', 'date_of_birth', 'room_number', 'medical_conditions']

class MedicationEntryForm(forms.ModelForm):
    class Meta:
        model = MedicationEntry
        fields = ['medication', 'time_of_day', 'dosage', 'start_date', 'end_date']