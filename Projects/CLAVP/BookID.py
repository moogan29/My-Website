import sqlite3
from datetime import datetime, timedelta

# Connect correctly
conn = sqlite3.connect('BookID.db')
cursor = conn.cursor()

def create_BookID_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS BookID(
            BookNumber INTEGER PRIMARY KEY,
            RoomName TEXT,
            time TEXT,
            freq TEXT,
            Staff_name TEXT,
            FOREIGN KEY(Staff_name) REFERENCES StaffID(Staff_name),
            FOREIGN KEY(RoomName) REFERENCES RoomID(RoomName)
        );
    ''')
    conn.commit()

def check_for_outdates():
    today = datetime.now().strftime("%d/%m/%y")
    bookings = cursor.execute('SELECT BookNumber, freq FROM BookID').fetchall()

    for book_id, freq in bookings:
        dates = [d.strip().strip("'") for d in freq.strip("[]").split(",") if d.strip()]
        updated_dates = [d for d in dates if d > today]

        if not updated_dates:
            cursor.execute('DELETE FROM BookID WHERE BookNumber = ?', (book_id,))
        else:
            cursor.execute('UPDATE BookID SET freq = ? WHERE BookNumber = ?', (str(updated_dates), book_id))

    conn.commit()

def BookID_book_room_weekly(Roomname, time, frequency, currentdate, Staff_name, value):
    if value == 1:
        Booknumber = currentbooknumber() + 1
        cursor.execute(
            '''INSERT INTO BookID (BookNumber, RoomName, time, freq, Staff_name)
               VALUES (?, ?, ?, ?, ?)''',
            (Booknumber, Roomname, time, frequency, Staff_name)
        )
    else:
        Booknumber = currentbooknumber() + 1
        alldates = [currentdate]
        maxdate = datetime(2021, 12, 31)
        date = datetime.strptime(currentdate, "%d/%m/%y")

        if frequency == 'everyweek':
            delta = timedelta(days=7)
        elif frequency == 'everytwoweek':
            delta = timedelta(days=14)
        elif frequency == 'everythreeweek':
            delta = timedelta(days=21)
        elif frequency == 'singleday':
            delta = None
        else:
            return

        if delta:
            while (date := date + delta) < maxdate:
                alldates.append(date.strftime("%d/%m/%y"))

        cursor.execute(
            '''INSERT INTO BookID (BookNumber, RoomName, time, freq, Staff_name)
               VALUES (?, ?, ?, ?, ?)''',
            (Booknumber, Roomname, time, str(alldates), Staff_name)
        )
    conn.commit()

def all_bookings_fromuser(Staff_name):
    row = cursor.execute('SELECT RoomName, time, freq FROM BookID WHERE Staff_name = ?', (Staff_name,))
    return row.fetchall()

def select_bookeddates_fromcurrentbooking(currentbooknumb):
    row = cursor.execute('SELECT freq FROM BookID WHERE BookNumber = ?', (currentbooknumb,)).fetchall()
    return row

def currentbooknumber():
    row = cursor.execute('SELECT BookNumber FROM BookID').fetchall()
    return len(row)

def check_bookings(listoffreeclasses, currentdate):
    bookings = cursor.execute('SELECT BookNumber, RoomName, time, freq FROM BookID').fetchall()

    for book in bookings:
        booknumber, roomname, timeslot, freqs = book
        dates = [d.strip().strip("'") for d in freqs.strip("[]").split(",") if d.strip()]
        if currentdate in dates:
            slot_map = {
                "8:40-9:40": 0,
                "9:40-10:40": 1,
                "11:30-12:30": 2,
                "12:30-14:00": 3,
                "14:00-15:00": 4
            }
            y = slot_map.get(timeslot)
            if y is not None:
                listoffreeclasses[y] = [r for r in listoffreeclasses[y] if r != roomname]

    return listoffreeclasses

def check_bookings_forchoosing_dates(session_number, FLN, datetocheck):
    rows = cursor.execute(
        'SELECT freq FROM BookID WHERE RoomName = ? AND time = ?', (FLN, session_number)).fetchall()

    for freq in rows:
        dates = [d.strip().strip("'") for d in freq[0].strip("[]").split(",") if d.strip()]
        if datetocheck in dates:
            return 0
    return 1

def remove_booking(FLN, session_time, Staff_name, freqs):
    rows = cursor.execute(
        'SELECT BookNumber, freq FROM BookID WHERE RoomName = ? AND time = ? AND Staff_name = ?',
        (FLN, session_time, Staff_name)
    ).fetchall()

    target_freqs = [f.strip() for f in freqs.replace(" ", "").split(",")]

    for book_id, freq in rows:
        booked_freqs = [f.strip().strip("'") for f in freq.strip("[]").split(",") if f.strip()]
        if booked_freqs == target_freqs:
            cursor.execute('DELETE FROM BookID WHERE BookNumber = ?', (book_id,))
    conn.commit()

def restart_BookID_table():
    cursor.execute('DROP TABLE IF EXISTS BookID')
    conn.commit()
    create_BookID_table()
    print("Reset required, BookID DB reset successful")

# Ensure table exists before accessing
create_BookID_table()

# Safe check for table content
try:
    row = cursor.execute('SELECT * FROM BookID').fetchall()
    if row:
        print("Connection to BookID successful, no restart required")
        check_for_outdates()
    else:
        restart_BookID_table()
except sqlite3.OperationalError:
    restart_BookID_table()


##freq = ['05/01/21', '12/01/21', '19/01/21', '26/01/21', '02/02/21', '09/02/21', '16/02/21', '23/02/21', '02/03/21', '09/03/21', '16/03/21', '23/03/21', '30/03/21', '06/04/21', '13/04/21', '20/04/21', '27/04/21', '04/05/21', '11/05/21', '18/05/21', '25/05/21', '01/06/21', '08/06/21', '15/06/21', '22/06/21', '29/06/21', '06/07/21', '13/07/21', '20/07/21', '27/07/21', '03/08/21', '10/08/21', '17/08/21', '24/08/21', '31/08/21', '07/09/21', '14/09/21', '21/09/21', '28/09/21', '05/10/21', '12/10/21', '19/10/21', '26/10/21', '02/11/21', '09/11/21', '16/11/21', '23/11/21', '30/11/21', '07/12/21', '14/12/21', '21/12/21', '28/12/21', '04/01/21']
##print(freq[0])
##remove_booking('CL04','8:40-9:40','Martin Corbishley',freq)
##check_bookings_forchoosing_dates(1,'CL04','19/04/21')
##lol = [['Fri:1', 'AL02', 'AL07', 'AL08', 'AL15', 'AU08', 'AU10', 'AU11', 'BL04', 'BL05', 'CL04', 'CU06', 'DL01', 'DU06', 'LIBR', 'ML02', 'ML03', 'THEA'], ['Fri:2', 'AL07', 'AL08', 'AU02', 'AU06', 'AU11', 'BDRM', 'CL06', 'CU02', 'CU07', 'DL01', 'DU06', 'LIBR', 'ML04', 'PE02', 'PE03', 'PE04', 'THEA'], ['Fri:3', 'AL02', 'AL07', 'AU06', 'AU08', 'AU10', 'AU11', 'BDRM', 'BL04', 'BL06', 'BL07', 'CL04', 'CL06', 'CU04', 'CU05', 'DL01', 'LIBR', 'ML05', 'MU05', 'MU08', 'PU02', 'THEA'], ['Fri:4', 'AL02', 'AL07', 'AU02', 'AU08', 'BL04', 'CL03', 'CL04', 'CL06', 'CU03', 'CU05', 'DL01', 'LIBR', 'ML07', 'PE01', 'PE02', 'PE03', 'PE04', 'PL05', 'THEA'], ['Fri:5', 'AL02', 'AL07', 'AU01', 'AU06', 'AU08', 'BDRM', 'BL04', 'CL04', 'CL05', 'CL07', 'DL01', 'LIBR', 'ML02', 'MU06', 'PL05', 'THEA']]
##[['Thu:1', 'AL07', 'AL08', 'AU01', 'AU06', 'AU08', 'BDRM', 'BL04', 'BL05', 'BL07', 'BU01', 'BU02', 'DL01', 'DU06', 'LIBR', 'ML03', 'ML04', 'PL05', 'PU04', 'THEA'], ['Thu:2', 'AL07', 'AL15', 'AU06', 'AU08', 'BU04', 'CL06', 'CL07', 'DL01', 'DU06', 'DU07', 'LIBR', 'ML04', 'MU03', 'MU04', 'MU06', 'MU07', 'THEA'], ['Thu:3', 'AL02', 'AL07', 'AL08', 'AL15', 'AU01', 'AU06', 'AU08', 'AU10', 'AU11', 'BL06', 'BL07', 'CL04', 'CL07', 'CU05', 'CU07', 'DL01', 'LIBR', 'ML04', 'PE03', 'PL05', 'THEA'], ['Thu:4', 'AU08', 'CU02', 'DL01', 'DU06', 'DU07', 'DU08', 'LIBR', 'ML04', 'ML08', 'MU06', 'MU08', 'PE01', 'PE02', 'PE03', 'PE04', 'THEA'], ['Thu:5', 'AL02', 'AL08', 'AU01', 'AU08', 'BL07', 'CL04', 'CL06', 'DL01', 'DU06', 'DU07', 'LIBR', 'ML02', 'ML03', 'ML04', 'PE02', 'THEA']]
##BookID_book_room_weekly("CL04","8:40-9:40","everyweek","01/01/21","Martin Corbishley")
##check_bookings(lol,"08/01/21")



