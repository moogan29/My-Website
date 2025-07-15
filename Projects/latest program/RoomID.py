import sqlite3
with sqlite3.connect('RoomID.db') as db:
    cursor =db.cursor()

RoomNames = ["AL1","AL2","AL3","AL4","AL5","AL6","AL7","AL8",
             "AU1","AU2","AU3","AU4","AU5","AU6","AU7","AU8",
             "BL1","BL2","BL3","BL4","BL5","BL6","BL7","BL8",
             "BU1","BU2","BU3","BU4","BU5","BU6","BU7","BU8",
             "CL1","CL2","CL3","CL4","CL5","CL6","CL7","CL8",
             "CU1","CU2","CU3","CU4","CU5","CU6","CU7","CU8",
             "ML1","ML2","ML3","ML4","ML5","ML6","ML7","ML8",
             "MU1","MU2","MU3","MU4","MU5","MU6","MU7","MU8",
             "PL1","PL2","PL3","PL4","PL5","PL6","PL7","PL8",
             "PU1","PU2","PU3","PU4","PU5","PU6","PU7","PU8"]

def create_RoomNames_table(RoomNames):
    cursor.execute('''
CREATE TABLE RoomID(
RoomName str,
Faculty Char,
ComputerRoom Float,
Primary Key(RoomName));''')

    for x in range (len(RoomNames)):
        Room = RoomNames[x]
        alter = ('''INSERT INTO RoomID (RoomName,Faculty) VALUES ("{room}","{faculty}")''')
        alter_command = alter.format(room = Room, faculty=Room[0])
        cursor.execute(alter_command)
        cursor.commit()


def restart_RoomID_table():
    cursor.execute('DROP TABLE RoomID')
    cursor.commit()
    create_RoomNames_table(RoomNames)
    print("Reset required, Room DB reset successful")


cursor = sqlite3.connect('RoomID.db')

row = cursor.execute('SELECT * FROM RoomID')
temp = len(row.fetchall())
cursor.commit()

if temp == len(RoomNames):
    print("Connection to RoomID successful, no restart required")
else:
    restart_RoomID_table()
    
