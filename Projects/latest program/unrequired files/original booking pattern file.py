from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry('700x700')
root.option_add("*font", "lucida 14" )
root.title("Mainpage")
root.configure(background='black')
global day,week,twoweek,threeweek
day = 0
week = 0
twoweek = 0
threeweek = 0

def backcommand():
    root.destroy()

    
def selected_date():
    global day,week,twoweek,threeweek
    if singlevar.get() == 1:
        day = 1
    else:
        day = 0
    if weekvar.get() == 1:
        week = 1
    else:
        week = 0
    if twoweekvar.get() == 1:
        twoweek = 1
    else:
        twoweek = 0
    if threeweekvar.get() == 1:
        threeweek = 1
    else:
        threeweek = 0


def next_command():
    global day,week,twoweek,threeweek
    total = day + week + twoweek + threeweek
    if total > 1:
        print("TICK ONLY 1 BITCH")
    if total < 1:
        print("YOU HAVENT TICKED ONE YET BITCH")
    if total == 1:
        print("just right")
    

top_text = Label(root,text="How often do you want to book?")
top_text.configure(width=80, height=3,background='turquoise',foreground='black')
top_text.grid(row=0,column=0,columnspan=7)

singlevar = tk.IntVar()
weekvar = tk.IntVar()
twoweekvar = tk.IntVar()
threeweekvar = tk.IntVar()

one_day = Checkbutton(root,variable=singlevar, onvalue=1, offvalue=0,command = selected_date,text="just on the selected date")
one_day.configure(width=20, height=3,background='turquoise',foreground='black')
one_day.grid(row=1,column=0,pady=10)
current_date = Label(root,text=("currently selected day"))
current_date.configure(width=20, height=3,background='turquoise',foreground='black')
current_date.grid(row=1,column=1,pady=10)                  

one_week = Checkbutton(root,variable=weekvar, onvalue=1, offvalue=0,command = selected_date,text="Every week")
one_week.configure(width=20, height=3,background='turquoise',foreground='black')
one_week.grid(row=2,column=0,pady=10)
everyweek_date = Label(root,text=("every 1 week difference dates"))
everyweek_date.configure(width=20, height=3,background='turquoise',foreground='black')
everyweek_date.grid(row=2,column=1,pady=10)

two_week = Checkbutton(root,variable=twoweekvar, onvalue=1, offvalue=0,command = selected_date,text="Every two weeks")
two_week.configure(width=20, height=3,background='turquoise',foreground='black')
two_week.grid(row=3,column=0,pady=10)
every2week_date = Label(root,text=("every 2 week difference dates"))
every2week_date.configure(width=20, height=3,background='turquoise',foreground='black')
every2week_date.grid(row=3,column=1,pady=10)

three_week = Checkbutton(root,variable=threeweekvar, onvalue=1, offvalue=0,command = selected_date,text="Every three weeks")
three_week.configure(width=20, height=3,background='turquoise',foreground='black')
three_week.grid(row=4,column=0,pady=10)
every3week_date = Label(root,text=("every 3 week difference dates"))
every3week_date.configure(width=20, height=3,background='turquoise',foreground='black')
every3week_date.grid(row=4,column=1,pady=10)

custome_dates = Label(root,text="choose dates yourself here")
custome_dates.configure(width=80,height=13,background='turquoise',foreground='black')
custome_dates.grid(row=5,column=0,columnspan=8)


backbttn = Button(root,command = backcommand,text="BACK")
backbttn.configure(width=20, height=3,background='turquoise',foreground='black')
backbttn.grid(row=6,column=0)

gobttn = Button(root,command = next_command,text="GO")
gobttn.configure(width=20, height=3,background='turquoise',foreground='black')
gobttn.grid(row=6,column=5)
