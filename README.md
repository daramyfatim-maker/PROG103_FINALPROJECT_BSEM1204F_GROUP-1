# Medica Sierra Leone

**Medica** is a comprehensive, offline‑capable hospital management system designed specifically for healthcare facilities in Sierra Leone. It digitises patient records, automates queuing, provides real‑time analytics, and generates reports – all within a user‑friendly graphical interface. Built with Python and open‑source technologies, Medica runs on basic hardware without requiring an internet connection.

## Features

- User authentication with three roles (Admin, Doctor, Nurse)
- Patient registration, update, and deletion (CRUD)
- Paginated patient list with search and filtering
- Queue management with priority levels (normal, urgent, super‑urgent)
- Visit history tracking for each patient
- Interactive data visualisation dashboard (8 charts)
- PDF report generation (weekly, monthly, yearly, and custom date ranges)
- Export patient data to CSV
- Light and dark theme switching
- Offline‑first design – no internet required
- SQLite embedded database – no separate server needed

## Technology Stack

- Python 3.13
- Tkinter (GUI)
- SQLite (database)
- Matplotlib (charts)
- ReportLab (PDF generation)
- Git / GitHub (version control)
- MIT License

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/medica.git
   cd medica