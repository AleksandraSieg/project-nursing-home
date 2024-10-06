# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Medication
from .forms import MedicationForm

def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'medications/medication_list.html', {'medications': medications})

def medication_detail(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    return render(request, 'medications/medication_detail.html', {'medication': medication})

def medication_create(request):
    if request.method == "POST":
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medication_list')
    else:
        form = MedicationForm()
    return render(request, 'medications/medication_form.html', {'form': form})

def medication_update(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    if request.method == "POST":
        form = MedicationForm(request.POST, instance=medication)
        if form.is_valid():
            form.save()
            return redirect('medication_list')
    else:
        form = MedicationForm(instance=medication)
    return render(request, 'medications/medication_form.html', {'form': form})

def medication_delete(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    if request.method == "POST":
        medication.delete()
        return redirect('medication_list')
    return render(request, 'medications/medication_confirm_delete.html', {'medication': medication})
