import sqlite3
login_details = [["Martin Corbishley","MCORB","cake","martin.corbishley@corbybusinessacademy.org","Computer Science"],["Heather thompson","HTHOM","cake","heather.thompson@corbybusinessacademy.org","Mathematics"]]


def create_StaffID_table():
    cursor.execute('''
CREATE TABLE StaffID(
Staff_name str,
username str,
password str,
email str,
subject str,
primary Key(Staff_name));''')

    for x in range(len(login_details)):
##        if login_details[x][0] == 'admin':
##            query = ('''INSERT INTO StaffID(username) VALUES("{username}")''')
##            query_command = query.format(username=login_details[x][0])
##            cursor.execute(query_command)
##        else:
        alter = ('''INSERT INTO StaffID (Staff_name,username,password,email,subject) VALUES ("{name}","{username}","{password}","{email}","{subject}")''')
        alter_command = alter.format(name = login_details[x][0], username=login_details[x][1],password=login_details[x][2],email=login_details[x][3],subject=login_details[x][4])
        cursor.execute(alter_command)
        cursor.commit()


def checklogindetails(entered_username,entered_password):
    row = cursor.execute('''SELECT username,password,Staff_name FROM StaffID''')
    temp = row.fetchall()
    details = []
    for x in range(len(temp)):
        if entered_username == temp[x][0]:
            if entered_password == temp[x][1]:
                details.append(temp[x][0])
                details.append(temp[x][2])
                return details
    cursor.commit()

    
    
def restart_StaffID_table():
    cursor.execute('DROP TABLE StaffID')
    cursor.commit()
    create_StaffID_table()
    print("Reset required, StaffID DB reset successful")
        
        
cursor = sqlite3.connect('StaffID.db')

row = cursor.execute('SELECT * FROM StaffID')
temp = len(row.fetchall())
cursor.commit()

if temp == len(login_details):
    print("Connection to StaffID successful, no restart required")
else:
    restart_StaffID_table()
    


