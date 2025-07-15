import sqlite3
from tkinter import *
import tkinter as tk
import datetime
from functools import partial
from FreeRooms import *
from BookID import *
import calendar as cal
import sys

def XandY(root):
    ## X-axis
    root_label = Label(root,text="column: 0")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=0)
    root_label = Label(root,text="column: 1")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=1)
    root_label = Label(root,text="column: 2")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=2)
    root_label = Label(root,text="column: 3")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=3)
    root_label = Label(root,text="column: 4")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=4)
    root_label = Label(root,text="column: 5")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=5)
    root_label = Label(root,text="column: 6")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=6)
    root_label = Label(root,text="column: 7")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=7)
    root_label = Label(root,text="column: 8")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=8)
    root_label = Label(root,text="column: 9")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=9)
    root_label = Label(root,text="column: 10")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=10)
    root_label = Label(root,text="column: 11")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=11)
    root_label = Label(root,text="column: 12")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=12)
    root_label = Label(root,text="column: 13") 
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=13)
    root_label = Label(root,text="column: 14")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=14)
    root_label = Label(root,text="column: 15") 
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=15)
    root_label = Label(root,text="column: 16")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=16)
    root_label = Label(root,text="column: 17") 
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=17)
    root_label = Label(root,text="column: 18") 
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=18)
    root_label = Label(root,text="column: 19") 
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=19)
    root_label = Label(root,text="column: 20") 
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=0,column=20)
    
    ## Y-axis
    root_label = Label(root,text="row: 1")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=1,column=0)
    root_label = Label(root,text="row: 2" )
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=2,column=0)
    root_label = Label(root,text="row: 3")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=3,column=0)
    root_label = Label(root,text="row: 4")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=4,column=0)
    root_label = Label(root,text="row: 5")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=5,column=0)
    root_label = Label(root,text="row: 6")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=6,column=0)
    root_label = Label(root,text="row: 7")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=7,column=0)
    root_label = Label(root,text="row: 8")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=8,column=0)
    root_label = Label(root,text="row: 9")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=9,column=0)
    root_label = Label(root,text="row: 10")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=10,column=0)
    root_label = Label(root,text="row: 11")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=11,column=0)
    root_label = Label(root,text="row: 12")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=12,column=0)
    root_label = Label(root,text="row: 13")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=13,column=0)
    root_label = Label(root,text="row: 14")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=14,column=0)
    root_label = Label(root,text="row: 15")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=15,column=0)
    root_label = Label(root,text="row: 16")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=16,column=0)
    root_label = Label(root,text="row: 17")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=17,column=0)
    root_label = Label(root,text="row: 18")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=18,column=0)
    root_label = Label(root,text="row: 19")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=19,column=0)
    root_label = Label(root,text="row: 20")
    root_label.configure(width=7, height=1,background='red',foreground='black')
    root_label.grid(row=20,column=0)

################################################################ CALENDER ############################################################
def choice_Calender(root,currentdate,session_number,FLN,Staff_name):
    
    M =  int(currentdate.split("/")[1])
    D =  int(currentdate.split("/")[0])
    x =  int(currentdate.split("/")[1]) - 1
    
    def close_root():
        global calenderopen
        calenderopen = 0
        root.destroy()
        
    
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]     
    colours = ["pink","purple","white","gold","green3","light blue","indian red","orange","salmon4","white","dark blue","indigo"]
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    root.title("Calander")
    root.geometry('1920x2000')
    root.configure(background='black')
    XandY(root)

    def chosen_date(date,text5,height,count):
        u = 0
        for x in range(len(text5)):
            if text5[x] == date:
                u = 1
        if date == '':
            u = 1
        if u == 0:
            text5.append(date)


        temp3 = []
        for i in range(len(text5)):
            temp2 = text5[i].strip("[").strip(" ").strip("'").strip("]").strip("'")
            temp3.append(temp2)
        duration = int(len(temp3) / 8)
        y = 7
        
        for x in range(duration):
            height = height + 3
            temp4 =  str(temp3[y])
            temp3[y] = str(temp4+'\n')
            y = y + 8

        temp5 = str("you have chosen to book:\n")
        for m in range (len(temp3)):
            temp5 = (temp5+"  ,"+temp3[m])
            

        chosen_dates_label = Label(root,text=(str(temp5)),foreground='white',background='black',height=height,width=100)
        chosen_dates_label.grid(row=10,column=0,columnspan=20)
        
    ##################################################  FINDS DAY NAME OF START OF MONTH   
    def findDay(x):
        y = x + 1
        year = 2021
        month = y
        day = 1
        born = datetime(year, month, day)
        return born.strftime("%A")
    def findNOofdays(x):
        y = x + 1
        year = 2021
        month = y
        return cal.monthrange(year, month)[1]  
        
    def change_month_backward(x,months):
        #### creates calender
        x = x - 1
        if x == -1:
            x = 11
        
        No_ofDays = findNOofdays(x)
        day_name = findDay(x)
        list = root.grid_slaves()
        for l in list:
            l.destroy()
        for m in range (len(days)):
            if day_name == days[m]:
                L = m + 6
        month = months[x]
        colour = colours[x]
        monthnumber = x
        Month_label = Label(root,text=month,background=colour,height=1,width=8)
        Month_label.grid(row=2,column=9,columnspan=2)
        
        calender_UI(session_number,x,L,No_ofDays,colour,monthnumber)

    def change_month_forward(x,months):
        x = x + 1
        if x == 12:
            x = 0
        
        No_ofDays = findNOofdays(x)
        day_name = findDay(x)
        list = root.grid_slaves()
        for l in list:
            l.destroy()
        for m in range (len(days)):
             if day_name == days[m]:
                L = m + 6                                                              
        month = months[x]
        colour = colours[x]
        monthnumber = x
        Month_label = Label(root,text=month,background=colour,height=1,width=8)
        Month_label.grid(row=2,column=9,columnspan=2)
        calender_UI(session_number,x,L,No_ofDays,colour,monthnumber)
    
    def calender_UI(session_number,x,L,No_ofDays,colour,monthnumber):
        XandY(root)
        changeMonthbttn = Button(root,command=partial(change_month_forward,x,months),text ="-->", height = 1, width = 2)
        changeMonthbttn.grid(row=2 ,column=13)
        changeMonthbttn = Button(root,command=partial(change_month_backward,x,months),text ="<--", height = 1, width = 2)
        changeMonthbttn.grid(row=2 ,column=6)
        
        mon_label = Label(root,text="M",background=colour,height=2,width=4)
        mon_label.grid(row=3,column=6)
        tue_label = Label(root,text="T",background=colour,height=2,width=4)
        tue_label.grid(row=3,column=7)
        wed_label = Label(root,text="W",background=colour,height=2,width=4)
        wed_label.grid(row=3,column=8)
        thu_label = Label(root,text="Th",background=colour,height=2,width=4)
        thu_label.grid(row=3,column=9)
        fri_label = Label(root,text="F",background=colour,height=2,width=4)
        fri_label.grid(row=3,column=10)
        sat_label = Label(root,text="Sa",background='grey',height=2,width=4)
        sat_label.grid(row=3,column=11)
        sun_label = Label(root,text="Su",background='grey',height=2,width=4)
        sun_label.grid(row=3,column=12)
        ##################################################  FINDS DAY NAME OF START OF MONTH 








        ####### CREATING THE CALENDER BUTTONS
        def create_day_buttons(L,No_ofDays,monthnumber):
            global D,M
            R = 4
            for x in range (No_ofDays):
                Q = 0
                x = x + 1
                D = x
                M = monthnumber + 1    
                day_name = datetime(2021,M,D) 
                if day_name.strftime("%A") == "Saturday":
                    day_bttn = Label(root, text =x,background ='grey',height = 2,width=4)
                    day_bttn.grid(row=R,column=L)
                elif day_name.strftime("%A") == "Sunday":
                    day_bttn = Label(root, text =x,background ='grey',height = 2,width=4)
                    day_bttn.grid(row=R,column=L)
                else:
                    results=find_chooseowndfates_calender(FLN,session_number)
                    for t in range(len(results)):
                        if day_name.strftime("%A") == results[t]:
                            american = day_name.strftime("%x")
                            british = (american.split("/")[1]+"/"+american.split("/")[0]+"/"+american.split("/")[2])
                            Q = check_bookings_forchoosing_dates(session_number,FLN,british)
                
                    if Q == 1:
                        day_bttn = Button(root, text =x,command=partial(chosen_date,british,text5,height,count),background ='snow',height = 2,width=4)
                        day_bttn.grid(row=R,column=L)
                    else:
                        day_label = Label(root, text =x,background ='grey',height = 2,width=4)
                        day_label.grid(row=R,column=L)
                        
                L = L + 1
                if L == 13:
                    L = 6
                    R = R + 1
            R = R + 1
            Gobutton = Button(root,command=partial(BookID_book_room_weekly,FLN,session_number,text5,currentdate,Staff_name,1),text="Book selecte dates",height=2,width=20)
            Gobutton.grid(row=7,column=13,columnspan=2)
            
        create_day_buttons(L,No_ofDays,monthnumber)
        chosen_date('',text5,height,count)

    M = findDay(x)
    for m in range(len(days)):
        if M == days[m]:
            M = m + 6
    N = findNOofdays(x)
    colour = colours[x]

    for i in range(len(months)):
        mydate = datetime(int(currentdate.split("/")[2]),int(currentdate.split("/")[1]),int(currentdate.split("/")[0]))
        if mydate.strftime("%B") == months[i]:
            monthnumber = i
    count = 0
    text5 = []
    height = 3
    Month_label = Label(root,text=months[x],background = colour,height=1,width=8)
    Month_label.grid(row=2,column=9,columnspan=2)
    calender_UI(session_number,x,M,N,colour,monthnumber)


