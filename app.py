from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from datetime import datetime
from cryptography.fernet import Fernet

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

# Load the encryption key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

# Function to get user by email
def get_user_by_email(email):
    conn = sqlite3.connect('bazazdravil.db')
    cur = conn.cursor()
    cur.execute("SELECT patient_id, password FROM Osebe WHERE email = ?", (email,))
    user = cur.fetchone()
    conn.close()
    return user

# Function to get encrypted health card number
def get_encrypted_health_number(health_in_number):
    return cipher_suite.encrypt(health_in_number.encode()).decode()

# Function to get doctor by username
def get_doctor_by_username(username):
    conn = sqlite3.connect('bazazdravil.db')
    cur = conn.cursor()
    cur.execute("SELECT doctor_id, password FROM DOCTORS WHERE username = ?", (username,))
    doctor = cur.fetchone()
    conn.close()
    return doctor

@app.route('/architecture')
def architecture():
    return render_template('architecture.html')

# Route to display registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        health_in_number = request.form['health_in_number']
        email = request.form['email']
        password = request.form['password']

        # Check if email already exists in the database
        user = get_user_by_email(email)

        # If email exists, show error message
        if user:
            flash("Email already registered.", "error")
        else:
            encrypted_health_number = get_encrypted_health_number(health_in_number)

            conn = sqlite3.connect('bazazdravil.db')
            cur = conn.cursor()

            cur.execute("INSERT INTO Osebe (health_in_number, email, password) VALUES (?, ?, ?)",
                        (encrypted_health_number, email, password))
            conn.commit()
            conn.close()

            flash("Registration successful. Your password is: " + password, "success")
            return redirect(url_for('login'))

    return render_template('register.html')

# Route to display login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = get_user_by_email(email)

        if user and user[1] == password:
            session['user_id'] = user[0]
            flash("Login successful!", "success")
            return redirect(url_for('form'))
        else:
            flash("Invalid email or password.", "error")

    return render_template('login.html')

# Route to display doctor login form
@app.route('/doctor_login', methods=['GET', 'POST'])
def doctor_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        doctor = get_doctor_by_username(username)

        if doctor and doctor[1] == password:
            session['doctor_id'] = doctor[0]
            flash("Doctor login successful!", "success")
            return redirect(url_for('doctor_dashboard'))
        else:
            flash("Invalid username or password.", "error")

    return render_template('doctor_login.html')

# Route to display doctor dashboard
@app.route('/doctor_dashboard', methods=['GET', 'POST'])
def doctor_dashboard():
    if 'doctor_id' not in session:
        flash("Please log in as doctor first.", "error")
        return redirect(url_for('doctor_login'))

    filter_patient_id = request.form.get('patient_id') if request.method == 'POST' else None
    filter_date_from = request.form.get('date_from') if request.method == 'POST' else None
    filter_date_to = request.form.get('date_to') if request.method == 'POST' else None

    query = "SELECT * FROM Kartoteke"
    filters = []

    if filter_patient_id:
        filters.append(f"patient_id = {filter_patient_id}")
    if filter_date_from:
        filters.append(f"Datum_in_cas >= '{filter_date_from}'")
    if filter_date_to:
        filters.append(f"Datum_in_cas <= '{filter_date_to}'")

    if filters:
        query += " WHERE " + " AND ".join(filters)

    conn = sqlite3.connect('bazazdravil.db')
    cur = conn.cursor()
    cur.execute(query)
    entries = cur.fetchall()
    conn.close()

    return render_template('doctor_dashboard.html', entries=entries)

# Route to display form to enter drug and dosage
@app.route('/form', methods=['GET', 'POST'])
def form():
    if 'user_id' not in session:
        flash("Please log in first.", "error")
        return redirect(url_for('login'))

    if request.method == 'POST':
        drug = request.form['drug']
        dosage = request.form['dosage']
        patient_id = session['user_id']

        # Get current timestamp
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Connect to database
        conn = sqlite3.connect('bazazdravil.db')
        cur = conn.cursor()

        # Insert data into Kartoteke table with current timestamp and user ID
        cur.execute("INSERT INTO Kartoteke (patient_id, Zdravilo, Odmerjanje, Datum_in_cas) VALUES (?, ?, ?, ?)",
                    (patient_id, drug, dosage, current_time))

        conn.commit()
        conn.close()

        return redirect(url_for('get_entries'))

    return render_template('form.html')

# Route to display all previous entries for the logged-in user
@app.route('/entries', methods=['GET'])
def get_entries():
    if 'user_id' not in session:
        flash("Please log in first.", "error")
        return redirect(url_for('login'))

    patient_id = session['user_id']

    # Connect to database
    conn = sqlite3.connect('bazazdravil.db')
    cur = conn.cursor()

    # Retrieve all entries for the user from Kartoteke table
    cur.execute("SELECT * FROM Kartoteke WHERE patient_id = ?", (patient_id,))
    entries = cur.fetchall()
    conn.close()

    return render_template('entries.html', entries=entries)

@app.route('/')
def index():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
