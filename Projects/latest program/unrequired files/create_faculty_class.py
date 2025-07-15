import tkinter as tk
from tkinter import font
from tkinter import *
if sys.version[0] == '2':
    import Tkinter as tk
else:
    import tkinter as tk
from finalSQL_DB import *
from experimenting import *

##root = tk.Tk()
##root.geometry('0x0')


def close_bttn():
    root.destroy()
    experimenting.mainpage()
    
class create_fac:
##    def __init__(self):
    
        
    def central_areas(corridor_colour):
        root.geometry('1920x2000')
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

    def COMMS(corridor_colour,bottom_classes,upper_classes,facultyname,VALUE):
        create_fac.central_areas(corridor_colour)
        ## faculty lower classrooms
        classONE = Button(root,text=bottom_classes +"1",height=10 , width=6)
        classONE.grid(row=6,column=3)
        classTWO = Button(root,text=bottom_classes +"2",height=10 , width=6)
        classTWO.grid(row=5,column=3)
        classTHREE = Button(root,text=bottom_classes +"3",height=10 , width=6)
        classTHREE.grid(row=4,column=3)
        classFOUR = Button(root,text=bottom_classes +"4",height=4 , width=6)
        classFOUR.grid(row=3,column=3)
        classFIVE = Button(root,text=bottom_classes +"5",height=4 , width=6)
        classFIVE.grid(row=3,column=5)
        classSIX = Button(root,text=bottom_classes +"6",height=10 , width=6)
        classSIX.grid(row=4,column=5)
        classSEVEN = Button(root,text=bottom_classes +"7",height=10 , width=6)
        classSEVEN.grid(row=5,column=5)
        classEIGHT = Button(root,text=bottom_classes +"8",height=10 , width=6)
        classEIGHT.grid(row=6,column=5)
            
        ## comms upper classrooms
        CUONE = Button(root,text=upper_classes +"1",height=10 , width=6)
        CUONE.grid(row=6,column=7)
        CUTWO = Button(root,text=upper_classes +"2",height=10 , width=6)
        CUTWO.grid(row=5,column=7)
        CUTHREE = Button(root,text=upper_classes +"3",height=10 , width=6)
        CUTHREE.grid(row=4,column=7)
        CUFOUR = Button(root,text=upper_classes +"4",height=4 , width=6)
        CUFOUR.grid(row=3,column=7)
        CUFIVE = Button(root,text=upper_classes +"5",height=4 , width=6)
        CUFIVE.grid(row=3,column=9)
        CUSIX = Button(root,text=upper_classes +"6" ,height=10 , width=6)
        CUSIX.grid(row=4,column=9)
        CUSEVEN = Button(root,text=upper_classes +"7",height=10 , width=6)
        CUSEVEN.grid(row=5,column=9)
        CUEIGHT = Button(root,text=upper_classes +"8",height=10 , width=6)
        CUEIGHT.grid(row=6,column=9)

        ## back button
        BACK = Button(root,text="BACK",command = close_bttn,height=1 , width=5)
        BACK.grid(row=1,column=1)
            
        


##first_number = int(input("1 - COMMS, 2 - PNS, 3 - AMID"))
##if first_number == 1:
##    mathematics.COMMS('red','CL','CU','COMMS',1)
##elif first_number == 2:
##    mathematics.COMMS('purple','PL','PU','PNS',2)
    
    
    
