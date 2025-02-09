from django import forms
from .models import Resident
from .models import MedicationEntry

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ['first_name', 'last_name', 'date_of_birth', 'room_number', 'medical_conditions']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

class MedicationEntryForm(forms.ModelForm):
    end_date = forms.DateField(
        required=False,  # Pozwala pozostawić pole puste
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = MedicationEntry
        fields = ['medication', 'time_of_day', 'dosage', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }