# Medicine Tracker

## Overview

Medicine Tracker is a web application designed to help patients and doctors manage and track medication prescriptions. Patients can register, log in, and enter details about their prescribed drugs and dosages. Doctors can log in to view and filter patient records.

## Features

- **User Registration**: Patients can register using their email, password, and health card number.
- **User Login**: Patients can log in to the application to enter and view their medication records.
- **Doctor Login**: Doctors can log in to view and filter patient medication records.
- **Medication Entry**: Patients can enter details about their prescribed drugs and dosages.
- **View Entries**: Patients can view their past medication entries.
- **Doctor Dashboard**: Doctors can view and filter patient records by patient ID and date.

## Project Structure

```
your_project/
│
├── app.py
├── templates/
│ ├── base.html
│ ├── login.html
│ ├── register.html
│ ├── doctor_login.html
│ ├── doctor_dashboard.html
│ └── architecture.html
├── static/
│ └── images/
│ └── architecture.png
├── bazazdravil.db
├── requirements.txt
├── insert_data.py
├── insert_doctors.py
└── secret.key
```
## Screenshots
![image](https://github.com/DoliTim/Academia/assets/121125226/694216c0-d205-49f4-adc2-12ce40aabc55)
![image](https://github.com/DoliTim/Academia/assets/121125226/ccfd2f3f-d587-4f34-8474-d77b7fcb49fb)
![image](https://github.com/DoliTim/Academia/assets/121125226/06a4d064-1c64-492c-9278-f34f94098bba)
![image](https://github.com/DoliTim/Academia/assets/121125226/cf7e63b6-c437-4122-861a-a633ea0973f7)


## Installation

1. Clone the repository:

```sh
git clone https://github.com/DoliTim/Academia.git
cd Academia
```

2. Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:

```sh
pip install -r requirements.txt
```


1. Run the Flask application:

```sh
flask run
```
or python app.py

2. Open your web browser and navigate to http://127.0.0.1:5000.

3. Use the application:
    - Register as a patient.
    - Log in as a patient to enter and view medication records.
    - Log in as a doctor to view and filter patient records.

