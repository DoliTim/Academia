import sqlite3
from cryptography.fernet import Fernet
from datetime import datetime
import random
import faker

# Initialize Faker to generate realistic data
fake = faker.Faker()

# Load the encryption key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

# Function to get encrypted health card number
def get_encrypted_health_number(health_in_number):
    return cipher_suite.encrypt(health_in_number.encode()).decode()

# Connect to the database
conn = sqlite3.connect('bazazdravil.db')
cur = conn.cursor()

# Clear existing data in the Osebe table
cur.execute('DELETE FROM Osebe')
cur.execute('DELETE FROM sqlite_sequence WHERE name="Osebe"')  # Reset auto-incrementing primary key

# Clear existing data in the Kartoteke table
cur.execute('DELETE FROM Kartoteke')
cur.execute('DELETE FROM sqlite_sequence WHERE name="Kartoteke"')  # Reset auto-incrementing primary key

# Generate and insert realistic data into Osebe table
for _ in range(20):
    health_in_number = fake.bothify(text='HCN####')
    email = fake.email()
    password = fake.password(length=10)
    encrypted_health_number = get_encrypted_health_number(health_in_number)
    cur.execute("INSERT INTO Osebe (health_in_number, email, password) VALUES (?, ?, ?)",
                (encrypted_health_number, email, password))

# Generate and insert matching data into Kartoteke table
for patient_id in range(1, 21):
    drug = fake.random_element(elements=('DrugA', 'DrugB', 'DrugC', 'DrugD', 'DrugE'))
    dosage = fake.random_element(elements=('10mg', '20mg', '30mg', '40mg', '50mg'))
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("INSERT INTO Kartoteke (patient_id, Zdravilo, Odmerjanje, Datum_in_cas) VALUES (?, ?, ?, ?)",
                (patient_id, drug, dosage, current_time))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data insertion complete.")
