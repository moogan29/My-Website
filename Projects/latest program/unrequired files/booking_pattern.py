import tkinter
import datetime
from datetime import datetime
from datetime import timedelta
from functools import partial
global root6,day,week,twoweek,threeweek
root6 = tkinter.Tk()
day = tkinter.IntVar()
week = tkinter.IntVar()
twoweek = tkinter.IntVar()
threeweek = tkinter.IntVar()

def next_command(day,week,twoweek,threeweek,currentdate):
 
    total = day.get() + week.get() + twoweek.get() + threeweek.get()
    print(total)
    if total != 1:
        warning_text = tkinter.Label(root6,text="Please select only ONE option")
        warning_text.configure(width=40, height=3,background='dark blue',foreground='red')
        warning_text.grid(row=6,column=0,columnspan=20,padx=250)
    if total == 1:
        lol = 1
        if day.get() == 1:
            print (currentdate)
        if week.get() == 1:
            return findweeklydates(0,currentdate)
        if twoweek.get() == 1:
            return findweeklydates(1,currentdate)
        if threeweek.get() == 1:
            return findweekltdates(2,currentdate)

        
def findweeklydates(y,currentdate):
    final = []
    days = int(currentdate.split("/")[0])
    month = int(currentdate.split("/")[1])
    year= int(currentdate.split("/")[2])
    date1 = datetime(year, month, days)
    final = []
    if y == 0:
        adddate = timedelta(days=7)
    if y == 1:
        adddate = timedelta(days=14)
    if y == 2:
        adddate = timedelta(days=21) 
    for x in range (3):
        date2 = date1 + adddate
        newdate = (date2.strftime('%Y-%m-%d'))
        date1 = date2
        month = (newdate.split("-")[1])
        days = (newdate.split("-")[2])
        newdate2 = (str(days)+"/"+str(month)+"/20")
        final.append(newdate2)
    return final



def backcommand():
    root6.destroy()
    
def booking_pattern_choice(FLN,session_time,currentdate):
    day1 = day
    root6.geometry('900x900')
    root6.option_add("*font", "lucida 14" )
    root6.title("Mainpage")
    root6.configure(background='black')

    top_text = tkinter.Label(root6,text="How often do you want to book "+FLN+ " at "+session_time+"?")
    top_text.configure(width=80, height=3,background='turquoise',foreground='black')
    top_text.grid(row=0,column=0,columnspan=7)

    week1dates = findweeklydates(0,currentdate)
    one_day = tkinter.Checkbutton(root6,text="just on the selected date",variable=day1,onvalue=1,offvalue=0)
    one_day.configure(width=20, height=3,background='turquoise',foreground='black')
    one_day.grid(row=1,column=0,pady=10)
    current_date = tkinter.Label(root6,text=currentdate)
    current_date.configure(width=20, height=2,background='turquoise',foreground='black')
    current_date.grid(row=1,column=1,pady=10)                  

    week1dates = findweeklydates(0,currentdate)
    one_week = tkinter.Checkbutton(root6,variable=week,onvalue=1,offvalue=0,text="Every week")
    one_week.configure(width=20, height=3,background='turquoise',foreground='black')
    one_week.grid(row=2,column=0,pady=10)
    everyweek_date = tkinter.Label(root6,text=(currentdate,",",week1dates[0],",",week1dates[1],",",week1dates[2],"etc.."))
    everyweek_date.configure(width=40, height=2,background='turquoise',foreground='black')
    everyweek_date.grid(row=2,column=1,pady=10)

    week1dates = findweeklydates(1,currentdate)
    two_week = tkinter.Checkbutton(root6,variable=twoweek,onvalue=1,offvalue=0,text="Every two weeks")
    two_week.configure(width=20, height=3,background='turquoise',foreground='black')
    two_week.grid(row=3,column=0,pady=10)
    every2week_date = tkinter.Label(root6,text=(currentdate,",",week1dates[0],",",week1dates[1],",",week1dates[2],"etc.."))
    every2week_date.configure(width=40, height=2,background='turquoise',foreground='black')
    every2week_date.grid(row=3,column=1,pady=10)

    week1dates = findweeklydates(2,currentdate)
    three_week = tkinter.Checkbutton(root6,variable=threeweek,onvalue=1,offvalue=0,text="Every three weeks")
    three_week.configure(width=20, height=3,background='turquoise',foreground='black')
    three_week.grid(row=4,column=0,pady=10)
    every3week_date = tkinter.Label(root6,text=(currentdate,",",week1dates[0],",",week1dates[1],",",week1dates[2],"etc.."))
    every3week_date.configure(width=40, height=2,background='turquoise',foreground='black')
    every3week_date.grid(row=4,column=1,pady=10)

    custome_dates = tkinter.Label(root6,text="choose dates yourself here")
    custome_dates.configure(width=80,height=13,background='turquoise',foreground='black')
    custome_dates.grid(row=5,column=0,columnspan=8)

    backbttn = tkinter.Button(root6,command = backcommand,text="BACK")
    backbttn.configure(width=20, height=3,background='turquoise',foreground='black')
    backbttn.grid(row=6,column=0)
    gobttn = tkinter.Button(root6,command = partial(next_command,day,week,twoweek,threeweek,currentdate),text="GO")
    gobttn.configure(width=20, height=3,background='turquoise',foreground='black')
    gobttn.grid(row=6,column=5)



    


