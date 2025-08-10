# Nursing Home Management App

A simple Django-based web application for managing a nursing home.  
It provides basic CRUD (Create, Read, Update, Delete) functionality for residents, medications, and reports.  
The project uses SQLite3 as the database and Tailwind CSS for basic styling.

## Features

### Dashboard
- Main view with three tiles:
  - **Reports**
  - **Residents**
  - **Medications**

### Modules

#### Reports
- Fields: `date`, `note`, `signature` (signature functionality not yet implemented)  
- Full CRUD support

#### Residents
- Fields: `first_name`, `last_name`, `date_of_birth`, `room_number`, `medical_conditions`  
- Full CRUD support

#### Medications
- Fields: `trade_name`, `international_latin_name`  
- Full CRUD support

## Tech Stack
- **Backend:** Python, Django  
- **Database:** SQLite3  
- **Frontend:** Tailwind CSS (basic configuration, not fully implemented yet)

## Installation & Setup

1. Clone the repository:  
   
   git clone https://github.com/AleksandraSieg/project-nursing-home.git
   cd project-nursing-home

2. Create and activate a virtual environment:
         python3 -m venv venv
           # source venv/bin/activate  # macOS/Linux
           # venv\Scripts\activate   # Windows

3. Install dependencies:
    pip install -r requirements.txt

4. Run the development server:
    python manage.py runserver

