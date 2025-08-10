
---

### `README_pl.md`

```markdown
# Aplikacja do Zarządzania Domem Spokojnej Starości

Prosta aplikacja webowa oparta na Django do zarządzania domem spokojnej starości.  
Zapewnia podstawową funkcjonalność CRUD (tworzenie, odczyt, edycja, usuwanie) dla mieszkańców, leków i raportów.  
Projekt używa bazy danych SQLite3 oraz Tailwind CSS do podstawowego stylowania.

## Funkcjonalności

### Dashboard (Pulpit)
- Główny widok z trzema kafelkami:
  - **Reports** (Raporty)
  - **Residents** (Mieszkańcy)
  - **Medications** (Leki)

### Moduły

#### Reports (Raporty)
- Pola: `date` (data), `note` (notatka), `signature` (podpis — funkcjonalność jeszcze niezaimplementowana)  
- Pełne wsparcie CRUD

#### Residents (Mieszkańcy)
- Pola: `first_name` (imię), `last_name` (nazwisko), `date_of_birth` (data urodzenia), `room_number` (numer pokoju), `medical_conditions` (schorzenia)  
- Pełne wsparcie CRUD

#### Medications (Leki)
- Pola: `trade_name` (nazwa handlowa), `international_latin_name` (międzynarodowa nazwa łacińska)  
- Pełne wsparcie CRUD

## Technologie
- **Backend:** Python, Django  
- **Baza danych:** SQLite3  
- **Frontend:** Tailwind CSS (podstawowa konfiguracja, jeszcze nie w pełni działająca)

## Instalacja i uruchomienie

1. Sklonuj repozytorium:  
   ```bash
   git clone https://github.com/AleksandraSieg/project-nursing-home.git
   cd project-nursing-home

2. Utwórz i aktywuj wirtualne środowisko:
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate   # Windows

3. Zainstaluj wymagane pakiety:
    pip install -r requirements.txt

4. Uruchom serwer deweloperski:
    python manage.py runserver

