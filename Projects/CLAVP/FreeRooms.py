#import sqlite3
import datetime
from datetime import datetime

##try:
##    cursor = sqlite3.connect('FreeRooms.db') 
##    print("opened FreeRooms.db succesffuly")
##except Exception as e:
##    print("Error during connection"+str(e))

sessions = [" ","Mon:1","Mon:2","Mon:R1","Mon:R2","Mon:3","Mon:4","Mon:5","Mon:6",
            "Tue:1","Tue:2","Tue:R1","Tue:R2","Tue:3","Tue:4","Tue:5","Tue:6",
            "Wed:1","Wed:2","Wed:R1","Wed:R2","Wed:3","Wed:4","Wed:5","Wed:6",
            "Thu:1","Thu:2","Thu:R1","Thu:R2","Thu:3","Thu:4","Thu:5","Thu:6",
            "Fri:1","Fri:2","Fri:R1","Fri:R2","Fri:3","Fri:4","Fri:5","Fri:6"]

##with sqlite3.connect('FreeRooms.db') as db:
##    cursor = db.cursor()

def create_FreeRoooms_table(sessions):
    cursor.execute('''
CREATE TABLE FreeRooms(
BookID integer,
Primary Key(BookID));''')
    
    for m in range(len(sessions)):
        green = sessions[m]
        alter = ('''ALTER TABLE FreeRooms
        ADD "{session}" str;''')
        sql_command = alter.format(session=green)
        cursor.execute(sql_command)
    conn.commit()

def create_FreeRoooms_rows(sessions):
    black = 'SELECT "Mon:1" FROM FreeRooms'
    row = cursor.execute(black)
    first_result = row.fetchall()
    length = len(first_result)
    if length == 0:
        txt_file = open("NEW_freeroomdata2.txt")
        txt_data = txt_file.readlines()
        column = len(txt_data)
        freeS1 = []
        blue = txt_data[0].split(",")
        row = len(blue) - 1
        s = 0
        for R in range(row):
            for C in range(column):
                temp1 = txt_data[C].split(",")
                freeS1.append(temp1[R])
                    
            if len(freeS1) == column:
                while("" in freeS1):
                    freeS1.remove("")
                for i in range(len(freeS1)):
                    sql = """INSERT INTO FreeRooms (BookID,"{session}") VALUES(NULL, "{classroom}");"""
                    sql_command = sql.format(session=sessions[s], classroom=freeS1[i])
                    cursor.execute(sql_command)
                freeS1 = []
                s += 1
        conn.commit()

def finding_classroom(lesson):
    result = []
    blue = '''SELECT "{session}" FROM FreeRooms'''
    sql_comm = blue.format(session=lesson)
    row2 = cursor.execute(sql_comm)
    cursor2 = row2.fetchall()
    for row in cursor2:
        outrows = str(row).strip("(").strip(")")
        if outrows != 'None,':
            result.append(outrows)
    for x in range(len(result)):
        result[x] = result[x].replace(",", "").replace("'", "")
    return result

def currentdate():
    d1 = datetime.now()
    d2 = datetime(2021, 1, 1)
    if d1 < d2:
        currentdate = "01/01/21"
    else:
        d3 = d1.strftime("%d/%m/%y")
        currentdate = d3
    return currentdate

def changing_current_date(D, M):
    date = datetime(2021, M, D)
    currentdate = date.strftime("%d/%m/%y")
    return currentdate

def create_dayandmonth_schedule_fromcalender(currentdate):
    year = 21
    month = int(currentdate.split("/")[1])
    day = int(currentdate.split("/")[0])
    born = datetime(year, month, day)
    day = born.strftime("%A")
    final = []
    days = []
    for y in range(5):
        day1 = str(day[0:3] + ":" + str(y + 1))
        days.append(day1)
    for x in range(5):
        result = []
        F = 1
        blue = '''SELECT "{sessions}" FROM FreeRooms'''
        sql_day = blue.format(sessions=days[x])
        row2 = cursor.execute(sql_day)
        c = row2.fetchall()
        for row in c:
            outrows = str(row).strip("(").strip(")")
            if outrows != 'None,':
                result.append(outrows)
        for x in range(len(result)):
            result[x] = result[x].replace(",", "").replace("'", "")
        final.append(result)
    conn.commit()
    return final

def find_chooseowndfates_calender(FLN, session_number):
    times = ["8:40-9:40", "9:40-10:40", "11:30-12:30", "12:30-14:00", "14:00-15:00"]
    for x in range(len(times)):
        if session_number == times[x]:
            number = x + 1
    final = []
    days = ["Mon:", "Tue:", "Wed:", "Thu:", "Fri:"]
    lessons = []
    for x in range(5):
        day = (days[x] + str(number))
        blue = '''SELECT "{sessions}" FROM FreeRooms'''
        sql_day = blue.format(sessions=day)
        row2 = cursor.execute(sql_day)
        c = row2.fetchall()
        templist = []
        for y in range(len(c)):
            outrows = str(c[y]).strip("(").strip(")")
            if outrows != 'None,':
                templist.append(outrows)
        lessons.append(templist)

    for x in range(len(lessons)):
        for y in range(len(lessons[x])):
            lessons[x][y] = lessons[x][y].replace(",", "").replace("'", "")
            if lessons[x][y] == FLN:
                for i in range(5):
                    if days[i] == lessons[x][0][:4]:
                        final.append(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"][i])
    return final

def restart_FreeRooms_table():
    cursor.execute('DROP TABLE FreeRooms')
    conn.commit()
    create_FreeRoooms_table(sessions)
    create_FreeRoooms_rows(sessions)
    print("Reset required, FreeRooms DB reset successful")


### Check if FreeRooms table exists
##def check_table_exists():
##    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='FreeRooms'")
##    return cursor.fetchone() is not None
##
##    if not check_table_exists():
##        print("Table 'FreeRooms' does not exist. Creating and populating it...")
##        create_FreeRoooms_table(sessions)
##        create_FreeRoooms_rows(sessions)
##    else:
##        print("Table 'FreeRooms' exists. Proceeding...")
##
##def initialize_database():
##    if not check_table_exists():
##        print("Creating FreeRooms table...")
##        create_FreeRoooms_table(sessions)
##        create_FreeRoooms_rows(sessions)
##    else:
##        print("FreeRooms table already exists.")

# initialization 
import sqlite3
import datetime
from datetime import datetime

# Connect to the database 
conn = sqlite3.connect('FreeRooms.db')
cursor = conn.cursor()


def check_table_exists():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='FreeRooms'")
    return cursor.fetchone() is not None

def initialize_database():
    if not check_table_exists():
        print("Creating FreeRooms table...")
        create_FreeRoooms_table(sessions)
        create_FreeRoooms_rows(sessions)
    else:
        print("FreeRooms table already exists.")




initialize_database()

##create_dayandmonth_schedule_fromcalender('01/01/2021')
##results = find_chooseowndfates_calender('CL04',)
##print(results)
##row = cursor.execute('SELECT * FROM FreeRooms')
##temp = len(row.fetchall())
##print(temp)
##conn.commit()
##
##if temp == len(sessions):
##    print("Connection to FreeRooms successful, no restart required")
##else:
##    create_FreeRoooms_table()
##    create_FreeRoooms_rows(sessions)
##    print("Reset required, Freeroom DB reset successful")

