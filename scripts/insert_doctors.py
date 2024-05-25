import sqlite3
from faker import Faker

# Initialize Faker to generate realistic data
fake = Faker()

# Connect to the database
conn = sqlite3.connect('bazazdravil.db')
cur = conn.cursor()

# Clear existing data in the DOCTORS table
cur.execute('DELETE FROM DOCTORS')
cur.execute('DELETE FROM sqlite_sequence WHERE name="DOCTORS"')  # Reset auto-incrementing primary key

# Generate and insert realistic data into DOCTORS table
for _ in range(5):
    username = fake.user_name()
    password = fake.password(length=10)
    cur.execute("INSERT INTO DOCTORS (username, password) VALUES (?, ?)",
                (username, password))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data insertion complete.")

