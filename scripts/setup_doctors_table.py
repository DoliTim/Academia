import sqlite3

conn = sqlite3.connect('bazazdravil.db')
cur = conn.cursor()

# Drop the existing DOCTORS table if it exists
cur.execute('DROP TABLE IF EXISTS DOCTORS')

# Create the new DOCTORS table
cur.execute('''CREATE TABLE DOCTORS (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)''')

# Insert a sample doctor
cur.execute("INSERT INTO DOCTORS (username, password) VALUES (?, ?)",
            ('doctor1', 'password1'))

conn.commit()
conn.close()

print("DOCTORS table setup complete.")

