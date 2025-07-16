import sqlite3

RoomNames = [
    "AL1","AL2","AL3","AL4","AL5","AL6","AL7","AL8",
    "AU1","AU2","AU3","AU4","AU5","AU6","AU7","AU8",
    "BL1","BL2","BL3","BL4","BL5","BL6","BL7","BL8",
    "BU1","BU2","BU3","BU4","BU5","BU6","BU7","BU8",
    "CL1","CL2","CL3","CL4","CL5","CL6","CL7","CL8",
    "CU1","CU2","CU3","CU4","CU5","CU6","CU7","CU8",
    "ML1","ML2","ML3","ML4","ML5","ML6","ML7","ML8",
    "MU1","MU2","MU3","MU4","MU5","MU6","MU7","MU8",
    "PL1","PL2","PL3","PL4","PL5","PL6","PL7","PL8",
    "PU1","PU2","PU3","PU4","PU5","PU6","PU7","PU8"
]

# connecting
conn = sqlite3.connect('RoomID.db')
cursor = conn.cursor()

def create_RoomNames_table(RoomNames):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS RoomID(
        RoomName TEXT PRIMARY KEY,
        Faculty TEXT,
        ComputerRoom REAL
    );''')

    for room in RoomNames:
        query = '''INSERT OR IGNORE INTO RoomID (RoomName, Faculty) VALUES (?, ?)'''
        cursor.execute(query, (room, room[0]))

    conn.commit()

def restart_RoomID_table():
    cursor.execute('DROP TABLE IF EXISTS RoomID')
    conn.commit()
    create_RoomNames_table(RoomNames)
    print("Reset required, Room DB reset successful")

#  Ensure table is created before querying
create_RoomNames_table(RoomNames)


cursor.execute('SELECT * FROM RoomID')
temp = len(cursor.fetchall())

if temp == len(RoomNames):
    print("Connection to RoomID successful, no restart required")
else:
    restart_RoomID_table()

