import sqlite3

login_details = [
    ["Martin Corbishley", "MCORB", "cake", "martin.corbishley@corbybusinessacademy.org", "Computer Science"],
    ["Heather thompson", "HTHOM", "cake", "heather.thompson@corbybusinessacademy.org", "Mathematics"]
]

conn = sqlite3.connect('StaffID.db')
cursor = conn.cursor()

def create_StaffID_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS StaffID(
        Staff_name TEXT PRIMARY KEY,
        username TEXT,
        password TEXT,
        email TEXT,
        subject TEXT
    );''')

    for entry in login_details:
        query = '''INSERT OR IGNORE INTO StaffID (Staff_name, username, password, email, subject)
                   VALUES (?, ?, ?, ?, ?)'''
        cursor.execute(query, tuple(entry))

    conn.commit()

def checklogindetails(entered_username, entered_password):
    cursor.execute('SELECT username, password, Staff_name FROM StaffID')
    temp = cursor.fetchall()
    for record in temp:
        if entered_username == record[0] and entered_password == record[1]:
            return [record[0], record[2]]
    return None

def restart_StaffID_table():
    cursor.execute('DROP TABLE IF EXISTS StaffID')
    conn.commit()
    create_StaffID_table()
    print("Reset required, StaffID DB reset successful")

# Ensure table exists before querying
create_StaffID_table()

# check content
cursor.execute('SELECT * FROM StaffID')
temp = len(cursor.fetchall())

if temp == len(login_details):
    print("Connection to StaffID successful, no restart required")
else:
    restart_StaffID_table()




