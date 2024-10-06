# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Resident, MedicationSchedule, MedicationEntry
from .forms import ResidentForm, MedicationEntryForm

def index(request):
    return render(request, 'index.html')

def resident_list(request):
    residents = Resident.objects.all()
    return render(request, 'residents/resident_list.html', {'residents': residents})

def resident_detail(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    schedule = MedicationSchedule.objects.filter(resident=resident).first()
    entries = MedicationEntry.objects.filter(medication_schedule=schedule) if schedule else []

    # Definiujemy kolejność pór dnia
    time_of_day_order = {
        'morning': 1,
        'afternoon': 2,
        'evening': 3,
        'late_evening': 4,
    }

    # Sortowanie według pory dnia
    sorted_entries = sorted(entries, key=lambda entry: time_of_day_order.get(entry.time_of_day, 5))

    return render(request, 'residents/resident_detail.html', {'resident': resident, 'entries': sorted_entries})

def resident_create(request):
    if request.method == "POST":
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resident_list')
    else:
        form = ResidentForm()
    return render(request, 'residents/resident_form.html', {'form': form})

def resident_update(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    if request.method == "POST":
        form = ResidentForm(request.POST, instance=resident)
        if form.is_valid():
            form.save()
            return redirect('resident_list')
    else:
        form = ResidentForm(instance=resident)
    return render(request, 'residents/resident_form.html', {'form': form})

def resident_delete(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    if request.method == "POST":
        resident.delete()
        return redirect('resident_list')
    return render(request, 'residents/resident_confirm_delete.html', {'resident': resident})


def add_medication_entry(request, resident_id):
    # Pobierz mieszkańca na podstawie jego ID
    resident = get_object_or_404(Resident, id=resident_id)

    # Pobierz harmonogram leków mieszkańca lub utwórz nowy, jeśli go nie ma
    schedule, created = MedicationSchedule.objects.get_or_create(resident=resident)

    if request.method == "POST":
        form = MedicationEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.medication_schedule = schedule
            entry.save()
            return redirect('resident_detail', pk=resident_id)  # Powrót do strony szczegółów mieszkańca
    else:
        form = MedicationEntryForm()

    return render(request, 'residents/add_medication_entry.html', {'form': form, 'resident': resident})

def edit_medication_entry(request, entry_id):
    entry = get_object_or_404(MedicationEntry, id=entry_id)
    if request.method == "POST":
        form = MedicationEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('resident_detail', pk=entry.medication_schedule.resident.id)
    else:
        form = MedicationEntryForm(instance=entry)
    return render(request, 'residents/edit_medication_entry.html', {'form': form, 'entry': entry})

def delete_medication_entry(request, entry_id):
    entry = get_object_or_404(MedicationEntry, id=entry_id)
    if request.method == "POST":
        entry.delete()
        return redirect('resident_detail', pk=entry.medication_schedule.resident.id)
    return render(request, 'residents/delete_medication_entry.html', {'entry': entry})
