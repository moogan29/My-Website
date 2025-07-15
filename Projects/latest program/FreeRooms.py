import sqlite3
import datetime
from datetime import datetime

##try:
##    cursor = sqlite3.connect('FreeRooms.db') 
##    print("opened FreeRooms.db succesffuly")
##except Exception as e:
##    print("Error during connection"+str(e))
sessions = [" ","Mon:1","Mon:2","Mon:R1","Mon:R2","Mon:3","Mon:4","Mon:5","Mon:6","Tue:1","Tue:2","Tue:R1","Tue:R2","Tue:3","Tue:4","Tue:5","Tue:6","Wed:1","Wed:2","Wed:R1","Wed:R2","Wed:3","Wed:4","Wed:5","Wed:6","Thu:1","Thu:2","Thu:R1","Thu:R2","Thu:3","Thu:4","Thu:5","Thu:6","Fri:1","Fri:2","Fri:R1","Fri:R2","Fri:3","Fri:4","Fri:5","Fri:6"]

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
    cursor.commit()



def create_FreeRoooms_rows(sessions):
    black = 'SELECT "Mon:1" FROM FreeRooms'
    row = cursor.execute(black)
    first_result = row.fetchall()
    length = len(first_result)
    if  length == 0:
        txt_file = open("NEW_freeroomdata2.txt")
        txt_data = txt_file.readlines()
        column = len(open("NEW_freeroomdata2.txt").readlines())
        freeS1=[]
        blue = txt_data[0].split(",")
        row = (len(blue)) - 1
        s = 0
        for R in range (row):
            for C in range (column):
                temp1 = txt_data[C].split(",")
                freeS1.append(temp1[R])
                    
            if len(freeS1) == column :
                while(("" in freeS1)):
                    freeS1.remove("")
                for i in range(len(freeS1)):
                    sql = """INSERT INTO FreeRooms (BookID,"{session}") VALUES(NULL, "{classroom}");"""
                    sql_command = sql.format(session=sessions[s],classroom=freeS1[i])
                    cursor.execute(sql_command)
                freeS1 = []
                s = s + 1
        cursor.commit()

        
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
    for x in range (len(result)):
        result[x] = result[x].replace(",","")
        result[x] = result[x].replace("'","")
    return result
    


##def check_monday(classroom):
##    final = []
##    monday = ['Mon:1','Mon:2','Mon:3','Mon:4','Mon:5']
##    for x in range (5):
##        result = []
##        c = db.cursor()
##        F = 1
##        blue = '''SELECT "{sessions}" FROM FreeRooms'''
##        sql_mon = blue.format(sessions = monday[x])
##        c.execute(sql_mon)
##        for row in c:
##            outrows = str(row).strip("(").strip(")")
##            if outrows != 'None,':
##                result.append(outrows)
##        for x in range (len(result)):
##            result[x] = result[x].replace(",","")
##            result[x] = result[x].replace("'","")
##        for x in range (len(result)):
##            if result[x] == classroom:
##                final.append(True)
##                F = F - 1
##        if F == 1:
##            final.append(False)
##        db.commit()
##    return final

def currentdate():
    d1 = datetime.now()
    d2 = datetime(2021,1,1)
    if  d1 < d2:
        currentdate = "01/01/21"
    else:
        d3 = d1.strftime("%d/%m/%y")
        currentdate = d3
    return currentdate


def changing_current_date(D,M):
    date = datetime(2021,M,D)
    currentdate = date.strftime("%d/%m/%y")
    return currentdate

    
def create_dayandmonth_schedule_fromcalender(currentdate):
    year = 21
    month = int(currentdate.split("/")[1])
    day = int(currentdate.split("/")[0])
    born = datetime(year, month, day)
    day = born.strftime("%A")
    final = []
    days=[]
    for y in range (5):
        day1 = str(day[0:3]+":"+str(y+1))
        days.append(day1)
    for x in range (5):
        result = []
        F = 1
        blue = '''SELECT "{sessions}" FROM FreeRooms'''
        sql_day = blue.format(sessions = days[x])
        row2 = cursor.execute(sql_day)
        c = row2.fetchall()
        for row in c:
            outrows = str(row).strip("(").strip(")")
            if outrows != 'None,':
                result.append(outrows)
        for x in range (len(result)):
            result[x] = result[x].replace(",","")
            result[x] = result[x].replace("'","")
        final.append(result)
    cursor.commit()
    return final


def find_chooseowndfates_calender(FLN,session_number):
    times=["8:40-9:40","9:40-10:40","11:30-12:30","12:30-14:00","14:00-15:00"]
    for x in range(len(times)):
        if session_number == times[x]:
            number = x + 1
    final = []
    days = ["Mon:","Tue:","Wed:","Thu:","Fri:"]
    lessons = []
    for x in range(5):
        day = (days[x]+str(number))
        blue = '''SELECT "{sessions}" FROM FreeRooms'''
        sql_day = blue.format(sessions = day)
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
            lessons[x][y] = lessons[x][y].replace(",","")
            lessons[x][y] = lessons[x][y].replace("'","")
            if lessons[x][y] == FLN:
                for i in range(5):
                    if days[i] ==  lessons[x][0][:4]:
                        if i == 0:
                            final.append('Monday')
                        if i == 1:
                            final.append('Tuesday')
                        if i == 2:
                            final.append('Wednesday')
                        if i == 3:
                            final.append('Thursday')
                        if i == 4:
                            final.append('Friday')
    return final
            
    

    

##def altering_DB(classroom,x):
##    monday = ['Mon:1','Mon:2','Mon:3','Mon:4','Mon:5']
##    
##    query = '''DELETE FROM Book WHERE "{session}" = "{classe}"'''
##    query_con = query.format(session = monday[x], classe = classroom)
##    cursor.execute(query_con)
##
##    result2 = []
##    blue = '''SELECT "{session}" FROM Book'''
##    sql_comm = blue.format(session=monday[x])
##    cursor.execute(sql_comm)
##    for row in cursor:
##        outrows = str(row).strip("(").strip(")")
##        if outrows != 'None,':
##            result2.append(outrows)
##    for x in range (len(result2)):
##        result2[x] = result2[x].replace(",","")
##        result2[x] = result2[x].replace("'","")
##    print(result2)
     
    
####def findallavailablerooms():
##
##def restart_FreeRooms_table():               
##    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='FreeRooms' ''')
##    if cursor.fetchone()[0] == 1 :
##        print("freerooms restarted")
##        delete = '''DROP TABLE FreeRooms'''
##        cursor.execute(delete)
##        create_FreeRoooms_table(sessions)
##        create_FreeRoooms_rows(sessions)
##
##    else:
##        create_FreeRoooms_table(sessions)
##        create_FreeRoooms_rows(sessions)


def restart_FreeRooms_table():
    cursor.execute('DROP TABLE FreeRooms')
    cursor.commit()
    create_FreeRoooms_table(sessions)
    create_FreeRoooms_rows(sessions)
    print("Reset required, FreeRooms DB reset successful")
    

cursor = sqlite3.connect('FreeRooms.db')
##create_dayandmonth_schedule_fromcalender('01/01/2021')
##results = find_chooseowndfates_calender('CL04',)
##print(results)
##row = cursor.execute('SELECT * FROM FreeRooms')
##temp = len(row.fetchall())
##print(temp)
##cursor.commit()
##
##if temp == len(sessions):
##    print("Connection to FreeRooms successful, no restart required")
##else:
##    create_FreeRoooms_table
##    create_FreeRoooms_rows(sessions)
##    print("Reset required, Freeroom DB reset successful")



