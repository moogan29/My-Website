import sqlite3
from datetime import datetime
from datetime import timedelta


def create_BookID_table():
    cursor.execute('''
CREATE TABLE BookID(
BookNumber int,
RoomName str,
time str,
freq str,
Staff_name str,
Primary Key(BookNumber)
Foreign Key(Staff_name) REFERENCES StaffID(Staff_name)
Foreign Key(RoomName) REFERENCES RoomID(RoomName));''')
    cursor.commit()

def check_for_outdates():
    d1 = datetime.now()
    d2 = d1.strftime("%d/%m/%y")
    row2 = cursor.execute('SELECT BookNumber,freq FROM BookID')
    row = row2.fetchall()
    for i in range(len(row)):
        temp = row[i][1]
        temp2 = temp.strip("[").strip("]")
        temp3 = []
        for m in range(len(temp2.split(","))):
            temp3.append(temp2.split(",")[m].strip(" ").strip("").strip("'"))
            if temp3[-1] <= d2:
                del temp3[-1]
        number = row[i][0]
        if len(temp3) == 0:
            cursor.execute('DELETE  FROM BookID WHERE BookNumber = ?', (number,))
        cursor.execute("""Update BookID set freq = ? where BookNumber = ?""", (str(temp3), number))

    row2 = cursor.execute('SELECT * FROM BookID').fetchall()
    cursor.commit()

             
    
def BookID_book_room_weekly(Roomname,time,frequency,currentdate,Staff_name,value):
    if value == 1:
        Booknumber = currentbooknumber() + 1
        query = """INSERT INTO BookID(BookNumber,RoomName, time, freq, Staff_name) VALUES ("{B}", "{R}","{T}","{F}","{S}");"""
        val = query.format(B=int(Booknumber),R=Roomname,T=time,F=frequency,S=Staff_name)
        cursor.execute(val)
        cursor.commit()
        
    else:
        maxdate = datetime(2021,12,31)
        row2 = cursor.execute('SELECT BookNumber FROM BookID')
        row = row2.fetchall()
        Booknumber = (len(row))+1
        def weekly(adddate):
            alldates = []
            alldates.append(currentdate)
            days = int(currentdate.split("/")[0])
            month = int(currentdate.split("/")[1])
            year= 2021
            date1 = datetime(year, month, days)
            date2 = date1 +  adddate
            while date2 < maxdate:
                newdate = (date2.strftime("%d-%m-%Y"))
                month = (newdate.split("-")[1])
                days = (newdate.split("-")[0])
                newdate2 = (str(days)+"/"+str(month)+"/21")
                alldates.append(newdate2)
                date2 = date2 +  adddate
                
            
            query = """INSERT INTO BookID(BookNumber,RoomName, time, freq, Staff_name) VALUES ("{B}", "{R}","{T}","{F}","{S}");"""
            val = query.format(B=Booknumber,R=Roomname,T=time,F=alldates,S=Staff_name)
            cursor.execute(val)
            
        if frequency == 'singleday':
            query = """INSERT INTO BookID(BookNumber,RoomName, time, freq, Staff_name) VALUES ("{B}", "{R}","{T}","{F}","{S}");"""
            val = query.format(B=Booknumber,R=Roomname,T=time,F=currentdate,S=Staff_name)
            cursor.execute(val)
            
        if frequency == 'everyweek':
            adddate =  timedelta(days=7)
            weekly(adddate)
        if frequency == 'everytwoweek':
            adddate =  timedelta(days=14)
            weekly(adddate)
        if frequency == 'everythreeweek':
            adddate =  timedelta(days=21)
            weekly(adddate)
        cursor.commit()


def all_bookings_fromuser(Staff_name):
    name = str(Staff_name)
    sql = ('SELECT RoomName, time, freq FROM BookID WHERE Staff_name = ?')
    row = cursor.execute(sql,[name])
    return row.fetchall()


def select_bookeddates_fromcurrentbooking(currentbooknumb):
    sql = cursor.execute('SELECT freq FROM BookID WHERE BookNumber = ?', (currentbooknumb,)).fetchall()
    row = (sql)
    cursor.commit()
    return row

def currentbooknumber():
    row = cursor.execute('SELECT BookNumber FROM BookID')
    row2 = len(row.fetchall())
    cursor.commit()
    return (row2)
    
        
def check_bookings(listoffreeclasses,currentdate):
    row2 = cursor.execute('SELECT BookNumber,RoomName,time,freq FROM BookID')
    row = row2.fetchall()
    for i in range(len(row)):
        temp = row[i][3]
        temp2 = temp.strip("[").strip("]")
        for m in range(len(temp2.split(","))):
            temp3 = temp2.split(",")[m].strip(" ").strip("").strip("'")
            if currentdate == temp3:
                if row[i][2] == "8:40-9:40":
                    y = 0
                elif row[i][2] == "9:40-10:40":
                    y = 1
                elif row[i][2] == "11:30-12:30":
                    y = 2
                elif row[i][2] == "12:30-14:00":
                    y = 3
                elif row[i][2] == "14:00-15:00":
                    y = 4
                for x in range(len(listoffreeclasses[y])):
                        temprow = str(row[i][1]).strip("(").strip(")").strip("'").strip("'").strip(",").strip("'")
                        try:
                            if temprow == listoffreeclasses[y][x]:
                                del listoffreeclasses[y][x]
                        except IndexError:
                            pass
    cursor.commit()
    return listoffreeclasses

            
def check_bookings_forchoosing_dates(session_number,FLN,datetocheck):
    row = cursor.execute('SELECT freq FROM BookID WHERE RoomName = ? AND time = ?', (FLN, session_number)).fetchall()
    Q = 1
    for x in range(len(row)):
        row2 = row[x][0].split(",")
        for i in range(len(row2)):
            row3 = row2[i].replace("[","").replace("]","")
            row4 = row3.replace("'","").replace(" ","")
            if datetocheck == row4:
                Q = 0
    return Q

        
def remove_booking(FLN,session_time,Staff_name,freqs):
    row = cursor.execute('SELECT BookNumber, freq FROM BookID WHERE RoomName = ? AND time = ? AND Staff_name = ?', (FLN, session_time, Staff_name,)).fetchall()
    cursor.commit()
    freq2 = freqs.replace(" ","")
    freq = freq2.split(",")
    for y in range(len(row)):
        row2 = row[y][1].split(",")
        m = 0
        for x in range(len(row2)):
            row3 = row2[x].replace("[","").replace("]","")
            row4 = row3.replace("'","").replace(" ","")
            if row4 != freq[x]:
                m = 1
        if m == 0:
            cursor.execute('DELETE  FROM BookID WHERE BookNumber = ?', (row[y][0],))
            cursor.commit()
 
    cursor.commit()

def restart_BookID_table():
    cursor.execute('DROP TABLE BookID')
    cursor.commit()
    create_BookID_table()
    print("Reset required, BookID DB reset successful")


cursor = sqlite3.connect('BookID.db')
row = cursor.execute('SELECT * FROM BookID')
temp = len(row.fetchall())
cursor.commit()

if temp > 0:
    print("Connection to BookID successful, no restart required")
    check_for_outdates()
else:
    restart_BookID_table()





##freq = ['05/01/21', '12/01/21', '19/01/21', '26/01/21', '02/02/21', '09/02/21', '16/02/21', '23/02/21', '02/03/21', '09/03/21', '16/03/21', '23/03/21', '30/03/21', '06/04/21', '13/04/21', '20/04/21', '27/04/21', '04/05/21', '11/05/21', '18/05/21', '25/05/21', '01/06/21', '08/06/21', '15/06/21', '22/06/21', '29/06/21', '06/07/21', '13/07/21', '20/07/21', '27/07/21', '03/08/21', '10/08/21', '17/08/21', '24/08/21', '31/08/21', '07/09/21', '14/09/21', '21/09/21', '28/09/21', '05/10/21', '12/10/21', '19/10/21', '26/10/21', '02/11/21', '09/11/21', '16/11/21', '23/11/21', '30/11/21', '07/12/21', '14/12/21', '21/12/21', '28/12/21', '04/01/21']
##print(freq[0])
##remove_booking('CL04','8:40-9:40','Martin Corbishley',freq)
##check_bookings_forchoosing_dates(1,'CL04','19/04/21')
##lol = [['Fri:1', 'AL02', 'AL07', 'AL08', 'AL15', 'AU08', 'AU10', 'AU11', 'BL04', 'BL05', 'CL04', 'CU06', 'DL01', 'DU06', 'LIBR', 'ML02', 'ML03', 'THEA'], ['Fri:2', 'AL07', 'AL08', 'AU02', 'AU06', 'AU11', 'BDRM', 'CL06', 'CU02', 'CU07', 'DL01', 'DU06', 'LIBR', 'ML04', 'PE02', 'PE03', 'PE04', 'THEA'], ['Fri:3', 'AL02', 'AL07', 'AU06', 'AU08', 'AU10', 'AU11', 'BDRM', 'BL04', 'BL06', 'BL07', 'CL04', 'CL06', 'CU04', 'CU05', 'DL01', 'LIBR', 'ML05', 'MU05', 'MU08', 'PU02', 'THEA'], ['Fri:4', 'AL02', 'AL07', 'AU02', 'AU08', 'BL04', 'CL03', 'CL04', 'CL06', 'CU03', 'CU05', 'DL01', 'LIBR', 'ML07', 'PE01', 'PE02', 'PE03', 'PE04', 'PL05', 'THEA'], ['Fri:5', 'AL02', 'AL07', 'AU01', 'AU06', 'AU08', 'BDRM', 'BL04', 'CL04', 'CL05', 'CL07', 'DL01', 'LIBR', 'ML02', 'MU06', 'PL05', 'THEA']]
##[['Thu:1', 'AL07', 'AL08', 'AU01', 'AU06', 'AU08', 'BDRM', 'BL04', 'BL05', 'BL07', 'BU01', 'BU02', 'DL01', 'DU06', 'LIBR', 'ML03', 'ML04', 'PL05', 'PU04', 'THEA'], ['Thu:2', 'AL07', 'AL15', 'AU06', 'AU08', 'BU04', 'CL06', 'CL07', 'DL01', 'DU06', 'DU07', 'LIBR', 'ML04', 'MU03', 'MU04', 'MU06', 'MU07', 'THEA'], ['Thu:3', 'AL02', 'AL07', 'AL08', 'AL15', 'AU01', 'AU06', 'AU08', 'AU10', 'AU11', 'BL06', 'BL07', 'CL04', 'CL07', 'CU05', 'CU07', 'DL01', 'LIBR', 'ML04', 'PE03', 'PL05', 'THEA'], ['Thu:4', 'AU08', 'CU02', 'DL01', 'DU06', 'DU07', 'DU08', 'LIBR', 'ML04', 'ML08', 'MU06', 'MU08', 'PE01', 'PE02', 'PE03', 'PE04', 'THEA'], ['Thu:5', 'AL02', 'AL08', 'AU01', 'AU08', 'BL07', 'CL04', 'CL06', 'DL01', 'DU06', 'DU07', 'LIBR', 'ML02', 'ML03', 'ML04', 'PE02', 'THEA']]
##BookID_book_room_weekly("CL04","8:40-9:40","everyweek","01/01/21","Martin Corbishley")
##check_bookings(lol,"08/01/21")



