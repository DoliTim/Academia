import sqlite3
from cryptography.fernet import Fernet

# Generate a key for encryption
# This key should be kept secret and safe
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Store the key in a file for later use (in a real application, this should be more secure)
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

conn = sqlite3.connect('bazazdravil.db')
cur = conn.cursor()

# Drop the existing Osebe table if it exists
cur.execute('DROP TABLE IF EXISTS Osebe')

# Create the new Osebe table
cur.execute('''CREATE TABLE Osebe (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    health_in_number TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)''')

# Drop the existing Kartoteke table if it exists
cur.execute('DROP TABLE IF EXISTS Kartoteke')

# Create the new Kartoteke table
cur.execute('''CREATE TABLE Kartoteke (
    Kartoteke_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    Zdravilo TEXT NOT NULL,
    Odmerjanje TEXT NOT NULL,
    Datum_in_cas TEXT NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Osebe(patient_id)
)''')

conn.commit()
conn.close()
