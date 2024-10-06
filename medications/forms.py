from django import forms
from .models import Medication

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['trade_name', 'international_latin_name']  # Zaktualizowana nazwa pola
