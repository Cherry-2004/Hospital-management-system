import sqlite3

con = sqlite3.connect("hospital.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS patient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    disease TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS doctor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialization TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS appointment(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS admin(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cur.execute("""
INSERT INTO admin(username, password)
SELECT 'admin', 'admin'
WHERE NOT EXISTS (SELECT 1 FROM admin);
""")


con.commit()
con.close()

print("All tables created successfully")