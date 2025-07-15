import sqlite3
import tkinter
import tkinter as tk
from tkinter import font
from tkinter import *
from functools import partial
import os
import calendar as cal
import datetime
from datetime import datetime
from datetime import timedelta
import sys
if sys.version[0] == '2':
    import Tkinter as tk
else:
    import tkinter as tk
from StaffID import *
from FreeRooms import *
from RoomID import *
from BookID import *
import choose_own_dates

root = tk.Tk()
root.geometry('1920x2000')
root.option_add("*font", "lucida 14" )
root.title("Mainpage")
root.configure(background='black')

LOGGED_IN = 0
username = ("")
global mop, chop, calenderopen,currentfac,resetclasshcedule,FLN,reset_all_classes,M,D,exitFlag
currentfac = 0
resetclasshcedule = 0
reset_all_classes = 0
mop = 0
chop = 0
calenderopen = 0
FLN = "None"
M = 1
D = 1
exitFlag = False


##################################################### creating inital date and classroom schedule #############################################
def close_root():
    root.destroy()
def init_date_classroom_schedule():
    global listoffreeclasses, currentdate
    currentdate = currentdate()
    listoffreeclasse = create_dayandmonth_schedule_fromcalender(currentdate)
    listoffreeclasses = check_bookings(listoffreeclasse,currentdate)

init_date_classroom_schedule()
####################################################### BOOKING CLASSROOM SESSION ##################################################################################################
def book_room(FLN,session_time):
    rootfour = tk.Tk()
    rootfour.geometry('600x150')
    rootfour.option_add("*font", "lucida 14" )
    rootfour.title("Sign Out")
    rootfour.configure(background='grey')
    rootfour.protocol("WM_DELETE_WINDOW", disable_event)
    def NO_bttn():
        rootfour.destroy()
        
    def YES_Book_bttn(value2):
        global mop, chop, listoffreeclasses,currrentdate
        def success_bookingUI(FLN,session_time):
            global rootfive,exitFlag
            if exitFlag == True:
                rootfive.destroy()
                
            exitFlag = True
            backcommand()
            currentbook = currentbooknumber()
            booked_dates = select_bookeddates_fromcurrentbooking(currentbook)
            rootfive = tk.Tk()
            rootfive.geometry('700x150')
            rootfive.option_add("*font", "lucida 2" )
            rootfive.title("Booking Successful")
            rootfive.configure(background='black')
            rootfive.protocol("WM_DELETE_WINDOW", disable_event)
            def close_rootfive():
                global exitFlag
                exitFlag = False
                rootfive.destroy()
        
            success_booking_label = Label(rootfive,text="You have now booked "+FLN+" at "+session_time)
            success_booking_label.configure(width=40,height=2,foreground = "white",background = "black")
            success_booking_label.grid(row=0,column=1,columnspan=10,padx=50)
            success_booking_label.config(font=("lucida",17))
            close_button = Button(rootfive,text="Close",command = close_rootfive)
            close_button.configure(width=10,height=2,foreground = "white",background = "grey")
            close_button.grid(row=0,column=0,columnspan=2)
            close_button.config(font=("lucida",13))
            
            temp1 = booked_dates[0][0].split(",")
            print(temp1)
            print(len(temp1))
            if len(temp1) == 1:
                success_booking_label.grid(row=0,column=1,columnspan=10)
                temp2 = temp1[0].strip("[").strip("'").strip("]").strip("'")
                listofbookeddates = Label(rootfive,text="booked dates: "+str(temp2))
                listofbookeddates.configure(width=20,height=2,foreground = "white",background = "black")
                listofbookeddates.grid(row=1,column=1,columnspan=10)
                listofbookeddates.config(font=("lucida",17))
            else:
                temp3 = []
                for i in range(len(temp1)):
                    temp2 = temp1[i].strip("[").strip(" ").strip("'").strip("]").strip("'")
                    temp3.append(temp2)
                duration = int(len(temp3) / 8)
                fontsize = 14 - (duration/2)
                y = 7
                for x in range(duration):
                    temp4 =  str(temp3[y])
                    temp3[y] = str(temp4+'\n')
                    y = y + 8

                
                rootfive.geometry('900x210')
                temp5 = str("booked dates:\n")
                for m in range (len(temp3)):
                        temp5 = (temp5+"  ,"+temp3[m])
                        
                listofbookeddates = Label(rootfive,text=str(temp5))
                listofbookeddates.configure(width=100,height=9,foreground = "white",background = "black")
                listofbookeddates.grid(row=4,column=1,columnspan=10,rowspan=3,padx=50)
                listofbookeddates.config(font=("lucida",int(fontsize)))

                
        if LOGGED_IN == 0:
            chop = 0
            mop = 1
            bttn_LOGIN(mop)
##################################################################  BOOKING PATTERN UI 
        elif LOGGED_IN == 1:
            global currentfac,Staff_name
            if value2 == 1:
                rootfour.destroy()
                list = root.grid_slaves()
                for l in list:
                    l.destroy()
            else:
                list = root.grid_slaves()
                for l in list:
                    l.destroy()
            
            
#################################################################################################################################################
            def choice_Calender(currentdate,session_number,FLN,Staff_name):
                global text5
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
                XandY()

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
                    for m in range (len(days)):
                        if day_name == days[m]:
                            L = m + 6
                    month = months[x]
                    colour = colours[x]
                    monthnumber = x
                    YES_Book_bttn(0)
                    Month_label = Label(root,text=month,background=colour,height=1,width=8)
                    Month_label.grid(row=2,column=9,columnspan=2)
                    calender_UI(session_number,x,L,No_ofDays,colour,monthnumber)

                def change_month_forward(x,months):
                    x = x + 1
                    if x == 12:
                        x = 0
    
                    No_ofDays = findNOofdays(x)
                    day_name = findDay(x)
                    for m in range (len(days)):
                         if day_name == days[m]:
                            L = m + 6                                                              
                    month = months[x]
                    colour = colours[x]
              
                    monthnumber = x
                   
                    YES_Book_bttn(0)
                    Month_label = Label(root,text=month,background=colour,height=1,width=8)
                    Month_label.grid(row=2,column=9,columnspan=2)
                    calender_UI(session_number,x,L,No_ofDays,colour,monthnumber)
                
                def calender_UI(session_number,x,L,No_ofDays,colour,monthnumber):
                    XandY()
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
                    ##################################################  check booked rooms arent empty
                    def check_non_emptybookings(FLN,session_number,text5,currentdate,Staff_name):
                        if len(text5) == 0:
                            warning_text = tkinter.Label(root,text="You have not selected any dates to book!")
                            warning_text.configure(width=50, height=3,background='black',foreground='red')
                            warning_text.grid(row=8,column=0,columnspan=5,rowspan=3)
                            warning_text.config(font=("lucida",20))
                        else:
                            BookID_book_room_weekly(FLN,session_number,text5,currentdate,Staff_name,1)
                            success_bookingUI(FLN,session_time)

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
##                        Gobutton = Button(root,command=partial(check_non_emptybookings,FLN,session_number,text5,currentdate,Staff_name),text="Book selected dates",height=2,width=20)
##                        Gobutton.grid(row=7,column=13,columnspan=2)
                        
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
                if value2 == 1:
                    Month_label = Label(root,text=months[x],background = colour,height=1,width=8)
                    Month_label.grid(row=2,column=9,columnspan=2)
                    
                calender_UI(session_number,x,M,N,colour,monthnumber)
            if value2 == 1:
                choice_Calender(currentdate,session_time,FLN,Staff_name)
#########################################################################################################################################                
            day = IntVar()
            week = IntVar()
            twoweek = IntVar()
            threeweek = IntVar()
            
            def next_command(text5,day,week,twoweek,threeweek,currentdate):
                total = day.get() + week.get() + twoweek.get() + threeweek.get()
                print(total)
                print(len(text5))
                if total > 1:

                    if len(text5) > 0:
                        warning_text = tkinter.Label(root,text="You can either book a weekly schedule, or choose your own dates, not both")
                        warning_text.configure(width=50, height=3,background='black',foreground='red')
                        warning_text.grid(row=8,column=0,columnspan=5,rowspan=3)
                        warning_text.config(font=("lucida",20))
                    else:
                        warning_text = tkinter.Label(root,text="Please select ONE option!")
                        warning_text.configure(width=50, height=3,background='black',foreground='red')
                        warning_text.grid(row=8,column=0,columnspan=5,rowspan=3)
                        warning_text.config(font=("lucida",20))
                 
                elif total == 1:
                    if day.get() == 1:
                        global listoffreeclasses 
                        frequency = 'singleday'
                        BookID_book_room_weekly(FLN,session_time,frequency,currentdate,Staff_name,0)
                        listoffreeclasses = check_bookings(listoffreeclasses,currentdate)
                        success_bookingUI(FLN,session_time)
                    if week.get() == 1:
                        frequency = 'everyweek'
                        BookID_book_room_weekly(FLN,session_time,frequency,currentdate,Staff_name,0)
                        check_bookings(listoffreeclasses,currentdate)
                        success_bookingUI(FLN,session_time)
                    if twoweek.get() == 1:
                        frequency = 'everytwoweek'
                        BookID_book_room_weekly(FLN,session_time,frequency,currentdate,Staff_name,0)
                        check_bookings(listoffreeclasses,currentdate)
                        success_bookingUI(FLN,session_time)
                    if threeweek.get() == 1:
                        frequency = 'everythreeweek'
                        BookID_book_room_weekly(FLN,session_time,frequency,currentdate,Staff_name,0)
                        check_bookings(listoffreeclasses,currentdate)
                        success_bookingUI(FLN,session_time)

                elif len(text5) == 0:
                    if total == 0:
                        warning_text = tkinter.Label(root,text="You have not selected any dates to book!")
                        warning_text.configure(width=50, height=3,background='black',foreground='red')
                        warning_text.grid(row=8,column=0,columnspan=5,rowspan=3)
                        warning_text.config(font=("lucida",20))
                else:
                    BookID_book_room_weekly(FLN,session_time,text5,currentdate,Staff_name,1)
                    success_bookingUI(FLN,session_time)
            def backcommand():
                if currentfac == 1:
                    bttn_COMMS()
                if currentfac == 2:
                    bttn_MAIT()
                if currentfac == 3:
                    bttn_BHE()
                if currentfac == 4:
                    bttn_PNS()
                if currentfac == 5:
                    bttn_AMID()
                if reset_all_classes == 1:
                    Allavailableclasses()
                if reset_all_classes == 0 and currentfac == 1:
                    mainpage()
    
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

            
                

            XandY()
            root.option_add("*font", "lucida 14" )
            root.title("Booking room "+FLN)
            root.configure(background='black')

            top_text = tkinter.Label(root,text="How often do you want to book "+FLN+ " at "+session_time+"?\n You could choose to book a weekly schedule, or choose your own dates")
            top_text.configure(width=150, height=3,background='turquoise',foreground='black')
            top_text.grid(row=0,column=1,columnspan=14)

            week1dates = findweeklydates(0,currentdate)
            one_day = tkinter.Checkbutton(root,text="just on the selected date",variable=day,onvalue=1,offvalue=0)
            one_day.configure(width=20, height=3,background='turquoise',foreground='black')
            one_day.grid(row=2,column=1,pady=10)
            current_date = tkinter.Label(root,text=currentdate)
            current_date.configure(width=20, height=2,background='turquoise',foreground='black')
            current_date.grid(row=2,column=2,pady=10)                  

            week1dates = findweeklydates(0,currentdate)
            one_week = tkinter.Checkbutton(root,variable=week,onvalue=1,offvalue=0,text="Every week")
            one_week.configure(width=20, height=3,background='turquoise',foreground='black')
            one_week.grid(row=3,column=1,pady=10)
            everyweek_date = tkinter.Label(root,text=(currentdate,",",week1dates[0],",",week1dates[1],",",week1dates[2],"etc.."))
            everyweek_date.configure(width=40, height=2,background='turquoise',foreground='black')
            everyweek_date.grid(row=3,column=2,pady=10)

            week1dates = findweeklydates(1,currentdate)
            two_week = tkinter.Checkbutton(root,variable=twoweek,onvalue=1,offvalue=0,text="Every two weeks")
            two_week.configure(width=20, height=3,background='turquoise',foreground='black')
            two_week.grid(row=4,column=1,pady=10)
            every2week_date = tkinter.Label(root,text=(currentdate,",",week1dates[0],",",week1dates[1],",",week1dates[2],"etc.."))
            every2week_date.configure(width=40, height=2,background='turquoise',foreground='black')
            every2week_date.grid(row=4,column=2,pady=10)

            week1dates = findweeklydates(2,currentdate)
            three_week = tkinter.Checkbutton(root,variable=threeweek,onvalue=1,offvalue=0,text="Every three weeks")
            three_week.configure(width=20, height=3,background='turquoise',foreground='black')
            three_week.grid(row=5,column=1,pady=10)
            every3week_date = tkinter.Label(root,text=(currentdate,",",week1dates[0],",",week1dates[1],",",week1dates[2],"etc.."))
            every3week_date.configure(width=40, height=2,background='turquoise',foreground='black')
            every3week_date.grid(row=5,column=2,pady=10)

            backbttn = tkinter.Button(root,command = backcommand,text="BACK")
            backbttn.configure(width=20, height=3,background='turquoise',foreground='black')
            backbttn.grid(row=7,column=1)
            
            gobttn = tkinter.Button(root,command = partial(next_command,text5,day,week,twoweek,threeweek,currentdate),text="Book selected dates")
            gobttn.configure(width=25, height=3,background='turquoise',foreground='black')
            gobttn.grid(row=7,column=2)
            
##        global mop, chop
##        if LOGGED_IN == 0:
##            chop = 0
##            mop = 1
##            bttn_LOGIN(mop)
##        elif LOGGED_IN == 1:
##            array2=[]
##            list = rootfour.grid_slaves()
##            for l in list:
##                l.destroy()
##            if os.path.isfile('temp_CA.txt') == FALSE:
##                shutil.copyfile('permanantCA.txt', 'temp_CA.txt')  
##            file = open("temp_CA.txt","r+")
##            data = file.readlines()
##            array1 = (data[line_number])
##            array2 = array1.split(",")
##            array2[x] = 'FALSE'
##            data[line_number] = array2
##            for i in range(len(data)):
##                file.writelines(data[i])
##            file.close()
            
            
    CL1_session1_time = Label(rootfour,text="Would you like to book "+FLN+" at "+session_time+"?")
    CL1_session1_time.configure(width=40,height=2,background = "grey")
    CL1_session1_time.grid(row=0,column=1,columnspan=2,padx=50)
    CL1_session1_time.config(font=("lucida",17))

    YES_bttn = Button(rootfour,text="YES",command = partial(YES_Book_bttn,1))
    YES_bttn.configure(width = 5, height = 1, background = 'grey')
    YES_bttn.grid(row=1,column = 1,columnspan=2)

    NO_bttn = Button(rootfour,text="NO",command = NO_bttn)
    NO_bttn.configure(width = 5, height = 1, background = 'grey')
    NO_bttn.grid(row=1,column = 2)
        
    
############################################### CREATES CLASSROOM SCHEDULE #####################################################
def classroom_schedule(FLN):
    if FLN != "None":
        global listoffreeclasses,currentdate,resetclasshcedule
        i = 0
        columncounter = 12
        session_time=["8:40-9:40","9:40-10:40","11:30-12:30","12:30-14:00","14:00-15:00"]
        resetclasshcedule = 1
        currentdate_label = Label(root,text="currently selected date: "+currentdate,background='black',foreground = 'white',height=2,width=30,font=("lucida",30))
        currentdate_label.grid(row=5,column=8,columnspan=20)
        for y in range (5):
            TorF = False
            for x in range(len(listoffreeclasses[y])):
                if FLN == listoffreeclasses[y][x]:
                    TorF = True
            if TorF == True:
                bttn_text = "available"
                bookcolour = "green"
                available_bttn = Button(root,text=bttn_text, height=10,width=10,command=partial(book_room,FLN,session_time[i]), highlightbackground=bookcolour, fg="Black", highlightthickness=8)
                available_bttn.grid(row=4,column=columncounter)

                CL1_session1_time = Label(root,text=session_time[i])
                CL1_session1_time.configure(width=9, height=2,background=bookcolour,foreground='black')
                CL1_session1_time.grid(row=3,column=columncounter)
            else:
                bttn_text = "unavailable"
                bookcolour = "red"
                unavailable_label = Label(root,text=bttn_text, height=10,width=10, highlightbackground=bookcolour, fg="Black", highlightthickness=8)
                unavailable_label.grid(row=4,column=columncounter)

                CL1_session1_time = Label(root,text=session_time[i])
                CL1_session1_time.configure(width=9, height=2,background=bookcolour,foreground='black')
                CL1_session1_time.grid(row=3,column=columncounter)

            columncounter = columncounter + 1
            i = i + 1

            room_title = Label(root,text=FLN ,font=("Helvetica", 30))
            room_title.configure(width=5, height=2,background='black',foreground='red')
            room_title.grid(row=2,column=14)



###################################################### FUNCTION FOR X AND Y AXIS ######################################################
def XandY():

    ## X-axis
    root_label = Label(root,text="column: 0")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=0)
    root_label = Label(root,text="column: 1")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=1)
    root_label = Label(root,text="column: 2")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=2)
    root_label = Label(root,text="column: 3")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=3)
    root_label = Label(root,text="column: 4")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=4)
    root_label = Label(root,text="column: 5")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=5)
    root_label = Label(root,text="column: 6")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=6)
    root_label = Label(root,text="column: 7")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=7)
    root_label = Label(root,text="column: 8")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=8)
    root_label = Label(root,text="column: 9")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=9)
    root_label = Label(root,text="column: 10")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=10)
    root_label = Label(root,text="column: 11")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=11)
    root_label = Label(root,text="column: 12")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=12)
    root_label = Label(root,text="column: 13") 
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=13)
    root_label = Label(root,text="column: 14")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=14)
    root_label = Label(root,text="column: 15") 
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=15)
    root_label = Label(root,text="column: 16")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=16)
    root_label = Label(root,text="column: 17") 
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=17)
    root_label = Label(root,text="column: 18") 
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=18)
    root_label = Label(root,text="column: 19") 
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=19)
    root_label = Label(root,text="column: 20") 
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=0,column=20)
    
    ## Y-axis
    root_label = Label(root,text="row: 1")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=1,column=0)
    root_label = Label(root,text="row: 2" )
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=2,column=0)
    root_label = Label(root,text="row: 3")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=3,column=0)
    root_label = Label(root,text="row: 4")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=4,column=0)
    root_label = Label(root,text="row: 5")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=5,column=0)
    root_label = Label(root,text="row: 6")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=6,column=0)
    root_label = Label(root,text="row: 7")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=7,column=0)
    root_label = Label(root,text="row: 8")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=8,column=0)
    root_label = Label(root,text="row: 9")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=9,column=0)
    root_label = Label(root,text="row: 10")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=10,column=0)
    root_label = Label(root,text="row: 11")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=11,column=0)
    root_label = Label(root,text="row: 12")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=12,column=0)
    root_label = Label(root,text="row: 13")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=13,column=0)
    root_label = Label(root,text="row: 14")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=14,column=0)
    root_label = Label(root,text="row: 15")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=15,column=0)
    root_label = Label(root,text="row: 16")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=16,column=0)
    root_label = Label(root,text="row: 17")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=17,column=0)
    root_label = Label(root,text="row: 18")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=18,column=0)
    root_label = Label(root,text="row: 19")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=19,column=0)
    root_label = Label(root,text="row: 20")
    root_label.configure(width=7, height=1,background='black',foreground='black')
    root_label.grid(row=20,column=0)


################################################################ CALENDER ############################################################
def Calender_UI():
    global mop, chop,M,D,currentdate,root2,calenderopen
    if calenderopen == 1:
        root2.destroy()

    root2 = tk.Tk()
    root2.protocol("WM_DELETE_WINDOW", disable_event)
    calenderopen = 1
    M =  int(currentdate.split("/")[1])
    D =  int(currentdate.split("/")[0])
    x =  int(currentdate.split("/")[1]) - 1
    
    def close_root2():
        global calenderopen
        calenderopen = 0
        root2.destroy()
    
  
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    colours = ["pink","purple","white","gold","green3","light blue","indian red","orange","salmon4","white","dark blue","indigo"]
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    root2.title("Calander")
    root2.geometry('230x320')
    root2.configure(background='black')



    ##### channging date to view #######
    def changingdate(D,M):
        global currentdate, listoffreeclasses, FLN,currentfac,reset_all_classes,resetclasshcedule
        currentdate = changing_current_date(D,M)
        listoffreeclasse = create_dayandmonth_schedule_fromcalender(currentdate)
        listoffreeclasses = check_bookings(listoffreeclasse,currentdate)
        
        if currentfac != 0:
            print(currentfac)
            print(resetclasshcedule)
            if resetclasshcedule == 1:
                classroom_schedule(FLN)
            else:
                if currentfac == 1:
                    bttn_COMMS()
                if currentfac == 2:
                    bttn_MAIT()
                if currentfac == 3:
                    bttn_BHE()
                if currentfac == 4:
                    bttn_PNS()
                if currentfac == 5:
                    bttn_AMID()
                    
        elif reset_all_classes == 1:
            Allavailableclasses()

        else:
            mainpage()
                
    

    ####  FINDS DAY NAME OF START OF MONTH   
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
        list = root2.grid_slaves()
        for l in list:
            l.destroy()
        for m in range (len(days)):
            if day_name == days[m]:
                L = m + 1
        month = months[x]
        colour = colours[x]
        monthnumber = x
        Month_label = Label(root2,text=month,background=colour,height=1,width=8)
        Month_label.grid(row=0,column=2,columnspan=8)
   
        calender_UI(x,L,No_ofDays,colour,monthnumber)

    def change_month_forward(x,months):
        x = x + 1
        if x == 12:
            x = 0
        
        No_ofDays = findNOofdays(x)
        day_name = findDay(x)
        list = root2.grid_slaves()
        for l in list:
            l.destroy()
        for m in range (len(days)):
             if day_name == days[m]:
                L = m + 1                                                              
        month = months[x]
        colour = colours[x]
        monthnumber = x
        Month_label = Label(root2,text=month,background=colour,height=1,width=8)
        Month_label.grid(row=0,column=2,columnspan=8)
        
        calender_UI(x,L,No_ofDays,colour,monthnumber)
    
    def calender_UI(x,L,No_ofDays,colour,monthnumber):
        changeMonthbttn = Button(root2,command=partial(change_month_forward,x,months),text ="-->", height = 1, width = 2)
        changeMonthbttn.grid(row=0 ,column=9 ,columnspan = 2)
        changeMonthbttn = Button(root2,command=partial(change_month_backward,x,months),text ="<--", height = 1, width = 2)
        changeMonthbttn.grid(row=0 ,column=0 ,columnspan = 2)
        
        mon_label = Label(root2,text="M",background=colour,height=2,width=2)
        mon_label.grid(row=1,column=1)
        tue_label = Label(root2,text="T",background=colour,height=2,width=2)
        tue_label.grid(row=1,column=2)
        wed_label = Label(root2,text="W",background=colour,height=2,width=2)
        wed_label.grid(row=1,column=3)
        thu_label = Label(root2,text="Th",background=colour,height=2,width=2)
        thu_label.grid(row=1,column=4)
        fri_label = Label(root2,text="F",background=colour,height=2,width=2)
        fri_label.grid(row=1,column=5)
        sat_label = Label(root2,text="Sa",background='grey',height=2,width=2)
        sat_label.grid(row=1,column=6)
        sun_label = Label(root2,text="Su",background='grey',height=2,width=2)
        sun_label.grid(row=1,column=7)


        def create_day_buttons(L,No_ofDays,monthnumber):
            global D,M
            R = 2
            for i in range (No_ofDays):
                i = i + 1
                D = i
                M = monthnumber + 1
       
                day_name = datetime(2021,M,D) 
                if day_name.strftime("%A") == "Saturday":
                    day_bttn = Label(root2, text =i,background ='grey',height = 2,width=2)
                    day_bttn.grid(row=R,column=L)
                elif day_name.strftime("%A") == "Sunday":
                    day_bttn = Label(root2, text =i,background ='grey',height = 2,width=2)
                    day_bttn.grid(row=R,column=L)
                else:
                    day_bttn = Button(root2, text =i,command=partial(changingdate,D,M),background ='snow',height = 2,width=2)
                    day_bttn.grid(row=R,column=L)
                L = L + 1
                if L == 8:
                    L = 1
                    R = R + 1
            R = R + 1
            closebttn = Button(root2,command=close_root2, text="Close",height=2,width=5)
            closebttn.grid(row=2,column=8,columnspan=2,rowspan=5)
            
        create_day_buttons(L,No_ofDays,monthnumber)
            
##        day_bttn = Button(root2, text ="1",height =2,width=2)
##        day_bttn.grid(row=2,column=1)
##        day_bttn = Button(root2, text ="2",height =2,width=2)
##        day_bttn.grid(row=2,column=2)
##        day_bttn = Button(root2, text ="3",height =2,width=2)
##        day_bttn.grid(row=2,column=3)
##        day_bttn = Button(root2, text ="4",height =2,width=2)
##        day_bttn.grid(row=2,column=4)
##        day_bttn = Button(root2, text ="5",height =2,width=2)
##        day_bttn.grid(row=2,column=5)
##        day_bttn = Button(root2, text ="6",height =2,width=2)
##        day_bttn.grid(row=2,column=6)
##        day_bttn = Button(root2, text ="7",height =2,width=2)
##        day_bttn.grid(row=2,column=7)
##        day_bttn = Button(root2, text ="8",height =2,width=2)
##        day_bttn.grid(row=3,column=1)
##        day_bttn = Button(root2, text ="9",height =2,width=2)
##        day_bttn.grid(row=3,column=2)
##        day_bttn = Button(root2, text ="10",height =2,width=2)
##        day_bttn.grid(row=3,column=3)
##        day_bttn = Button(root2, text ="11",height =2,width=2)
##        day_bttn.grid(row=3,column=4)
##        day_bttn = Button(root2, text ="12",height =2,width=2)
##        day_bttn.grid(row=3,column=5)
##        day_bttn = Button(root2, text ="13",height =2,width=2)
##        day_bttn.grid(row=3,column=6)
##        day_bttn = Button(root2, text ="14",height =2,width=2)
##        day_bttn.grid(row=3,column=7)
##        day_bttn = Button(root2, text ="15",height =2,width=2)
##        day_bttn.grid(row=4,column=1)
##        day_bttn = Button(root2, text ="16",height =2,width=2)
##        day_bttn.grid(row=4,column=2)
##        day_bttn = Button(root2, text ="17",height =2,width=2)
##        day_bttn.grid(row=4,column=3)
##        day_bttn = Button(root2, text ="18",height =2,width=2)
##        day_bttn.grid(row=4,column=4)
##        day_bttn = Button(root2, text ="19",height =2,width=2)
##        day_bttn.grid(row=4,column=5)
##        day_bttn = Button(root2, text ="20",height =2,width=2)
##        day_bttn.grid(row=4,column=6)
##        day_bttn = Button(root2, text ="21",height =2,width=2)
##        day_bttn.grid(row=4,column=7)
##        day_bttn = Button(root2, text ="22",height =2,width=2)
##        day_bttn.grid(row=5,column=1)
##        day_bttn = Button(root2, text ="23",height =2,width=2)
##        day_bttn.grid(row=5,column=2)
##        day_bttn = Button(root2, text ="24",height =2,width=2)
##        day_bttn.grid(row=5,column=3)
##        day_bttn = Button(root2, text ="25",height =2,width=2)
##        day_bttn.grid(row=5,column=4)
##        day_bttn = Button(root2, text ="26",height =2,width=2)
##        day_bttn.grid(row=5,column=5)
##        day_bttn = Button(root2, text ="27",height =2,width=2)
##        day_bttn.grid(row=5,column=6)
##        day_bttn = Button(root2, text ="28",height =2,width=2)
##        day_bttn.grid(row=5,column=7)
##        day_bttn = Button(root2, text ="29",height =2,width=2)
##        day_bttn.grid(row=6,column=1)
##        day_bttn = Button(root2, text ="30",height =2,width=2)
##        day_bttn.grid(row=6,column=2)
##        day_bttn31 = Button(root2, text ="31",height =2,width=2)
##        day_bttn31.grid(row=6,column=3)
        
    M = findDay(x)
    for m in range(len(days)):
        if M == days[m]:
            M = m + 1
    N = findNOofdays(x)
    colour = colours[x]
    print(N)
    for i in range(len(months)):
        mydate = datetime(int(currentdate.split("/")[2]),int(currentdate.split("/")[1]),int(currentdate.split("/")[0]))
        if mydate.strftime("%B") == months[i]:
            monthnumber = i
            
    Month_label = Label(root2,text=months[x],background = colour,height=1,width=8)
    Month_label.grid(row=0,column=2,columnspan=8)
    calender_UI(x,M,N,colour,monthnumber)
######################################################### SHOW ALL BOOKINGS FOR LOGGED IN USER ####################################
def show_all_bookings():
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    XandY()
    global Staff_name
    bookings = all_bookings_fromuser(Staff_name)
    
    BACK = Button(root,text="Back", command = mainpage , height=1 , width=5)
    BACK.grid(row=1,column=1)

    staff_title = Label(root,text="All bookings under the name of  "+Staff_name,background='black',foreground = 'white',height=2,width=50,font=("lucida",40))
    staff_title.grid(row=2,column=1,columnspan=5,rowspan=2)
    
    def full_bookingdetails(FLN,session_time,freq,value3):
        global exitFlag,rootfive
        if exitFlag == True:
            rootfive.destroy()
            
        exitFlag = True
        rootfive = tk.Tk()
        rootfive.geometry('800x150')
        rootfive.option_add("*font", "lucida 2" )
        rootfive.title("Booked")
        rootfive.configure(background='black')
        rootfive.protocol("WM_DELETE_WINDOW", disable_event)

        def delete_booking(FLN,session_time,Staff_name,freq):
            global listoffreeclasses,currentdate
            remove_booking(FLN,session_time,Staff_name,freq)
            listoffreeclasse = create_dayandmonth_schedule_fromcalender(currentdate)
            listoffreeclasses = check_bookings(listoffreeclasse,currentdate)
            list = rootfive.grid_slaves()
            for l in list:
                l.destroy()
            success_delete_label = Label(rootfive,text="Successfully Deleted Booking")
            success_delete_label.configure(width=50,height=2,foreground = "white",background = "black")
            success_delete_label.grid(row=0,column=1,columnspan=10,padx=50)
            success_delete_label.config(font=("lucida",17))
            close_button = Button(rootfive,text="Close",command = close_rootfive)
            close_button.configure(width=10,height=2,foreground = "white",background = "grey")
            close_button.grid(row=0,column=0,columnspan=2)
            close_button.config(font=("lucida",13))
            show_all_bookings()
            
        
        def close_rootfive():
            global exitFlag
            exitFlag = False
            rootfive.destroy()
        if value3 == 0:
            success_booking_label = Label(rootfive,text="You have booked  "+FLN+" at "+session_time)
        else:
            success_booking_label = Label(rootfive,text="Would you like to cancel the booking of "+FLN+" at "+session_time)
        success_booking_label.configure(width=60,height=2,foreground = "white",background = "black")
        success_booking_label.grid(row=0,column=1,columnspan=10,padx=50)
        success_booking_label.config(font=("lucida",17))
        
        freq = freq.replace("[","").replace("'","").replace("]","")

        if len(freq) == 8:
                success_booking_label.grid(row=0,column=1,columnspan=10)
                listofbookeddates = Label(rootfive,text="booked dates: "+str(freq))
                listofbookeddates.configure(width=20,height=2,foreground = "white",background = "black")
                listofbookeddates.grid(row=1,column=1,columnspan=10)
                listofbookeddates.config(font=("lucida",17))
        else:
                temp3 = []
                temp2 = freq.split(",")
                for m in range(len(temp2)):
                    temp5 = temp2[m].strip("[").strip("]").strip(" ").strip("'").strip("'")
                    temp3.append(temp5)
                duration = int(len(temp3) / 8)
                y = 7
                for x in range(duration):
                    temp4 =  str(temp3[y])
                    temp3[y] = str(temp4+'\n')
                    y = y + 8
                
                rootfive.geometry('900x220')
                temp5 = str("booked dates:\n")
                for m in range (len(temp3)):
                        temp5 = (temp5+"  ,"+temp3[m])
                        
                listofbookeddates = Label(rootfive,text=str(temp5))
                listofbookeddates.configure(width=100,height=9,foreground = "white",background = "black")
                listofbookeddates.grid(row=4,column=1,columnspan=10,rowspan=3,padx=50)
                listofbookeddates.config(font=("lucida",12))
        if value3 == 0 :
            close_button = Button(rootfive,text="Close",command = close_rootfive)
            close_button.configure(width=10,height=2,foreground = "white",background = "grey")
            close_button.grid(row=0,column=0,columnspan=2)
            close_button.config(font=("lucida",13))
            cancel_button = Button(rootfive,text="Cancel booking",command = partial(full_bookingdetails,FLN,session_time,freq,1))
            cancel_button.configure(width=17,height=2,foreground = "white",background = "grey")
            cancel_button.grid(row=2,column=0,rowspan=3,columnspan=2)
            cancel_button.config(font=("lucida",13))
        else:
            yes_button = Button(rootfive,text="YES",command =partial(delete_booking,FLN,session_time,Staff_name,freq))
            yes_button.grid(row=0,column=0,columnspan=2)
            yes_button.config(font=("lucida",13),width=10,height=2,foreground = "white",background = "grey")
            no_button = Button(rootfive,text="NO",command = partial(full_bookingdetails,FLN,session_time,freq,0))
            no_button.configure(width=10,height=2,foreground = "white",background = "grey")
            no_button.grid(row=2,column=0,rowspan=3,columnspan=2)
            no_button.config(font=("lucida",13))
        
    row = 4
    column = 2
    for x in range(len(bookings)):
        single_booking = Button(root,text = (bookings[x][0]+" "+bookings[x][1]),command=partial(full_bookingdetails,bookings[x][0],bookings[x][1],bookings[x][2],0),height = 2,width=20)
        single_booking.grid(row=row,column=column,pady=10)
        row = row + 1
        if row == 14:
            row = 4
            column = column + 1
        

######################################################### ALL AVAILABLE CLASSES #################################################
def Allavailableclasses():
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    global currentdate,resetclasshcedule,reset_all_classes,listoffreeclasses,calenderopen
    resetclasshcedule = 0
    reset_all_classes = 1

    
    def create_allclass_lists(listoffreeclasses):
        global D,M
        RoomNames = ["AL01","AL02","AL03","AL04","AL05","AL06","AL07","AL08",
             "AU01","AU02","AU03","AU04","AU05","AU06","AU07","AU08",
             "BL01","BL02","BL03","BL04","BL05","BL06","BL07","BL08",
             "BU01","BU02","BU3","BU04","BU05","BU06","BU07","BU08",
             "CL01","CL02","CL03","CL04","CL05","CL06","CL07","CL08",
             "CU01","CU02","CU03","CU04","CU05","CU06","CU07","CU08",
             "ML01","ML02","ML03","ML04","ML05","ML06","ML07","ML08",
             "MU01","MU02","MU03","MU04","MU05","MU06","MU07","MU08",
             "PL01","PL02","PL03","PL04","PL05","PL06","PL07","PL08",
             "PU01","PU02","PU03","PU04","PU05","PU06","PU07","PU08"]
        setcolumn = 0
        sessiontime=["8:40-9:40","9:40-10:40","11:30-12:30","12:30-14:00","14:00-15:00"]
        colours = ["red","blue","green","orange","purple"]
        for x in range(5):
            row = 2
            session_time = sessiontime[x]
            padx = 0
            session1 = Label(root,text="SESSION"+str(x+1),background = colours[x],height=2,width=10)
            session1.grid(row=1,column=setcolumn)
            for y in range(len(listoffreeclasses[x])-1):
                y = y + 1
                check = 0
                for m in range(len(RoomNames)):
                    if RoomNames[m] == listoffreeclasses[x][y]:
                        check = 1
                if check == 1:
                    row = row + 1
                    FLN = listoffreeclasses[x][y]
                    classroom = Button(root,text =listoffreeclasses[x][y],command=partial(book_room,FLN,session_time),background =colours[x],height = 1,width=5)
                    classroom.grid(row=row,column=setcolumn)
                    if row == 24:
                        setcolumn = setcolumn + 1
                        row = 2
                        padx = 0

            
    root.title("Mainpage , All available classes")
    XandY()
        
    currentdate_label = Label(root,text="currently selected date: "+currentdate,background='black',foreground = 'white',height=2,width=50,font=("lucida",40))
    currentdate_label.grid(row=0,column=0,columnspan=22)

                            

    ## calender button
    CALbutton = Button(root,text="CALENDER", command = Calender_UI,height=3, width=20,highlightbackground="white", fg="Black", highlightthickness=20)
    CALbutton.grid(row=0,column=14,columnspan=50)
    CALbutton.configure(background='white')

    ## back button
    BACK = Button(root,text="BACK", command = mainpage , height=1 , width=5)
    BACK.grid(row=0,column=1,)
    
    create_allclass_lists(listoffreeclasses)
   

###################################################### CLASSROOM SCHEDULE ON FACULTY PAGE ##################################################################
### comms bottom classrooms ###
def CLASSEIGHT_bttn(VALUE):
    global FLN
    if VALUE == 1:
        FLN = 'CL08'
        classroom_schedule(FLN)
    if VALUE == 2:
        FLN = 'CU08'
        classroom_schedule(FLN)
    if VALUE == 3:
        FLN = 'ML08'
        classroom_schedule(FLN)
    if VALUE == 4:
        FLN = 'MU08'
        classroom_schedule(FLN)
    if VALUE == 5:
        FLN = 'BL08'
        classroom_schedule(FLN)
    if VALUE == 6:
        FLN = 'BU08'
        classroom_schedule(FLN)
    if VALUE == 7:
        FLN = 'PL08'
        classroom_schedule(FLN)
    if VALUE == 8:
        FLN = 'PU08'
        classroom_schedule(FLN)
    if VALUE == 9:
        FLN = 'AL08'
        classroom_schedule(FLN)
    if VALUE == 10:
        FLN = 'AU08'
        classroom_schedule(FLN)
        
def CLASSSEVEN_bttn(VALUE):
    global FLN
    if VALUE == 1:
        FLN = 'CL07'
        classroom_schedule(FLN)
    if VALUE == 2:
        FLN = 'CU07'
        classroom_schedule(FLN)
    if VALUE == 3:
        FLN = 'ML07'
        classroom_schedule(FLN)
    if VALUE == 4:
        FLN = 'MU07'
        classroom_schedule(FLN)
    if VALUE == 5:
        FLN = 'BL07'
        classroom_schedule(FLN)
    if VALUE == 6:
        FLN = 'BU07'
        classroom_schedule(FLN)
    if VALUE == 7:
        FLN = 'PL07'
        classroom_schedule(FLN)
    if VALUE == 8:
        FLN = 'PU07'
        classroom_schedule(FLN)
    if VALUE == 9:
        FLN = 'AL07'
        classroom_schedule(FLN)
    if VALUE == 10:
        FLN = 'AU07'
        classroom_schedule(FLN)

def CLASSSIX_bttn(VALUE):
    global FLN
    if VALUE == 1:
        FLN = 'CL06'
        classroom_schedule(FLN)
    if VALUE == 2:
        FLN = 'CU06'
        classroom_schedule(FLN)
    if VALUE == 3:
        FLN = 'ML06'
        classroom_schedule(FLN)
    if VALUE == 4:
        FLN = 'MU06'
        classroom_schedule(FLN)
    if VALUE == 5:
        FLN = 'BL06'
        classroom_schedule(FLN)
    if VALUE == 6:
        FLN = 'BU06'
        classroom_schedule(FLN)
    if VALUE == 7:
        FLN = 'PL06'
        classroom_schedule(FLN)
    if VALUE == 8:
        FLN = 'PU06'
        classroom_schedule(FLN)
    if VALUE == 9:
        FLN = 'AL06'
        classroom_schedule(FLN)
    if VALUE == 10:
        FLN = 'AU06'
        classroom_schedule(FLN)
    
def CLASSFIVE_bttn(VALUE):
    global FLN
    if VALUE == 1:
        FLN = 'CL05'
        classroom_schedule(FLN)
    if VALUE == 2:
        FLN = 'CU05'
        classroom_schedule(FLN)
    if VALUE == 3:
        FLN = 'ML05'
        classroom_schedule(FLN)
    if VALUE == 4:
        FLN = 'MU05'
        classroom_schedule(FLN)
    if VALUE == 5:
        FLN = 'BL05'
        classroom_schedule(FLN)
    if VALUE == 6:
        FLN = 'BU05'
        classroom_schedule(FLN)
    if VALUE == 7:
        FLN = 'PL05'
        classroom_schedule(FLN)
    if VALUE == 8:
        FLN = 'PU05'
        classroom_schedule(FLN)
    if VALUE == 9:
        FLN = 'AL05'
        classroom_schedule(FLN)
    if VALUE == 10:
        FLN = 'AU05'
        classroom_schedule(FLN)
    
def CLASSFOUR_bttn(VALUE):
    global FLN
    if VALUE == 1:
        FLN = 'CL04'
        classroom_schedule(FLN)
    if VALUE == 2:
        FLN = 'CU04'
        classroom_schedule(FLN)
    if VALUE == 3:
        FLN = 'ML04'
        classroom_schedule(FLN)
    if VALUE == 4:
        FLN = 'MU04'
        classroom_schedule(FLN)
    if VALUE == 5:
        FLN = 'BL04'
        classroom_schedule(FLN)
    if VALUE == 6:
        FLN = 'BU04'
        classroom_schedule(FLN)
    if VALUE == 7:
        FLN = 'PL04'
        classroom_schedule(FLN)
    if VALUE == 8:
        FLN = 'PU04'
        classroom_schedule(FLN)
    if VALUE == 9:
        FLN = 'AL04'
        classroom_schedule(FLN)
    if VALUE == 10:
        FLN = 'AU04'
        classroom_schedule(FLN)

def CLASSTHREE_bttn(VALUE):
    global FLN
    if VALUE == 1:
        FLN = 'CL03'
        classroom_schedule(FLN)
    if VALUE == 2:
        FLN = 'CU03'
        classroom_schedule(FLN)
    if VALUE == 3:
        FLN = 'ML03'
        classroom_schedule(FLN)
    if VALUE == 4:
        FLN = 'MU03'
        classroom_schedule(FLN)
    if VALUE == 5:
        FLN = 'BL03'
        classroom_schedule(FLN)
    if VALUE == 6:
        FLN = 'BU03'
        classroom_schedule(FLN)
    if VALUE == 7:
        FLN = 'PL03'
        classroom_schedule(FLN)
    if VALUE == 8:
        FLN = 'PU03'
        classroom_schedule(FLN)
    if VALUE == 9:
        FLN = 'AL03'
        classroom_schedule(FLN)
    if VALUE == 10:
        FLN = 'AU03'
        classroom_schedule(FLN)

          
def CLASSTWO_bttn(VALUE):
    global FLN
    if VALUE == 1:
        FLN = 'CL02'
        classroom_schedule(FLN)
    if VALUE == 2:
        FLN = 'CU02'
        classroom_schedule(FLN)
    if VALUE == 3:
        FLN = 'ML02'
        classroom_schedule(FLN)
    if VALUE == 4:
        FLN = 'MU02'
        classroom_schedule(FLN)
    if VALUE == 5:
        FLN = 'BL02'
        classroom_schedule(FLN)
    if VALUE == 6:
        FLN = 'BU02'
        classroom_schedule(FLN)
    if VALUE == 7:
        FLN = 'PL02'
        classroom_schedule(FLN)
    if VALUE == 8:
        FLN = 'PU02'
        classroom_schedule(FLN)
    if VALUE == 9:
        FLN = 'AL02'
        classroom_schedule(FLN)
    if VALUE == 10:
        FLN = 'AU02'
        classroom_schedule(FLN)

def CLASSONE_bttn(VALUE):
    global FLN
    if VALUE == 1:
        FLN = 'CL01'
        classroom_schedule(FLN)
    if VALUE == 2:
        FLN = 'CU01'
        classroom_schedule(FLN)
    if VALUE == 3:
        FLN = 'ML01'
        classroom_schedule(FLN)
    if VALUE == 4:
        FLN = 'MU01'
        classroom_schedule(FLN)
    if VALUE == 5:
        FLN = 'BL01'
        classroom_schedule(FLN)
    if VALUE == 6:
        FLN = 'BU01'
        classroom_schedule(FLN)
    if VALUE == 7:
        FLN = 'PL01'
        classroom_schedule(FLN)
    if VALUE == 8:
        FLN = 'PU01'
        classroom_schedule(FLN)
    if VALUE == 9:
        FLN = 'AL01'
        classroom_schedule(FLN)
    if VALUE == 10:
        FLN = 'AU01'
        classroom_schedule(FLN)
    
####################################################### CREATING FACULTY PAGE ############################################################
def create_faculty(corridor_colour,bottom_classes,upper_classes,facultyname,VALUE,VALUE2,currentdate):
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    root.geometry('1920x2000')
    root.title("Mainpage"+facultyname)
    XandY()
    
    currentdate_label = Label(root,text="currently selected date: "+currentdate,background='black',foreground = 'white',height=2,width=60,font=("lucida",30))
    currentdate_label.grid(row=5,column=8,columnspan=20)
    
    ## faculty lower central area     
    MainCorridor = Label(root,width=10, height=11,highlightthickness=0)
    MainCorridor.configure(background=corridor_colour)
    MainCorridor.grid(row=4,column=4)

    MainCorridor = Label(root,width=10, height=11,highlightthickness=0)
    MainCorridor.configure(background=corridor_colour)
    MainCorridor.grid(row=5,column=4)

    MainCorridor = Label(root,width=10, height=11,highlightthickness=0)
    MainCorridor.configure(background=corridor_colour)
    MainCorridor.grid(row=6,column=4)


    ## faculty upper central area  
    MainCorridor = Label(root,width=10, height=11,highlightthickness=0)
    MainCorridor.configure(background=corridor_colour)
    MainCorridor.grid(row=4,column=8)

    MainCorridor = Label(root,width=10, height=11,highlightthickness=0)
    MainCorridor.configure(background=corridor_colour)
    MainCorridor.grid(row=5,column=8)

    MainCorridor = Label(root,width=10, height=11,highlightthickness=0)
    MainCorridor.configure(background=corridor_colour)
    MainCorridor.grid(row=6,column=8)
    
    
    ## faculty lower classrooms
    classONE = Button(root,text=bottom_classes +"1",height=10 , width=6,command = partial(CLASSONE_bttn,VALUE))
    classONE.grid(row=6,column=3)
    classTWO = Button(root,text=bottom_classes +"2",height=10 , width=6,command = partial(CLASSTWO_bttn,VALUE))
    classTWO.grid(row=5,column=3)
    classTHREE = Button(root,text=bottom_classes +"3",height=10 , width=6,command = partial(CLASSTHREE_bttn,VALUE))
    classTHREE.grid(row=4,column=3)
    classFOUR = Button(root,text=bottom_classes +"4",height=4 , width=6,command = partial(CLASSFOUR_bttn,VALUE))
    classFOUR.grid(row=3,column=3)
    classFIVE = Button(root,text=bottom_classes +"5",height=4 , width=6,command = partial(CLASSFIVE_bttn,VALUE))
    classFIVE.grid(row=3,column=5)
    classSIX = Button(root,text=bottom_classes +"6",height=10 , width=6,command = partial(CLASSSIX_bttn,VALUE))
    classSIX.grid(row=4,column=5)
    classSEVEN = Button(root,text=bottom_classes +"7",height=10 , width=6,command = partial(CLASSSEVEN_bttn,VALUE))
    classSEVEN.grid(row=5,column=5)
    classEIGHT = Button(root,text=bottom_classes +"8",height=10 , width=6,command = partial(CLASSEIGHT_bttn,VALUE))
    classEIGHT.grid(row=6,column=5)
        
    ## comms upper classrooms
    CUONE = Button(root,text=upper_classes +"1",height=10 , width=6,command = partial(CLASSONE_bttn,VALUE2))
    CUONE.grid(row=6,column=7)
    CUTWO = Button(root,text=upper_classes +"2",height=10 , width=6,command = partial(CLASSTWO_bttn,VALUE2))
    CUTWO.grid(row=5,column=7)
    CUTHREE = Button(root,text=upper_classes +"3",height=10 , width=6,command = partial(CLASSTHREE_bttn,VALUE2))
    CUTHREE.grid(row=4,column=7)
    CUFOUR = Button(root,text=upper_classes +"4",height=4 , width=6,command = partial(CLASSFOUR_bttn,VALUE2))
    CUFOUR.grid(row=3,column=7)
    CUFIVE = Button(root,text=upper_classes +"5",height=4 , width=6,command = partial(CLASSFIVE_bttn,VALUE2))
    CUFIVE.grid(row=3,column=9)
    CUSIX = Button(root,text=upper_classes +"6" ,height=10 , width=6,command = partial(CLASSSIX_bttn,VALUE2))
    CUSIX.grid(row=4,column=9)
    CUSEVEN = Button(root,text=upper_classes +"7",height=10 , width=6,command = partial(CLASSSEVEN_bttn,VALUE2))
    CUSEVEN.grid(row=5,column=9)
    CUEIGHT = Button(root,text=upper_classes +"8",height=10 , width=6,command = partial(CLASSEIGHT_bttn,VALUE2))
    CUEIGHT.grid(row=6,column=9)

    ## back button
    BACK = Button(root,text="BACK", command = mainpage , height=1 , width=5)
    BACK.grid(row=1,column=1)

    ## Calender Button
    CALbutton = Button(root,text="CALENDER", command = Calender_UI,height=3, width=20,highlightbackground="white", fg="Black", highlightthickness=20)
    CALbutton.grid(row=6,column=15,columnspan=5)
    CALbutton.configure(background='white')


def bttn_COMMS():
    global currentfac,currentdate
    currentfac = 1
    create_faculty('red','CL','CU','COMMS',1,2,currentdate)

def bttn_MAIT():
    global currentfac
    currentfac = 2
    create_faculty('orange','ML','MU','MAIT',3,4,currentdate)

def bttn_BHE():
    global currentfac
    currentfac = 3
    create_faculty('green2','BL','BU','BHE',5,6,currentdate)   

def bttn_PNS():
    global currentfac,currentdate
    currentfac = 4
    create_faculty('purple','PL','PU','PNS',7,8,currentdate)

def bttn_AMID():
    global currentfac,currentdate
    currentfac = 5
    create_faculty('blue','AL','AU','AMID',9,10,currentdate)

############################################################# SIGN OUT PAGE #########################################################
def SIGN_OUT():
    roottwo = tk.Tk()
    roottwo.geometry('650x150')
    roottwo.option_add("*font", "lucida 14" )
    roottwo.title("Sign Out")
    roottwo.configure(background='dark grey')
    roottwo.protocol("WM_DELETE_WINDOW", disable_event)
    def NO_BTTN():
        roottwo.destroy()

    def YES_BTTN():
        global LOGGED_IN
        LOGGED_IN = 0

        list = root.grid_slaves()
        for l in list:
            l.destroy()
        mainpage()

        roottwo.destroy()

    sign_out_text = Label(roottwo,width = 55, heigh = 1, text="you are now logged in as " +username+". Are you sure you want to sign out?")
    sign_out_text.grid(row=0,column=0,columnspan = 2)
    sign_out_text.configure(background='dark grey')
    sign_out_text.config(font=("lucida",15))
    
    YES_bttn = Button(roottwo,text="YES",command = YES_BTTN,width=5,height=1)
    YES_bttn.configure(background='dark grey')
    YES_bttn.grid(row=2,column=0)

    NO_bttn = Button(roottwo,text="NO",command = NO_BTTN,width=5,height=1)
    NO_bttn.configure(background='dark grey')
    NO_bttn.grid(row=2,column=1)

    blackblock = Label(roottwo,width=1, height=1,highlightthickness=0)
    blackblock.configure(background='dark grey')
    blackblock.grid(row=1,column=0)
    

############################################################### LOGIN PAGE ####################################################################
def  bttn_LOGIN(mop):
    global LOGGED_IN
    
    def validatelogin():
        if username_enter.get() == 'ADMIN':
            restart_FreeRooms_table()
            restart_StaffID_table()
            restart_BookID_table()
            restart_RoomID_table()
            
        else:
            details = checklogindetails(username_enter.get(),password_enter.get())
            if details == None:
                logged_in = Label(roottwo,text="Incorrect login details",width=20, height=1,highlightthickness=0)
                logged_in.configure(background='dark grey')
                logged_in.grid(row=6,column=3,columnspan=2)
                
            else:
                global username, LOGGED_IN, Staff_name,resetclasshcedule,reset_all_classes
                LOGGED_IN = 1
                username = details[0]
                Staff_name = details[1]
                if reset_all_classes == 0:
                    if resetclasshcedule == 0:
                        mainpage()
                list = roottwo.grid_slaves()
                for l in list:
                    l.destroy()
                    
                roottwo.geometry('700x200')
                roottwo.protocol("WM_DELETE_WINDOW", disable_event)
                logged_in = Label(roottwo,text="you are now logged in as " + Staff_name,width=50, height=1,highlightthickness=0)
                logged_in.configure(background='dark grey')
                logged_in.grid(row=0,column=0,pady=50)
                logged_in.config(font=("lucida",20))

                BACK = Button(roottwo,text="CLOSE", command = close_page, height=1 , width=5)
                BACK.grid(row=1,column=0)
            
                
    roottwo = tk.Tk()
    roottwo.protocol("WM_DELETE_WINDOW", disable_event)
    roottwo.geometry('600x200')
    roottwo.option_add("*font", "lucida 14" )
    roottwo.title("Login")
    roottwo.configure(background='dark grey')
    
    username = Label(roottwo,text="username",width=8, height=1,highlightthickness=0)
    username.configure(background='dark grey')
    username.grid(row=3,column=2)

    password = Label(roottwo,text="password",width=8, height=1,highlightthickness=0)
    password.configure(background='dark grey')
    password.grid(row=5,column=2)

    blackblock = Label(roottwo,width=8, height=1,highlightthickness=0)
    blackblock.configure(background='dark grey')
    blackblock.grid(row=4,column=1)

    password_enter = Entry(roottwo,width=20, highlightthickness=0)
    password_enter.configure(background='white')
    password_enter.grid(row=5,column=3,padx = 10)

    username_enter = Entry(roottwo,width=20, highlightthickness=0)
    username_enter.configure(background='white')
    username_enter.grid(row=3,column=3,padx = 10)
    
    ## login button
    login_bttn = Button(roottwo,text="login",command = validatelogin,width=5,height=1)
    login_bttn.configure(background='dark grey')
    login_bttn.grid(row=6,column=2)

    if mop == 1:
        text = Label(roottwo,text="You must login to book a room. Please Login to continue.")
        text.configure(background='dark grey')
        text.grid(row=1,column=2,columnspan=3)
    


    ## close login page
    def close_page():
        roottwo.destroy()
    ## back button to close login window
    BACK = Button(roottwo,text="BACK", command = close_page, height=1 , width=5)
    BACK.grid(row=1,column=1)



############################################################ CALENDER PAGE ##################################################################
##def calender_page():
##    list = root.grid_slaves()
##    for l in list:
##        l.destroy()
##        
##    XandY()
##
##    ## session / time set
##    allavailablebutton = Button(root,command = set_session,text="session / time set", height =1,width=20,background='purple',highlightbackground="grey", fg="Black", highlightthickness=20)
##    allavailablebutton.grid(row=6,column=11,rowspan=5)
##    allavailablebutton.configure(background='yellow')
##
##    ## back button 
##    BACK = Button(root,text="BACK", command = mainpage , height=1 , width=5)
##    BACK.grid(row=1,column=1)
##
################################################################ THE MAIN PAGE ##########################################################
def mainpage():
    global chop, mop, caledneropen,resetclasshcedule,reset_all_classes,currentfac
    list = root.grid_slaves()
    for l in list:
        l.destroy()

    mop = 0
    chop = 1
    root.title("Mainpage")
 
    XandY()
    currentfac = 0
    resetclasshcedule = 0
    reset_all_classes = 0
    
    ## Calender Button
    CALbutton = Button(root,text="CALENDER", command = Calender_UI,height=3, width=20,highlightbackground="white", fg="Black", highlightthickness=20)
    CALbutton.grid(row=6,column=10)
    CALbutton.configure(background='white')

    ### currenrtly selected date title at top of screen
    currentdate_label = Label(root,text="currently selected date: "+currentdate,background='black',foreground = 'white',height=2,width=60,font=("lucida",30))
    currentdate_label.grid(row=1,column=0,columnspan=12)

    ##  corridor of school
    corridor1 = Text(root,width=15, height=10,borderwidth=0,highlightthickness=0)
    corridor1.configure(background='grey')
    corridor1.grid(row=4,column=4)

    corridor2 = Text(root,width=15, height=10,borderwidth=0,highlightthickness=0)
    corridor2.configure(background='grey')
    corridor2.grid(row=5,column=4)

    corridor3 = Text(root,width=15, height=10,borderwidth=0,highlightthickness=0)
    corridor3.configure(background='grey')
    corridor3.grid(row=6,column=4)


    ## login button
    if LOGGED_IN == 0:
        LOGINbutton = Button(root,text="LOGIN", command = partial(bttn_LOGIN,mop),height=3, width=20,highlightbackground="white", fg="Black", highlightthickness=20)
        LOGINbutton.grid(row=4,column=8)
        LOGINbutton.configure(background='white')
    ## sign out / already logged in
    elif LOGGED_IN == 1:
        LOGINbutton = Label(root,text="Logged in as " + username,height=3, width=20,highlightbackground="white", fg="Black", highlightthickness=20)
        LOGINbutton.grid(row=4,column=8)
        LOGINbutton.configure(background='white')

        Sign_out = Button(root,text="Sign out", command = SIGN_OUT,height=1, width=20,highlightbackground="white", fg="Black", highlightthickness=20)
        Sign_out.grid(row=4,column=8,rowspan=2)
        Sign_out.configure(background='white')

        all_bookings = Button(root,text="All of your bookings", command = show_all_bookings,height=1, width=20,highlightbackground="white", fg="Black", highlightthickness=20)
        all_bookings.grid(row=3,column=8)
        all_bookings.configure(background='white')
        
    ### MAIT
    MAITbutton = Button(root,text="MAIT", command = bttn_MAIT,height=5, width=20,highlightbackground="orange", fg="Black", highlightthickness=20)
    MAITbutton.grid(row=5,column=5)
    MAITbutton.configure(background='dark orange')
    ### COMMS
    COMMSbutton = Button(root,command = bttn_COMMS,text="COMMS", height=5,width=20,highlightbackground="red", fg="Black", highlightthickness=20)
    COMMSbutton.grid(row=5,column=3)
    COMMSbutton.configure(background='red')
    ### AMID
    AMIDbutton = Button(root,command = bttn_AMID,text="AMID", height =5,width=20,highlightbackground="blue", fg="Black",highlightthickness=20)
    AMIDbutton.grid(row=4,column=5)
    AMIDbutton.configure(background='blue2')
    ### BHE
    BHEbutton = Button(root,command = bttn_BHE,text="BHE", height =5,width=20,highlightbackground="green", fg="Black", highlightthickness=20)
    BHEbutton.grid(row=6,column=5)
    BHEbutton.configure(background='green2')
    ### PNS
    PNSbutton = Button(root,command = bttn_PNS,text="PNS", height =5,width=20,highlightbackground="purple", fg="Black", highlightthickness=20)
    PNSbutton.grid(row=6,column=3)
    PNSbutton.configure(background='purple')
    ## entrance to building
    entrance = Label(root,text="Entrance")
    entrance.configure(width=10, height=1,background='black',foreground='red')
    entrance.grid(row=7,column=4)

    ## close mainpage
    def close_mainpage():
        root.destroy()
        
    BACK = Button(root,text="Close", command = close_mainpage , height=1 , width=5)
    BACK.grid(row=1,column=1)
    
    ## button to list of ALL available classes
    allavailablebutton = Button(root,command = Allavailableclasses,text="ALL available classes", height =5,width=20,background='purple',highlightbackground="grey", fg="Black", highlightthickness=20)
    allavailablebutton.grid(row=4,column=10)
    allavailablebutton.configure(background='yellow')

def disable_event():
    pass

mainpage()
root.protocol("WM_DELETE_WINDOW", disable_event)
root.mainloop() 
