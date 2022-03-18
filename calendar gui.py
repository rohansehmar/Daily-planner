from tkinter import *
import calendar
import tkinter.font as font
from datetime import date
from datetime import datetime
import time
import tkinter.messagebox


month=0
userdate=0

#todays date
today = date.today()
date = today.strftime("%d/%m/%Y")


#current time
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")

def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

bgcolour=from_rgb((15, 70, 140)) 

root = Tk()
root.title("Calendar")
root.geometry("1300x650") #Width x Height
root.configure(bg=bgcolour) 
days_in_month = 30
first_14 = (days_in_month - 16)
last_days = days_in_month - first_14


canvastxt = Canvas(root, width=600, height=100)
canvastxt.configure(bg="grey")
canvastxt.place(x=450, y=450)
box = canvastxt.create_rectangle(2, 2, 601, 101)

photo = PhotoImage(file="blk sqr.png")
label = Label(canvastxt, image=photo)

addFont = font.Font(size=11, weight="bold")

#calendar text
myFont = font.Font(size=15)

#show time
def showTime():
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    timelabel.config(text=currentTime)
    timelabel.after(200, showTime)


def delete_event(event):
    #blank text
    blankdate=63
    f=open("blank.txt", "r+")
    blanklinenum = (blankdate - 1)
    readtxt = f.readlines() 
    blankdateline = (readtxt[blanklinenum])
    blankText = Label(canvastxt, text=(blankdateline), bg="grey", fg="white")
    addFont = font.Font(size=11, weight="bold")
    blankText["font"] = addFont
    blankText.place(x=5, y=5)
#dateline is the chosen date's corresponding line which lists all the events
    f.close()


    if month ==1:
        warning = tkinter.messagebox.askquestion("Warning", "Are you sure you want to delete all events from the selcted date")
        if warning == "yes":         
            f = open("Users\Rohan\OneDrive\Documents\python\calendar\january.txt", "r+")
            linenum = (userdate - 1)
            readtxt = f.readlines()
            dateline = (readtxt[linenum])
            
            event4file=("")
            f.close()
            
            f = open("january.txt", "r+")
            list_of_lines = f.readlines()
            list_of_lines[linenum] = (event4file)
            f.close()
            
            f = open("january.txt", "r+")
            f.writelines(list_of_lines)
            f.close()
        elif warning == "no":
            print("")

    if month ==2:
        warning = tkinter.messagebox.askquestion("Warning", "Are you sure you want to delete all events from the selcted date")
        if warning == "yes":
            f = open("february.txt", "r+")
            linenum = (userdate - 1)
            readtxt = f.readlines()
            dateline = (readtxt[linenum])
            
            event4file=("")
            f.close()
            
            f = open("february.txt", "r+")
            list_of_lines = f.readlines()
            list_of_lines[linenum] = (event4file)
            f.close()
            
            f = open("february.txt", "r+")
            f.writelines(list_of_lines)
            f.close()
        elif warning == "no":
            print("")
    if month ==3:
        warning = tkinter.messagebox.askquestion("Warning", "Are you sure you want to delete all events from the selcted date")
        if warning == "yes":
            f = open("march.txt", "r+")
            linenum = (userdate - 1)
            readtxt = f.readlines()
            dateline = (readtxt[linenum])
            
            event4file=("")
            f.close()
            
            f = open("march.txt", "r+")
            list_of_lines = f.readlines()
            list_of_lines[linenum] = (event4file)
            f.close()
            
            f = open("march.txt", "r+")
            f.writelines(list_of_lines)
            f.close()
        elif warning == "no":
            print("")

    if month ==4:
        warning = tkinter.messagebox.askquestion("Warning", "Are you sure you want to delete all events from the selcted date")
        if warning == "yes":
            f = open("april.txt", "r+")
            linenum = (userdate - 1)
            readtxt = f.readlines()
            dateline = (readtxt[linenum])
            
            event4file=("")
            f.close()
            
            f = open("april.txt", "r+")
            list_of_lines = f.readlines()
            list_of_lines[linenum] = (event4file)
            f.close()
            
            f = open("april.txt", "r+")
            f.writelines(list_of_lines)
            f.close()
        elif warning == "no":
            print("")            

    if month ==5:
        warning = tkinter.messagebox.askquestion("Warning", "Are you sure you want to delete all events from the selcted date")
        if warning == "yes":
            f = open("may.txt", "r+")
            linenum = (userdate - 1)
            readtxt = f.readlines()
            dateline = (readtxt[linenum])
            
            event4file=("")
            f.close()
            
            f = open("may.txt", "r+")
            list_of_lines = f.readlines()
            list_of_lines[linenum] = (event4file)
            f.close()
            
            f = open("may.txt", "r+")
            f.writelines(list_of_lines)
            f.close()
        elif warning == "no":
            print("")

    if month ==6:
        warning = tkinter.messagebox.askquestion("Warning", "Are you sure you want to delete all events from the selcted date")
        if warning == "yes":
            f = open("june.txt", "r+")
            linenum = (userdate - 1)
            readtxt = f.readlines()
            dateline = (readtxt[linenum])
            
            event4file=("")
            f.close()
            
            f = open("june.txt", "r+")
            list_of_lines = f.readlines()
            list_of_lines[linenum] = (event4file)
            f.close()
            
            f = open("june.txt", "r+")
            f.writelines(list_of_lines)
            f.close()
        elif warning == "no":
            print("")

    if month ==7:
        warning = tkinter.messagebox.askquestion("Warning", "Are you sure you want to delete all events from the selcted date")
        if warning == "yes":
            f = open("july.txt", "r+")
            linenum = (userdate - 1)
            readtxt = f.readlines()
            dateline = (readtxt[linenum])
            
            event4file=("")
            f.close()
            
            f = open("july.txt", "r+")
            list_of_lines = f.readlines()
            list_of_lines[linenum] = (event4file)
            f.close()
            
            f = open("july.txt", "r+")
            f.writelines(list_of_lines)
            f.close()
        elif warning == "no":
            print("")

    if month ==8:
        warning = tkinter.messagebox.askquestion("Warning", "Are you sure you want to delete all events from the selcted date")
        if warning == "yes":
            f = open("august.txt", "r+")
            linenum = (userdate - 1)
            readtxt = f.readlines()
            dateline = (readtxt[linenum])
            
            event4file=("")
            f.close()
            
            f = open("august.txt", "r+")
            list_of_lines = f.readlines()
            list_of_lines[linenum] = (event4file)
            f.close()
            
            f = open("august.txt", "r+")
            f.writelines(list_of_lines)
            f.close()
        elif warning == "no":
            print("")

    if month ==9:
        warning = tkinter.messagebox.askquestion("Warning", "Are you sure you want to delete all events from the selcted date")
        if warning == "yes":
            f = open("september.txt", "r+")
            linenum = (userdate - 1)
            readtxt = f.readlines()
            dateline = (readtxt[linenum])
            
            event4file=("")
            f.close()
            
            f = open("september.txt", "r+")
            list_of_lines = f.readlines()
            list_of_lines[linenum] = (event4file)
            f.close()
            
            f = open("september.txt", "r+")
            f.writelines(list_of_lines)
            f.close()
        elif warning == "no":
            print("")

    if month ==10:
        warning = tkinter.messagebox.askquestion("Warning", "Are you sure you want to delete all events from the selcted date")
        if warning == "yes":
            f = open("october.txt", "r+")
            linenum = (userdate - 1)
            readtxt = f.readlines()
            dateline = (readtxt[linenum])
            
            event4file=("")
            f.close()
            
            f = open("october.txt", "r+")
            list_of_lines = f.readlines()
            list_of_lines[linenum] = (event4file)
            f.close()
            
            f = open("october.txt", "r+")
            f.writelines(list_of_lines)
            f.close()
        elif warning == "no":
            print("")

    if month ==11:
        warning = tkinter.messagebox.askquestion("Warning", "Are you sure you want to delete all events from the selcted date")
        if warning == "yes":
            f = open("november.txt", "r+")
            linenum = (userdate - 1)
            readtxt = f.readlines()
            dateline = (readtxt[linenum])
            
            event4file=("")
            f.close()
            
            f = open("november.txt", "r+")
            list_of_lines = f.readlines()
            list_of_lines[linenum] = (event4file)
            f.close()
            
            f = open("november.txt", "r+")
            f.writelines(list_of_lines)
            f.close()

        elif warning == "no":
            print("")

    if month ==12:
        warning = tkinter.messagebox.askquestion("Warning", "Are you sure you want to delete all events from the selcted date")
        if warning == "yes":
            f = open("december.txt", "r+")
            linenum = (userdate - 1)
            readtxt = f.readlines()
            dateline = (readtxt[linenum])
            
            event4file=("")
            f.close()
            
            f = open("december.txt", "r+")
            list_of_lines = f.readlines()
            list_of_lines[linenum] = (event4file)
            f.close()
            
            f = open("december.txt", "r+")
            f.writelines(list_of_lines)
            f.close()
        elif warning == "no":
            print("")

def add_event(event):
    global useradd
    useradd.get()
    
    #dateline = existing text

    if month==1:
        f = open("january.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        
        event4file=useradd.get() + ", " + dateline
        f.close()
        
        f = open("january.txt", "r+")
        list_of_lines = f.readlines()
        list_of_lines[linenum] = (event4file)
        f.close()
        
        f = open("january.txt", "r+")
        f.writelines(list_of_lines)
        f.close()
                
        f=open("january.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()
        
    if month==2:
        f = open("february.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        
        event4file=useradd.get() + ", " + dateline
        f.close()
        
        f = open("february.txt", "r+")
        list_of_lines = f.readlines()
        list_of_lines[linenum] = (event4file)
        f.close()
        
        f = open("february.txt", "r+")
        f.writelines(list_of_lines)
        f.close()
                
        f=open("february.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()

    if month==3:
        f = open("march.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        
        event4file=useradd.get() + ", " + dateline
        f.close()
        
        f = open("march.txt", "r+")
        list_of_lines = f.readlines()
        list_of_lines[linenum] = (event4file)
        f.close()
        
        f = open("march.txt", "r+")
        f.writelines(list_of_lines)
        f.close()
                
        f=open("march.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()


    if month==4:
        f = open("april.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        
        event4file=useradd.get() + ", " + dateline
        f.close()
        
        f = open("april.txt", "r+")
        list_of_lines = f.readlines()
        list_of_lines[linenum] = (event4file)
        f.close()
        
        f = open("april.txt", "r+")
        f.writelines(list_of_lines)
        f.close()
                
        f=open("april.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()

    if month==5:
        f = open("may.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        
        event4file=useradd.get() + ", " + dateline
        f.close()
        
        f = open("may.txt", "r+")
        list_of_lines = f.readlines()
        list_of_lines[linenum] = (event4file)
        f.close()
        
        f = open("may.txt", "r+")
        f.writelines(list_of_lines)
        f.close()
                
        f=open("may.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()

    if month==6:
        f = open("june.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        
        event4file=useradd.get() + ", " + dateline
        f.close()
        
        f = open("june.txt", "r+")
        list_of_lines = f.readlines()
        list_of_lines[linenum] = (event4file)
        f.close()
        
        f = open("june.txt", "r+")
        f.writelines(list_of_lines)
        f.close()
                
        f=open("june.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()

    if month==7:
        f = open("july.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        
        event4file=useradd.get() + ", " + dateline
        f.close()
        
        f = open("july.txt", "r+")
        list_of_lines = f.readlines()
        list_of_lines[linenum] = (event4file)
        f.close()
        
        f = open("july.txt", "r+")
        f.writelines(list_of_lines)
        f.close()
                
        f=open("july.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()

    if month==8:
        f = open("august.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        
        event4file=useradd.get() + ", " + dateline
        f.close()
        
        f = open("august.txt", "r+")
        list_of_lines = f.readlines()
        list_of_lines[linenum] = (event4file)
        f.close()
        
        f = open("august.txt", "r+")
        f.writelines(list_of_lines)
        f.close()
                
        f=open("august.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()

    if month==9:
        f = open("september.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        
        event4file=useradd.get() + ", " + dateline
        f.close()
        
        f = open("september.txt", "r+")
        list_of_lines = f.readlines()
        list_of_lines[linenum] = (event4file)
        f.close()
        
        f = open("september.txt", "r+")
        f.writelines(list_of_lines)
        f.close()
                
        f=open("september.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()

    if month==10:
        f = open("october.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        
        event4file=useradd.get() + ", " + dateline
        f.close()
        
        f = open("october.txt", "r+")
        list_of_lines = f.readlines()
        list_of_lines[linenum] = (event4file)
        f.close()
        
        f = open("october.txt", "r+")
        f.writelines(list_of_lines)
        f.close()
                
        f=open("october.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()

    if month==11:
        f = open("november.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        
        event4file=useradd.get() + ", " + dateline
        f.close()
        
        f = open("novemebr.txt", "r+")
        list_of_lines = f.readlines()
        list_of_lines[linenum] = (event4file)
        f.close()
        
        f = open("novemebr.txt", "r+")
        f.writelines(list_of_lines)
        f.close()
                
        f=open("novemebr.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()

    if month==12:
        f = open("december.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        
        event4file=useradd.get() + ", " + dateline
        f.close()
        
        f = open("december.txt", "r+")
        list_of_lines = f.readlines()
        list_of_lines[linenum] = (event4file)
        f.close()
        
        f = open("december.txt", "r+")
        f.writelines(list_of_lines)
        f.close()
                
        f=open("december.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        blankdateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()



def event_interact(event):
    #blank text
    blankdate=63
    f=open("blank.txt", "r+")
    blanklinenum = (blankdate - 1)
    readtxt = f.readlines() 
    blankdateline = (readtxt[blanklinenum])
    blankText = Label(canvastxt, text=(blankdateline), bg="grey", fg="white")
    blankText["font"] = addFont
    blankText.place(x=5, y=5)
    #dateline is the chosen date's corresponding line which lists all the events
    f.close()

    #open file
    if month==1:
                
        f=open("january.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines() 
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        #dateline is the chosen date's corresponding line which lists all the events
        f.close()

    if month==2:
        f=open("february.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close() #dateline is the chosen date's corresponding line which lists all the events

    if month==3:
        f=open("march.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close() #dateline is the chosen date's corresponding line which lists all the events

    if month==4:
        f=open("april.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close() #dateline is the chosen date's corresponding line which lists all the events

    if month==5:
        f=open("may.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()

    if month==6:
        f=open("june.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()

    if month==7:
        f=open("july.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        #dateline is the chosen date's corresponding line which lists all the events
        f.close()

    if month==8:
        f=open("august.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        #dateline is the chosen date's corresponding line which lists all the events
        f.close()

    if month==9:
        f=open("september.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        #dateline is the chosen date's corresponding line which lists all the events
        f.close()

    if month==10:
        f=open("october.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
         #dateline is the chosen date's corresponding line which lists all the events
        f.close()

    if month==11:
        f=open("november.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()

    if month==12:
        f=open("december.txt", "r+")
        linenum = (userdate - 1)
        readtxt = f.readlines()
        dateline = (readtxt[linenum])
        eventText = Label(canvastxt, text=(dateline), bg="grey", fg="white")
        eventText["font"] = addFont
        eventText.place(x=5, y=5)
        f.close()



#creates show button
showButton = Button(root, text="SHOW", fg="black")
showButton.bind("<Button-1>", event_interact)
addButtonFont = font.Font(size=8, weight="bold")
showButton["font"] = (addButtonFont)


useradd = StringVar() 
#creates text entry
entry1=Entry(root, width=40, fg="black", relief="sunken", textvariable = useradd)
entry1.place(x=115, y=490)

#label says add event
add_event_label = Label(root, text="Add an event", bg=from_rgb((15, 70, 140)) , fg="white")
addFont = font.Font(size=11, weight="bold")
add_event_label["font"] = (addFont)
add_event_label.place(x=16, y=491)

#add button
addButton = Button(root, text="ADD", fg="black")
addButton.bind("<Button-1>", add_event)
addButtonFont = font.Font(size=8, weight="bold")
addButton["font"] = (addButtonFont)
addButton.place(x=378, y=488)

#delete button
deleteButton = Button(root, text="DELETE", fg="black")
deleteButton.bind("<Button-1>", delete_event)
deleteButtonfont = font.Font(size=11, weight="bold")
deleteButton["font"] = (deleteButtonfont)
deleteButton.place(x=1060, y=522)



def january(event):
    global month
    showButton.place(x=450, y=420)
    month=1
    
    calLabel = Label(root, text=str((calendar.month(2020, month))), bg="grey", fg="white")
    calLabel["font"] = myFont
    calLabel.place(x=550, y=117)

    #shows buttons with dates
    global userdate
    xVal=30
    yVal=200
    
    button1 = Button(root, text="1")
    button1.bind("<Button-1>", findEvent1)
    xVal=30
    yVal=200
    button1.place(x = (xVal*1)-20, y=yVal)
    
    button2 = Button(root, text="2")
    button2.bind("<Button-1>", findEvent2)
    xVal=30
    yVal=200
    button2.place(x = (xVal*2)-20, y=yVal)
    
    button3 = Button(root, text="3")
    button3.bind("<Button-1>", findEvent3)
    xVal=30
    yVal=200
    button3.place(x = (xVal*3)-20, y=yVal)

    button4 = Button(root, text="4")
    button4.bind("<Button-1>", findEvent4)
    xVal=30
    yVal=200
    button4.place(x = (xVal*4)-20, y=yVal)

    button5 = Button(root, text="5")
    button5.bind("<Button-1>", findEvent5)
    xVal=30
    yVal=200
    button5.place(x = (xVal*5)-20, y=yVal)

    button6 = Button(root, text="6")
    button6.bind("<Button-1>", findEvent6)
    xVal=30
    yVal=200
    button6.place(x = (xVal * 6) - 20, y=yVal)

    button7 = Button(root, text="7")
    button7.bind("<Button-1>", findEvent7)
    xVal=30
    yVal=200
    button7.place(x = (xVal * 7) - 20, y=yVal)

    button8 = Button(root, text="8")
    button8.bind("<Button-1>", findEvent8)
    xVal=30
    yVal=200
    button8.place(x = (xVal * 8) - 20, y=yVal)

    button9 = Button(root, text="9")
    button9.bind("<Button-1>", findEvent9)
    button9.place(x = (xVal * 9) - 20, y=yVal)

    button10 = Button(root, text="10")
    button10.bind("<Button-1>", findEvent10)
    xVal=30
    yVal=200
    button10.place(x = (xVal * 10) - 20, y=yVal)

    button11 = Button(root, text="11")
    button11.bind("<Button-1>", findEvent11)
    xVal=30
    yVal=200
    button11.place(x = (xVal * 11) - 20, y=yVal)

    button12 = Button(root, text="12")
    button12.bind("<Button-1>", findEvent12)
    xVal=30
    yVal=200
    button12.place(x = (xVal * 12) - 20, y=yVal)

    button13 = Button(root, text="13")
    button13.bind("<Button-1>", findEvent13)
    xVal=30
    yVal=200
    button13.place(x = (xVal * 13) - 20, y=yVal)

    button14 = Button(root, text="14")
    button14.bind("<Button-1>", findEvent14)
    xVal=30
    yVal=200
    button14.place(x = (xVal * 14) - 20, y=yVal)

    button15 = Button(root, text="15")
    button15.bind("<Button-1>", findEvent15)
    xVal=30
    yVal=250
    button15.place(x = (xVal * 1) - 20, y=yVal)


    button16 = Button(root, text="16")
    button16.bind("<Button-1>", findEvent16)
    xVal=30
    yVal=250
    button16.place(x = (xVal * 2) - 20, y=yVal)

    button17 = Button(root, text="17")
    button17.bind("<Button-1>", findEvent17)
    xVal=30
    yVal=250
    button17.place(x = (xVal * 3) - 20, y=yVal)

    button18 = Button(root, text="18")
    button18.bind("<Button-1>", findEvent18)
    xVal=30
    yVal=250
    button18.place(x = (xVal * 4) - 20, y=yVal)

    button19 = Button(root, text="19")
    button19.bind("<Button-1>", findEvent19)
    xVal=30
    yVal=250
    button19.place(x = (xVal * 5) - 20, y=yVal)


    button20 = Button(root, text="20")
    button20.bind("<Button-1>", findEvent20)
    xVal=30
    yVal=250
    button20.place(x = (xVal * 6) - 20, y=yVal)

    button21 = Button(root, text="21")
    button21.bind("<Button-1>", findEvent21)
    xVal=30
    yVal=250
    button21.place(x = (xVal * 7) - 20, y=yVal)


    button22 = Button(root, text="22")
    button22.bind("<Button-1>", findEvent22)
    xVal=30
    yVal=250
    button22.place(x = (xVal * 8) - 20, y=yVal)

    button23 = Button(root, text="23")
    button23.bind("<Button-1>", findEvent23)
    xVal=30
    yVal=250
    button23.place(x = (xVal * 9) - 20, y=yVal)

    button24 = Button(root, text="24")
    button24.bind("<Button-1>", findEvent24)
    xVal=30
    yVal=250
    button24.place(x = (xVal * 10) - 20, y=yVal)

    button25 = Button(root, text="25")
    button25.bind("<Button-1>", findEvent25)
    xVal=30
    yVal=250
    button25.place(x = (xVal * 11) - 20, y=yVal)

    button26 = Button(root, text="26")
    button26.bind("<Button-1>", findEvent26)
    xVal=30
    yVal=250
    button26.place(x = (xVal * 12) - 20, y=yVal)

    button27 = Button(root, text="27")
    button27.bind("<Button-1>", findEvent27)
    xVal=30
    yVal=250
    button27.place(x = (xVal * 13) - 20, y=yVal)

    button28 = Button(root, text="28")
    button28.bind("<Button-1>", findEvent28)
    xVal=30
    yVal=250
    button28.place(x = (xVal * 14) - 20, y=yVal)

    button29 = Button(root, text="29")
    button29.bind("<Button-1>", findEvent29)
    xVal=30
    yVal=300
    button29.place(x = (xVal * 1) - 20, y=yVal)

    button30 = Button(root, text="30")
    button30.bind("<Button-1>", findEvent30)
    xVal=30
    yVal=300
    button30.place(x = (xVal * 2) - 20, y=yVal)

    button31 = Button(root, text="31")
    button31.bind("<Button-1>", findEvent31)
    xVal=30
    yVal=300
    button31.place(x = (xVal * 3) - 20, y=yVal)


def february(event):
    global month
    showButton.place(x=450, y=420)
    month=2
    
    calLabel = Label(root, text=str((calendar.month(2020, month))), bg="grey", fg="white")
    calLabel["font"] = myFont
    calLabel.place(x=550, y=117)

    #shows dates
    global userdate
    xVal=30
    yVal=200
    
    button1 = Button(root, text="1")
    button1.bind("<Button-1>", findEvent1)
    xVal=30
    yVal=200
    button1.place(x = (xVal*1)-20, y=yVal)
    
    button2 = Button(root, text="2")
    button2.bind("<Button-1>", findEvent2)
    xVal=30
    yVal=200
    button2.place(x = (xVal*2)-20, y=yVal)
    
    button3 = Button(root, text="3")
    button3.bind("<Button-1>", findEvent3)
    xVal=30
    yVal=200
    button3.place(x = (xVal*3)-20, y=yVal)

    button4 = Button(root, text="4")
    button4.bind("<Button-1>", findEvent4)
    xVal=30
    yVal=200
    button4.place(x = (xVal*4)-20, y=yVal)

    button5 = Button(root, text="5")
    button5.bind("<Button-1>", findEvent5)
    xVal=30
    yVal=200
    button5.place(x = (xVal*5)-20, y=yVal)

    button6 = Button(root, text="6")
    button6.bind("<Button-1>", findEvent6)
    xVal=30
    yVal=200
    button6.place(x = (xVal * 6) - 20, y=yVal)

    button7 = Button(root, text="7")
    button7.bind("<Button-1>", findEvent7)
    xVal=30
    yVal=200
    button7.place(x = (xVal * 7) - 20, y=yVal)

    button8 = Button(root, text="8")
    button8.bind("<Button-1>", findEvent8)
    xVal=30
    yVal=200
    button8.place(x = (xVal * 8) - 20, y=yVal)

    button9 = Button(root, text="9")
    button9.bind("<Button-1>", findEvent9)
    button9.place(x = (xVal * 9) - 20, y=yVal)

    button10 = Button(root, text="10")
    button10.bind("<Button-1>", findEvent10)
    xVal=30
    yVal=200
    button10.place(x = (xVal * 10) - 20, y=yVal)

    button11 = Button(root, text="11")
    button11.bind("<Button-1>", findEvent11)
    xVal=30
    yVal=200
    button11.place(x = (xVal * 11) - 20, y=yVal)

    button12 = Button(root, text="12")
    button12.bind("<Button-1>", findEvent12)
    xVal=30
    yVal=200
    button12.place(x = (xVal * 12) - 20, y=yVal)

    button13 = Button(root, text="13")
    button13.bind("<Button-1>", findEvent13)
    xVal=30
    yVal=200
    button13.place(x = (xVal * 13) - 20, y=yVal)

    button14 = Button(root, text="14")
    button14.bind("<Button-1>", findEvent14)
    xVal=30
    yVal=200
    button14.place(x = (xVal * 14) - 20, y=yVal)

    button15 = Button(root, text="15")
    button15.bind("<Button-1>", findEvent15)
    xVal=30
    yVal=250
    button15.place(x = (xVal * 1) - 20, y=yVal)


    button16 = Button(root, text="16")
    button16.bind("<Button-1>", findEvent16)
    xVal=30
    yVal=250
    button16.place(x = (xVal * 2) - 20, y=yVal)

    button17 = Button(root, text="17")
    button17.bind("<Button-1>", findEvent17)
    xVal=30
    yVal=250
    button17.place(x = (xVal * 3) - 20, y=yVal)

    button18 = Button(root, text="18")
    button18.bind("<Button-1>", findEvent18)
    xVal=30
    yVal=250
    button18.place(x = (xVal * 4) - 20, y=yVal)

    button19 = Button(root, text="19")
    button19.bind("<Button-1>", findEvent19)
    xVal=30
    yVal=250
    button19.place(x = (xVal * 5) - 20, y=yVal)


    button20 = Button(root, text="20")
    button20.bind("<Button-1>", findEvent20)
    xVal=30
    yVal=250
    button20.place(x = (xVal * 6) - 20, y=yVal)

    button21 = Button(root, text="21")
    button21.bind("<Button-1>", findEvent21)
    xVal=30
    yVal=250
    button21.place(x = (xVal * 7) - 20, y=yVal)


    button22 = Button(root, text="22")
    button22.bind("<Button-1>", findEvent22)
    xVal=30
    yVal=250
    button22.place(x = (xVal * 8) - 20, y=yVal)

    button23 = Button(root, text="23")
    button23.bind("<Button-1>", findEvent23)
    xVal=30
    yVal=250
    button23.place(x = (xVal * 9) - 20, y=yVal)

    button24 = Button(root, text="24")
    button24.bind("<Button-1>", findEvent24)
    xVal=30
    yVal=250
    button24.place(x = (xVal * 10) - 20, y=yVal)

    button25 = Button(root, text="25")
    button25.bind("<Button-1>", findEvent25)
    xVal=30
    yVal=250
    button25.place(x = (xVal * 11) - 20, y=yVal)

    button26 = Button(root, text="26")
    button26.bind("<Button-1>", findEvent26)
    xVal=30
    yVal=250
    button26.place(x = (xVal * 12) - 20, y=yVal)

    button27 = Button(root, text="27")
    button27.bind("<Button-1>", findEvent27)
    xVal=30
    yVal=250
    button27.place(x = (xVal * 13) - 20, y=yVal)

    button28 = Button(root, text="28")
    button28.bind("<Button-1>", findEvent28)
    xVal=30
    yVal=250
    button28.place(x = (xVal * 14) - 20, y=yVal)

    button29 = Button(root, text="    ")
    button29.bind("<Button-1>")
    xVal=30
    yVal=300
    button29.place(x = (xVal * 1) - 20, y=yVal)

    button30 = Button(root, text="    ")
    button30.bind("<Button-1>")
    xVal=30
    yVal=300
    button30.place(x = (xVal * 2) - 20, y=yVal)

    button31 = Button(root, text="    ")
    button31.bind("<Button-1>")
    xVal=30
    yVal=300
    button31.place(x = (xVal * 3) - 20, y=yVal)
    


def march(event):
    global month
    showButton.place(x=450, y=420)
    month=3

    calLabel = Label(root, text=str((calendar.month(2020, month))), bg="grey", fg="white")
    calLabel["font"] = myFont
    calLabel.place(x=550, y=117)

    #shows buttons with dates
    global userdate
    xVal=30
    yVal=200
    
    button1 = Button(root, text="1")
    button1.bind("<Button-1>", findEvent1)
    xVal=30
    yVal=200
    button1.place(x = (xVal*1)-20, y=yVal)
    
    button2 = Button(root, text="2")
    button2.bind("<Button-1>", findEvent2)
    xVal=30
    yVal=200
    button2.place(x = (xVal*2)-20, y=yVal)
    
    button3 = Button(root, text="3")
    button3.bind("<Button-1>", findEvent3)
    xVal=30
    yVal=200
    button3.place(x = (xVal*3)-20, y=yVal)

    button4 = Button(root, text="4")
    button4.bind("<Button-1>", findEvent4)
    xVal=30
    yVal=200
    button4.place(x = (xVal*4)-20, y=yVal)

    button5 = Button(root, text="5")
    button5.bind("<Button-1>", findEvent5)
    xVal=30
    yVal=200
    button5.place(x = (xVal*5)-20, y=yVal)

    button6 = Button(root, text="6")
    button6.bind("<Button-1>", findEvent6)
    xVal=30
    yVal=200
    button6.place(x = (xVal * 6) - 20, y=yVal)

    button7 = Button(root, text="7")
    button7.bind("<Button-1>", findEvent7)
    xVal=30
    yVal=200
    button7.place(x = (xVal * 7) - 20, y=yVal)

    button8 = Button(root, text="8")
    button8.bind("<Button-1>", findEvent8)
    xVal=30
    yVal=200
    button8.place(x = (xVal * 8) - 20, y=yVal)

    button9 = Button(root, text="9")
    button9.bind("<Button-1>", findEvent9)
    button9.place(x = (xVal * 9) - 20, y=yVal)

    button10 = Button(root, text="10")
    button10.bind("<Button-1>", findEvent10)
    xVal=30
    yVal=200
    button10.place(x = (xVal * 10) - 20, y=yVal)

    button11 = Button(root, text="11")
    button11.bind("<Button-1>", findEvent11)
    xVal=30
    yVal=200
    button11.place(x = (xVal * 11) - 20, y=yVal)

    button12 = Button(root, text="12")
    button12.bind("<Button-1>", findEvent12)
    xVal=30
    yVal=200
    button12.place(x = (xVal * 12) - 20, y=yVal)

    button13 = Button(root, text="13")
    button13.bind("<Button-1>", findEvent13)
    xVal=30
    yVal=200
    button13.place(x = (xVal * 13) - 20, y=yVal)

    button14 = Button(root, text="14")
    button14.bind("<Button-1>", findEvent14)
    xVal=30
    yVal=200
    button14.place(x = (xVal * 14) - 20, y=yVal)

    button15 = Button(root, text="15")
    button15.bind("<Button-1>", findEvent15)
    xVal=30
    yVal=250
    button15.place(x = (xVal * 1) - 20, y=yVal)


    button16 = Button(root, text="16")
    button16.bind("<Button-1>", findEvent16)
    xVal=30
    yVal=250
    button16.place(x = (xVal * 2) - 20, y=yVal)

    button17 = Button(root, text="17")
    button17.bind("<Button-1>", findEvent17)
    xVal=30
    yVal=250
    button17.place(x = (xVal * 3) - 20, y=yVal)

    button18 = Button(root, text="18")
    button18.bind("<Button-1>", findEvent18)
    xVal=30
    yVal=250
    button18.place(x = (xVal * 4) - 20, y=yVal)

    button19 = Button(root, text="19")
    button19.bind("<Button-1>", findEvent19)
    xVal=30
    yVal=250
    button19.place(x = (xVal * 5) - 20, y=yVal)


    button20 = Button(root, text="20")
    button20.bind("<Button-1>", findEvent20)
    xVal=30
    yVal=250
    button20.place(x = (xVal * 6) - 20, y=yVal)

    button21 = Button(root, text="21")
    button21.bind("<Button-1>", findEvent21)
    xVal=30
    yVal=250
    button21.place(x = (xVal * 7) - 20, y=yVal)


    button22 = Button(root, text="22")
    button22.bind("<Button-1>", findEvent22)
    xVal=30
    yVal=250
    button22.place(x = (xVal * 8) - 20, y=yVal)

    button23 = Button(root, text="23")
    button23.bind("<Button-1>", findEvent23)
    xVal=30
    yVal=250
    button23.place(x = (xVal * 9) - 20, y=yVal)

    button24 = Button(root, text="24")
    button24.bind("<Button-1>", findEvent24)
    xVal=30
    yVal=250
    button24.place(x = (xVal * 10) - 20, y=yVal)

    button25 = Button(root, text="25")
    button25.bind("<Button-1>", findEvent25)
    xVal=30
    yVal=250
    button25.place(x = (xVal * 11) - 20, y=yVal)

    button26 = Button(root, text="26")
    button26.bind("<Button-1>", findEvent26)
    xVal=30
    yVal=250
    button26.place(x = (xVal * 12) - 20, y=yVal)

    button27 = Button(root, text="27")
    button27.bind("<Button-1>", findEvent27)
    xVal=30
    yVal=250
    button27.place(x = (xVal * 13) - 20, y=yVal)

    button28 = Button(root, text="28")
    button28.bind("<Button-1>", findEvent28)
    xVal=30
    yVal=250
    button28.place(x = (xVal * 14) - 20, y=yVal)

    button29 = Button(root, text="29")
    button29.bind("<Button-1>", findEvent29)
    xVal=30
    yVal=300
    button29.place(x = (xVal * 1) - 20, y=yVal)

    button30 = Button(root, text="30")
    button30.bind("<Button-1>", findEvent30)
    xVal=30
    yVal=300
    button30.place(x = (xVal * 2) - 20, y=yVal)

    button31 = Button(root, text="31")
    button31.bind("<Button-1>", findEvent31)
    xVal=30
    yVal=300
    button31.place(x = (xVal * 3) - 20, y=yVal)



def april(event):
    global month
    showButton.place(x=450, y=420)
    month=4

    calLabel = Label(root, text=str((calendar.month(2020, month))), bg="grey", fg="white")
    calLabel["font"] = myFont
    calLabel.place(x=550, y=117)


    global userdate
    xVal=30
    yVal=200
    
    button1 = Button(root, text="1")
    button1.bind("<Button-1>", findEvent1)
    xVal=30
    yVal=200
    button1.place(x = (xVal*1)-20, y=yVal)
    
    button2 = Button(root, text="2")
    button2.bind("<Button-1>", findEvent2)
    xVal=30
    yVal=200
    button2.place(x = (xVal*2)-20, y=yVal)
    
    button3 = Button(root, text="3")
    button3.bind("<Button-1>", findEvent3)
    xVal=30
    yVal=200
    button3.place(x = (xVal*3)-20, y=yVal)

    button4 = Button(root, text="4")
    button4.bind("<Button-1>", findEvent4)
    xVal=30
    yVal=200
    button4.place(x = (xVal*4)-20, y=yVal)

    button5 = Button(root, text="5")
    button5.bind("<Button-1>", findEvent5)
    xVal=30
    yVal=200
    button5.place(x = (xVal*5)-20, y=yVal)

    button6 = Button(root, text="6")
    button6.bind("<Button-1>", findEvent6)
    xVal=30
    yVal=200
    button6.place(x = (xVal * 6) - 20, y=yVal)

    button7 = Button(root, text="7")
    button7.bind("<Button-1>", findEvent7)
    xVal=30
    yVal=200
    button7.place(x = (xVal * 7) - 20, y=yVal)

    button8 = Button(root, text="8")
    button8.bind("<Button-1>", findEvent8)
    xVal=30
    yVal=200
    button8.place(x = (xVal * 8) - 20, y=yVal)

    button9 = Button(root, text="9")
    button9.bind("<Button-1>", findEvent9)
    button9.place(x = (xVal * 9) - 20, y=yVal)

    button10 = Button(root, text="10")
    button10.bind("<Button-1>", findEvent10)
    xVal=30
    yVal=200
    button10.place(x = (xVal * 10) - 20, y=yVal)

    button11 = Button(root, text="11")
    button11.bind("<Button-1>", findEvent11)
    xVal=30
    yVal=200
    button11.place(x = (xVal * 11) - 20, y=yVal)

    button12 = Button(root, text="12")
    button12.bind("<Button-1>", findEvent12)
    xVal=30
    yVal=200
    button12.place(x = (xVal * 12) - 20, y=yVal)

    button13 = Button(root, text="13")
    button13.bind("<Button-1>", findEvent13)
    xVal=30
    yVal=200
    button13.place(x = (xVal * 13) - 20, y=yVal)

    button14 = Button(root, text="14")
    button14.bind("<Button-1>", findEvent14)
    xVal=30
    yVal=200
    button14.place(x = (xVal * 14) - 20, y=yVal)

    button15 = Button(root, text="15")
    button15.bind("<Button-1>", findEvent15)
    xVal=30
    yVal=250
    button15.place(x = (xVal * 1) - 20, y=yVal)


    button16 = Button(root, text="16")
    button16.bind("<Button-1>", findEvent16)
    xVal=30
    yVal=250
    button16.place(x = (xVal * 2) - 20, y=yVal)

    button17 = Button(root, text="17")
    button17.bind("<Button-1>", findEvent17)
    xVal=30
    yVal=250
    button17.place(x = (xVal * 3) - 20, y=yVal)

    button18 = Button(root, text="18")
    button18.bind("<Button-1>", findEvent18)
    xVal=30
    yVal=250
    button18.place(x = (xVal * 4) - 20, y=yVal)

    button19 = Button(root, text="19")
    button19.bind("<Button-1>", findEvent19)
    xVal=30
    yVal=250
    button19.place(x = (xVal * 5) - 20, y=yVal)


    button20 = Button(root, text="20")
    button20.bind("<Button-1>", findEvent20)
    xVal=30
    yVal=250
    button20.place(x = (xVal * 6) - 20, y=yVal)

    button21 = Button(root, text="21")
    button21.bind("<Button-1>", findEvent21)
    xVal=30
    yVal=250
    button21.place(x = (xVal * 7) - 20, y=yVal)


    button22 = Button(root, text="22")
    button22.bind("<Button-1>", findEvent22)
    xVal=30
    yVal=250
    button22.place(x = (xVal * 8) - 20, y=yVal)

    button23 = Button(root, text="23")
    button23.bind("<Button-1>", findEvent23)
    xVal=30
    yVal=250
    button23.place(x = (xVal * 9) - 20, y=yVal)

    button24 = Button(root, text="24")
    button24.bind("<Button-1>", findEvent24)
    xVal=30
    yVal=250
    button24.place(x = (xVal * 10) - 20, y=yVal)

    button25 = Button(root, text="25")
    button25.bind("<Button-1>", findEvent25)
    xVal=30
    yVal=250
    button25.place(x = (xVal * 11) - 20, y=yVal)

    button26 = Button(root, text="26")
    button26.bind("<Button-1>", findEvent26)
    xVal=30
    yVal=250
    button26.place(x = (xVal * 12) - 20, y=yVal)

    button27 = Button(root, text="27")
    button27.bind("<Button-1>", findEvent27)
    xVal=30
    yVal=250
    button27.place(x = (xVal * 13) - 20, y=yVal)

    button28 = Button(root, text="28")
    button28.bind("<Button-1>", findEvent28)
    xVal=30
    yVal=250
    button28.place(x = (xVal * 14) - 20, y=yVal)

    button29 = Button(root, text="29")
    button29.bind("<Button-1>", findEvent29)
    xVal=30
    yVal=300
    button29.place(x = (xVal * 1) - 20, y=yVal)

    button30 = Button(root, text="30")
    button30.bind("<Button-1>", findEvent30)
    xVal=30
    yVal=300
    button30.place(x = (xVal * 2) - 20, y=yVal)

    button31 = Button(root, text="    ")
    button31.bind("<Button-1>")
    xVal=30
    yVal=300
    button31.place(x = (xVal * 3) - 20, y=yVal)



def may(event):
    global month
    showButton.place(x=450, y=420)
    month=5

    calLabel = Label(root, text=str((calendar.month(2020, month))), bg="grey", fg="white")
    calLabel["font"] = myFont
    calLabel.place(x=550, y=117)

    #shows buttons with dates
    global userdate
    xVal=30
    yVal=200
    
    button1 = Button(root, text="1")
    button1.bind("<Button-1>", findEvent1)
    xVal=30
    yVal=200
    button1.place(x = (xVal*1)-20, y=yVal)
    
    button2 = Button(root, text="2")
    button2.bind("<Button-1>", findEvent2)
    xVal=30
    yVal=200
    button2.place(x = (xVal*2)-20, y=yVal)
    
    button3 = Button(root, text="3")
    button3.bind("<Button-1>", findEvent3)
    xVal=30
    yVal=200
    button3.place(x = (xVal*3)-20, y=yVal)

    button4 = Button(root, text="4")
    button4.bind("<Button-1>", findEvent4)
    xVal=30
    yVal=200
    button4.place(x = (xVal*4)-20, y=yVal)

    button5 = Button(root, text="5")
    button5.bind("<Button-1>", findEvent5)
    xVal=30
    yVal=200
    button5.place(x = (xVal*5)-20, y=yVal)

    button6 = Button(root, text="6")
    button6.bind("<Button-1>", findEvent6)
    xVal=30
    yVal=200
    button6.place(x = (xVal * 6) - 20, y=yVal)

    button7 = Button(root, text="7")
    button7.bind("<Button-1>", findEvent7)
    xVal=30
    yVal=200
    button7.place(x = (xVal * 7) - 20, y=yVal)

    button8 = Button(root, text="8")
    button8.bind("<Button-1>", findEvent8)
    xVal=30
    yVal=200
    button8.place(x = (xVal * 8) - 20, y=yVal)

    button9 = Button(root, text="9")
    button9.bind("<Button-1>", findEvent9)
    button9.place(x = (xVal * 9) - 20, y=yVal)

    button10 = Button(root, text="10")
    button10.bind("<Button-1>", findEvent10)
    xVal=30
    yVal=200
    button10.place(x = (xVal * 10) - 20, y=yVal)

    button11 = Button(root, text="11")
    button11.bind("<Button-1>", findEvent11)
    xVal=30
    yVal=200
    button11.place(x = (xVal * 11) - 20, y=yVal)

    button12 = Button(root, text="12")
    button12.bind("<Button-1>", findEvent12)
    xVal=30
    yVal=200
    button12.place(x = (xVal * 12) - 20, y=yVal)

    button13 = Button(root, text="13")
    button13.bind("<Button-1>", findEvent13)
    xVal=30
    yVal=200
    button13.place(x = (xVal * 13) - 20, y=yVal)

    button14 = Button(root, text="14")
    button14.bind("<Button-1>", findEvent14)
    xVal=30
    yVal=200
    button14.place(x = (xVal * 14) - 20, y=yVal)

    button15 = Button(root, text="15")
    button15.bind("<Button-1>", findEvent15)
    xVal=30
    yVal=250
    button15.place(x = (xVal * 1) - 20, y=yVal)


    button16 = Button(root, text="16")
    button16.bind("<Button-1>", findEvent16)
    xVal=30
    yVal=250
    button16.place(x = (xVal * 2) - 20, y=yVal)

    button17 = Button(root, text="17")
    button17.bind("<Button-1>", findEvent17)
    xVal=30
    yVal=250
    button17.place(x = (xVal * 3) - 20, y=yVal)

    button18 = Button(root, text="18")
    button18.bind("<Button-1>", findEvent18)
    xVal=30
    yVal=250
    button18.place(x = (xVal * 4) - 20, y=yVal)

    button19 = Button(root, text="19")
    button19.bind("<Button-1>", findEvent19)
    xVal=30
    yVal=250
    button19.place(x = (xVal * 5) - 20, y=yVal)


    button20 = Button(root, text="20")
    button20.bind("<Button-1>", findEvent20)
    xVal=30
    yVal=250
    button20.place(x = (xVal * 6) - 20, y=yVal)

    button21 = Button(root, text="21")
    button21.bind("<Button-1>", findEvent21)
    xVal=30
    yVal=250
    button21.place(x = (xVal * 7) - 20, y=yVal)


    button22 = Button(root, text="22")
    button22.bind("<Button-1>", findEvent22)
    xVal=30
    yVal=250
    button22.place(x = (xVal * 8) - 20, y=yVal)

    button23 = Button(root, text="23")
    button23.bind("<Button-1>", findEvent23)
    xVal=30
    yVal=250
    button23.place(x = (xVal * 9) - 20, y=yVal)

    button24 = Button(root, text="24")
    button24.bind("<Button-1>", findEvent24)
    xVal=30
    yVal=250
    button24.place(x = (xVal * 10) - 20, y=yVal)

    button25 = Button(root, text="25")
    button25.bind("<Button-1>", findEvent25)
    xVal=30
    yVal=250
    button25.place(x = (xVal * 11) - 20, y=yVal)

    button26 = Button(root, text="26")
    button26.bind("<Button-1>", findEvent26)
    xVal=30
    yVal=250
    button26.place(x = (xVal * 12) - 20, y=yVal)

    button27 = Button(root, text="27")
    button27.bind("<Button-1>", findEvent27)
    xVal=30
    yVal=250
    button27.place(x = (xVal * 13) - 20, y=yVal)

    button28 = Button(root, text="28")
    button28.bind("<Button-1>", findEvent28)
    xVal=30
    yVal=250
    button28.place(x = (xVal * 14) - 20, y=yVal)

    button29 = Button(root, text="29")
    button29.bind("<Button-1>", findEvent29)
    xVal=30
    yVal=300
    button29.place(x = (xVal * 1) - 20, y=yVal)

    button30 = Button(root, text="30")
    button30.bind("<Button-1>", findEvent30)
    xVal=30
    yVal=300
    button30.place(x = (xVal * 2) - 20, y=yVal)

    button31 = Button(root, text="31")
    button31.bind("<Button-1>", findEvent31)
    xVal=30
    yVal=300
    button31.place(x = (xVal * 3) - 20, y=yVal)



def june(event):
    global month
    showButton.place(x=450, y=420)
    month=6

    calLabel = Label(root, text=str((calendar.month(2020, month))), bg="grey", fg="white")
    calLabel["font"] = myFont
    calLabel.place(x=550, y=117)

    global userdate
    xVal=30
    yVal=200
    
    button1 = Button(root, text="1")
    button1.bind("<Button-1>", findEvent1)
    xVal=30
    yVal=200
    button1.place(x = (xVal*1)-20, y=yVal)
    
    button2 = Button(root, text="2")
    button2.bind("<Button-1>", findEvent2)
    xVal=30
    yVal=200
    button2.place(x = (xVal*2)-20, y=yVal)
    
    button3 = Button(root, text="3")
    button3.bind("<Button-1>", findEvent3)
    xVal=30
    yVal=200
    button3.place(x = (xVal*3)-20, y=yVal)

    button4 = Button(root, text="4")
    button4.bind("<Button-1>", findEvent4)
    xVal=30
    yVal=200
    button4.place(x = (xVal*4)-20, y=yVal)

    button5 = Button(root, text="5")
    button5.bind("<Button-1>", findEvent5)
    xVal=30
    yVal=200
    button5.place(x = (xVal*5)-20, y=yVal)

    button6 = Button(root, text="6")
    button6.bind("<Button-1>", findEvent6)
    xVal=30
    yVal=200
    button6.place(x = (xVal * 6) - 20, y=yVal)

    button7 = Button(root, text="7")
    button7.bind("<Button-1>", findEvent7)
    xVal=30
    yVal=200
    button7.place(x = (xVal * 7) - 20, y=yVal)

    button8 = Button(root, text="8")
    button8.bind("<Button-1>", findEvent8)
    xVal=30
    yVal=200
    button8.place(x = (xVal * 8) - 20, y=yVal)

    button9 = Button(root, text="9")
    button9.bind("<Button-1>", findEvent9)
    button9.place(x = (xVal * 9) - 20, y=yVal)

    button10 = Button(root, text="10")
    button10.bind("<Button-1>", findEvent10)
    xVal=30
    yVal=200
    button10.place(x = (xVal * 10) - 20, y=yVal)

    button11 = Button(root, text="11")
    button11.bind("<Button-1>", findEvent11)
    xVal=30
    yVal=200
    button11.place(x = (xVal * 11) - 20, y=yVal)

    button12 = Button(root, text="12")
    button12.bind("<Button-1>", findEvent12)
    xVal=30
    yVal=200
    button12.place(x = (xVal * 12) - 20, y=yVal)

    button13 = Button(root, text="13")
    button13.bind("<Button-1>", findEvent13)
    xVal=30
    yVal=200
    button13.place(x = (xVal * 13) - 20, y=yVal)

    button14 = Button(root, text="14")
    button14.bind("<Button-1>", findEvent14)
    xVal=30
    yVal=200
    button14.place(x = (xVal * 14) - 20, y=yVal)

    button15 = Button(root, text="15")
    button15.bind("<Button-1>", findEvent15)
    xVal=30
    yVal=250
    button15.place(x = (xVal * 1) - 20, y=yVal)


    button16 = Button(root, text="16")
    button16.bind("<Button-1>", findEvent16)
    xVal=30
    yVal=250
    button16.place(x = (xVal * 2) - 20, y=yVal)

    button17 = Button(root, text="17")
    button17.bind("<Button-1>", findEvent17)
    xVal=30
    yVal=250
    button17.place(x = (xVal * 3) - 20, y=yVal)

    button18 = Button(root, text="18")
    button18.bind("<Button-1>", findEvent18)
    xVal=30
    yVal=250
    button18.place(x = (xVal * 4) - 20, y=yVal)

    button19 = Button(root, text="19")
    button19.bind("<Button-1>", findEvent19)
    xVal=30
    yVal=250
    button19.place(x = (xVal * 5) - 20, y=yVal)


    button20 = Button(root, text="20")
    button20.bind("<Button-1>", findEvent20)
    xVal=30
    yVal=250
    button20.place(x = (xVal * 6) - 20, y=yVal)

    button21 = Button(root, text="21")
    button21.bind("<Button-1>", findEvent21)
    xVal=30
    yVal=250
    button21.place(x = (xVal * 7) - 20, y=yVal)


    button22 = Button(root, text="22")
    button22.bind("<Button-1>", findEvent22)
    xVal=30
    yVal=250
    button22.place(x = (xVal * 8) - 20, y=yVal)

    button23 = Button(root, text="23")
    button23.bind("<Button-1>", findEvent23)
    xVal=30
    yVal=250
    button23.place(x = (xVal * 9) - 20, y=yVal)

    button24 = Button(root, text="24")
    button24.bind("<Button-1>", findEvent24)
    xVal=30
    yVal=250
    button24.place(x = (xVal * 10) - 20, y=yVal)

    button25 = Button(root, text="25")
    button25.bind("<Button-1>", findEvent25)
    xVal=30
    yVal=250
    button25.place(x = (xVal * 11) - 20, y=yVal)

    button26 = Button(root, text="26")
    button26.bind("<Button-1>", findEvent26)
    xVal=30
    yVal=250
    button26.place(x = (xVal * 12) - 20, y=yVal)

    button27 = Button(root, text="27")
    button27.bind("<Button-1>", findEvent27)
    xVal=30
    yVal=250
    button27.place(x = (xVal * 13) - 20, y=yVal)

    button28 = Button(root, text="28")
    button28.bind("<Button-1>", findEvent28)
    xVal=30
    yVal=250
    button28.place(x = (xVal * 14) - 20, y=yVal)

    button29 = Button(root, text="29")
    button29.bind("<Button-1>", findEvent29)
    xVal=30
    yVal=300
    button29.place(x = (xVal * 1) - 20, y=yVal)

    button30 = Button(root, text="30")
    button30.bind("<Button-1>", findEvent30)
    xVal=30
    yVal=300
    button30.place(x = (xVal * 2) - 20, y=yVal)

    button31 = Button(root, text="    ")
    button31.bind("<Button-1>")
    xVal=30
    yVal=300
    button31.place(x = (xVal * 3) - 20, y=yVal)



def july(event):
    global month
    showButton.place(x=450, y=420)
    month=7

    calLabel = Label(root, text=str((calendar.month(2020, month))), bg="grey", fg="white")
    calLabel["font"] = myFont
    calLabel.place(x=550, y=117)

    #shows buttons with dates
    global userdate
    xVal=30
    yVal=200
    
    button1 = Button(root, text="1")
    button1.bind("<Button-1>", findEvent1)
    xVal=30
    yVal=200
    button1.place(x = (xVal*1)-20, y=yVal)
    
    button2 = Button(root, text="2")
    button2.bind("<Button-1>", findEvent2)
    xVal=30
    yVal=200
    button2.place(x = (xVal*2)-20, y=yVal)
    
    button3 = Button(root, text="3")
    button3.bind("<Button-1>", findEvent3)
    xVal=30
    yVal=200
    button3.place(x = (xVal*3)-20, y=yVal)

    button4 = Button(root, text="4")
    button4.bind("<Button-1>", findEvent4)
    xVal=30
    yVal=200
    button4.place(x = (xVal*4)-20, y=yVal)

    button5 = Button(root, text="5")
    button5.bind("<Button-1>", findEvent5)
    xVal=30
    yVal=200
    button5.place(x = (xVal*5)-20, y=yVal)

    button6 = Button(root, text="6")
    button6.bind("<Button-1>", findEvent6)
    xVal=30
    yVal=200
    button6.place(x = (xVal * 6) - 20, y=yVal)

    button7 = Button(root, text="7")
    button7.bind("<Button-1>", findEvent7)
    xVal=30
    yVal=200
    button7.place(x = (xVal * 7) - 20, y=yVal)

    button8 = Button(root, text="8")
    button8.bind("<Button-1>", findEvent8)
    xVal=30
    yVal=200
    button8.place(x = (xVal * 8) - 20, y=yVal)

    button9 = Button(root, text="9")
    button9.bind("<Button-1>", findEvent9)
    button9.place(x = (xVal * 9) - 20, y=yVal)

    button10 = Button(root, text="10")
    button10.bind("<Button-1>", findEvent10)
    xVal=30
    yVal=200
    button10.place(x = (xVal * 10) - 20, y=yVal)

    button11 = Button(root, text="11")
    button11.bind("<Button-1>", findEvent11)
    xVal=30
    yVal=200
    button11.place(x = (xVal * 11) - 20, y=yVal)

    button12 = Button(root, text="12")
    button12.bind("<Button-1>", findEvent12)
    xVal=30
    yVal=200
    button12.place(x = (xVal * 12) - 20, y=yVal)

    button13 = Button(root, text="13")
    button13.bind("<Button-1>", findEvent13)
    xVal=30
    yVal=200
    button13.place(x = (xVal * 13) - 20, y=yVal)

    button14 = Button(root, text="14")
    button14.bind("<Button-1>", findEvent14)
    xVal=30
    yVal=200
    button14.place(x = (xVal * 14) - 20, y=yVal)

    button15 = Button(root, text="15")
    button15.bind("<Button-1>", findEvent15)
    xVal=30
    yVal=250
    button15.place(x = (xVal * 1) - 20, y=yVal)


    button16 = Button(root, text="16")
    button16.bind("<Button-1>", findEvent16)
    xVal=30
    yVal=250
    button16.place(x = (xVal * 2) - 20, y=yVal)

    button17 = Button(root, text="17")
    button17.bind("<Button-1>", findEvent17)
    xVal=30
    yVal=250
    button17.place(x = (xVal * 3) - 20, y=yVal)

    button18 = Button(root, text="18")
    button18.bind("<Button-1>", findEvent18)
    xVal=30
    yVal=250
    button18.place(x = (xVal * 4) - 20, y=yVal)

    button19 = Button(root, text="19")
    button19.bind("<Button-1>", findEvent19)
    xVal=30
    yVal=250
    button19.place(x = (xVal * 5) - 20, y=yVal)


    button20 = Button(root, text="20")
    button20.bind("<Button-1>", findEvent20)
    xVal=30
    yVal=250
    button20.place(x = (xVal * 6) - 20, y=yVal)

    button21 = Button(root, text="21")
    button21.bind("<Button-1>", findEvent21)
    xVal=30
    yVal=250
    button21.place(x = (xVal * 7) - 20, y=yVal)


    button22 = Button(root, text="22")
    button22.bind("<Button-1>", findEvent22)
    xVal=30
    yVal=250
    button22.place(x = (xVal * 8) - 20, y=yVal)

    button23 = Button(root, text="23")
    button23.bind("<Button-1>", findEvent23)
    xVal=30
    yVal=250
    button23.place(x = (xVal * 9) - 20, y=yVal)

    button24 = Button(root, text="24")
    button24.bind("<Button-1>", findEvent24)
    xVal=30
    yVal=250
    button24.place(x = (xVal * 10) - 20, y=yVal)

    button25 = Button(root, text="25")
    button25.bind("<Button-1>", findEvent25)
    xVal=30
    yVal=250
    button25.place(x = (xVal * 11) - 20, y=yVal)

    button26 = Button(root, text="26")
    button26.bind("<Button-1>", findEvent26)
    xVal=30
    yVal=250
    button26.place(x = (xVal * 12) - 20, y=yVal)

    button27 = Button(root, text="27")
    button27.bind("<Button-1>", findEvent27)
    xVal=30
    yVal=250
    button27.place(x = (xVal * 13) - 20, y=yVal)

    button28 = Button(root, text="28")
    button28.bind("<Button-1>", findEvent28)
    xVal=30
    yVal=250
    button28.place(x = (xVal * 14) - 20, y=yVal)

    button29 = Button(root, text="29")
    button29.bind("<Button-1>", findEvent29)
    xVal=30
    yVal=300
    button29.place(x = (xVal * 1) - 20, y=yVal)

    button30 = Button(root, text="30")
    button30.bind("<Button-1>", findEvent30)
    xVal=30
    yVal=300
    button30.place(x = (xVal * 2) - 20, y=yVal)

    button31 = Button(root, text="31")
    button31.bind("<Button-1>", findEvent31)
    xVal=30
    yVal=300
    button31.place(x = (xVal * 3) - 20, y=yVal)



def august(event):
    global month
    showButton.place(x=450, y=420)
    month=8

    calLabel = Label(root, text=str((calendar.month(2020, month))), bg="grey", fg="white")
    calLabel["font"] = myFont
    calLabel.place(x=550, y=117)

    #shows buttons with dates
    global userdate
    xVal=30
    yVal=200
    
    button1 = Button(root, text="1")
    button1.bind("<Button-1>", findEvent1)
    xVal=30
    yVal=200
    button1.place(x = (xVal*1)-20, y=yVal)
    
    button2 = Button(root, text="2")
    button2.bind("<Button-1>", findEvent2)
    xVal=30
    yVal=200
    button2.place(x = (xVal*2)-20, y=yVal)
    
    button3 = Button(root, text="3")
    button3.bind("<Button-1>", findEvent3)
    xVal=30
    yVal=200
    button3.place(x = (xVal*3)-20, y=yVal)

    button4 = Button(root, text="4")
    button4.bind("<Button-1>", findEvent4)
    xVal=30
    yVal=200
    button4.place(x = (xVal*4)-20, y=yVal)

    button5 = Button(root, text="5")
    button5.bind("<Button-1>", findEvent5)
    xVal=30
    yVal=200
    button5.place(x = (xVal*5)-20, y=yVal)

    button6 = Button(root, text="6")
    button6.bind("<Button-1>", findEvent6)
    xVal=30
    yVal=200
    button6.place(x = (xVal * 6) - 20, y=yVal)

    button7 = Button(root, text="7")
    button7.bind("<Button-1>", findEvent7)
    xVal=30
    yVal=200
    button7.place(x = (xVal * 7) - 20, y=yVal)

    button8 = Button(root, text="8")
    button8.bind("<Button-1>", findEvent8)
    xVal=30
    yVal=200
    button8.place(x = (xVal * 8) - 20, y=yVal)

    button9 = Button(root, text="9")
    button9.bind("<Button-1>", findEvent9)
    button9.place(x = (xVal * 9) - 20, y=yVal)

    button10 = Button(root, text="10")
    button10.bind("<Button-1>", findEvent10)
    xVal=30
    yVal=200
    button10.place(x = (xVal * 10) - 20, y=yVal)

    button11 = Button(root, text="11")
    button11.bind("<Button-1>", findEvent11)
    xVal=30
    yVal=200
    button11.place(x = (xVal * 11) - 20, y=yVal)

    button12 = Button(root, text="12")
    button12.bind("<Button-1>", findEvent12)
    xVal=30
    yVal=200
    button12.place(x = (xVal * 12) - 20, y=yVal)

    button13 = Button(root, text="13")
    button13.bind("<Button-1>", findEvent13)
    xVal=30
    yVal=200
    button13.place(x = (xVal * 13) - 20, y=yVal)

    button14 = Button(root, text="14")
    button14.bind("<Button-1>", findEvent14)
    xVal=30
    yVal=200
    button14.place(x = (xVal * 14) - 20, y=yVal)

    button15 = Button(root, text="15")
    button15.bind("<Button-1>", findEvent15)
    xVal=30
    yVal=250
    button15.place(x = (xVal * 1) - 20, y=yVal)


    button16 = Button(root, text="16")
    button16.bind("<Button-1>", findEvent16)
    xVal=30
    yVal=250
    button16.place(x = (xVal * 2) - 20, y=yVal)

    button17 = Button(root, text="17")
    button17.bind("<Button-1>", findEvent17)
    xVal=30
    yVal=250
    button17.place(x = (xVal * 3) - 20, y=yVal)

    button18 = Button(root, text="18")
    button18.bind("<Button-1>", findEvent18)
    xVal=30
    yVal=250
    button18.place(x = (xVal * 4) - 20, y=yVal)

    button19 = Button(root, text="19")
    button19.bind("<Button-1>", findEvent19)
    xVal=30
    yVal=250
    button19.place(x = (xVal * 5) - 20, y=yVal)


    button20 = Button(root, text="20")
    button20.bind("<Button-1>", findEvent20)
    xVal=30
    yVal=250
    button20.place(x = (xVal * 6) - 20, y=yVal)

    button21 = Button(root, text="21")
    button21.bind("<Button-1>", findEvent21)
    xVal=30
    yVal=250
    button21.place(x = (xVal * 7) - 20, y=yVal)


    button22 = Button(root, text="22")
    button22.bind("<Button-1>", findEvent22)
    xVal=30
    yVal=250
    button22.place(x = (xVal * 8) - 20, y=yVal)

    button23 = Button(root, text="23")
    button23.bind("<Button-1>", findEvent23)
    xVal=30
    yVal=250
    button23.place(x = (xVal * 9) - 20, y=yVal)

    button24 = Button(root, text="24")
    button24.bind("<Button-1>", findEvent24)
    xVal=30
    yVal=250
    button24.place(x = (xVal * 10) - 20, y=yVal)

    button25 = Button(root, text="25")
    button25.bind("<Button-1>", findEvent25)
    xVal=30
    yVal=250
    button25.place(x = (xVal * 11) - 20, y=yVal)

    button26 = Button(root, text="26")
    button26.bind("<Button-1>", findEvent26)
    xVal=30
    yVal=250
    button26.place(x = (xVal * 12) - 20, y=yVal)

    button27 = Button(root, text="27")
    button27.bind("<Button-1>", findEvent27)
    xVal=30
    yVal=250
    button27.place(x = (xVal * 13) - 20, y=yVal)

    button28 = Button(root, text="28")
    button28.bind("<Button-1>", findEvent28)
    xVal=30
    yVal=250
    button28.place(x = (xVal * 14) - 20, y=yVal)

    button29 = Button(root, text="29")
    button29.bind("<Button-1>", findEvent29)
    xVal=30
    yVal=300
    button29.place(x = (xVal * 1) - 20, y=yVal)

    button30 = Button(root, text="30")
    button30.bind("<Button-1>", findEvent30)
    xVal=30
    yVal=300
    button30.place(x = (xVal * 2) - 20, y=yVal)

    button31 = Button(root, text="31")
    button31.bind("<Button-1>", findEvent31)
    xVal=30
    yVal=300
    button31.place(x = (xVal * 3) - 20, y=yVal)



def september(event):
    global month
    showButton.place(x=450, y=420)
    month=9

    calLabel = Label(root, text=str((calendar.month(2020, month))), bg="grey", fg="white")
    calLabel["font"] = myFont
    calLabel.place(x=550, y=117)


    global userdate
    xVal=30
    yVal=200
    
    button1 = Button(root, text="1")
    button1.bind("<Button-1>", findEvent1)
    xVal=30
    yVal=200
    button1.place(x = (xVal*1)-20, y=yVal)
    
    button2 = Button(root, text="2")
    button2.bind("<Button-1>", findEvent2)
    xVal=30
    yVal=200
    button2.place(x = (xVal*2)-20, y=yVal)
    
    button3 = Button(root, text="3")
    button3.bind("<Button-1>", findEvent3)
    xVal=30
    yVal=200
    button3.place(x = (xVal*3)-20, y=yVal)

    button4 = Button(root, text="4")
    button4.bind("<Button-1>", findEvent4)
    xVal=30
    yVal=200
    button4.place(x = (xVal*4)-20, y=yVal)

    button5 = Button(root, text="5")
    button5.bind("<Button-1>", findEvent5)
    xVal=30
    yVal=200
    button5.place(x = (xVal*5)-20, y=yVal)

    button6 = Button(root, text="6")
    button6.bind("<Button-1>", findEvent6)
    xVal=30
    yVal=200
    button6.place(x = (xVal * 6) - 20, y=yVal)

    button7 = Button(root, text="7")
    button7.bind("<Button-1>", findEvent7)
    xVal=30
    yVal=200
    button7.place(x = (xVal * 7) - 20, y=yVal)

    button8 = Button(root, text="8")
    button8.bind("<Button-1>", findEvent8)
    xVal=30
    yVal=200
    button8.place(x = (xVal * 8) - 20, y=yVal)

    button9 = Button(root, text="9")
    button9.bind("<Button-1>", findEvent9)
    button9.place(x = (xVal * 9) - 20, y=yVal)

    button10 = Button(root, text="10")
    button10.bind("<Button-1>", findEvent10)
    xVal=30
    yVal=200
    button10.place(x = (xVal * 10) - 20, y=yVal)

    button11 = Button(root, text="11")
    button11.bind("<Button-1>", findEvent11)
    xVal=30
    yVal=200
    button11.place(x = (xVal * 11) - 20, y=yVal)

    button12 = Button(root, text="12")
    button12.bind("<Button-1>", findEvent12)
    xVal=30
    yVal=200
    button12.place(x = (xVal * 12) - 20, y=yVal)

    button13 = Button(root, text="13")
    button13.bind("<Button-1>", findEvent13)
    xVal=30
    yVal=200
    button13.place(x = (xVal * 13) - 20, y=yVal)

    button14 = Button(root, text="14")
    button14.bind("<Button-1>", findEvent14)
    xVal=30
    yVal=200
    button14.place(x = (xVal * 14) - 20, y=yVal)

    button15 = Button(root, text="15")
    button15.bind("<Button-1>", findEvent15)
    xVal=30
    yVal=250
    button15.place(x = (xVal * 1) - 20, y=yVal)


    button16 = Button(root, text="16")
    button16.bind("<Button-1>", findEvent16)
    xVal=30
    yVal=250
    button16.place(x = (xVal * 2) - 20, y=yVal)

    button17 = Button(root, text="17")
    button17.bind("<Button-1>", findEvent17)
    xVal=30
    yVal=250
    button17.place(x = (xVal * 3) - 20, y=yVal)

    button18 = Button(root, text="18")
    button18.bind("<Button-1>", findEvent18)
    xVal=30
    yVal=250
    button18.place(x = (xVal * 4) - 20, y=yVal)

    button19 = Button(root, text="19")
    button19.bind("<Button-1>", findEvent19)
    xVal=30
    yVal=250
    button19.place(x = (xVal * 5) - 20, y=yVal)


    button20 = Button(root, text="20")
    button20.bind("<Button-1>", findEvent20)
    xVal=30
    yVal=250
    button20.place(x = (xVal * 6) - 20, y=yVal)

    button21 = Button(root, text="21")
    button21.bind("<Button-1>", findEvent21)
    xVal=30
    yVal=250
    button21.place(x = (xVal * 7) - 20, y=yVal)


    button22 = Button(root, text="22")
    button22.bind("<Button-1>", findEvent22)
    xVal=30
    yVal=250
    button22.place(x = (xVal * 8) - 20, y=yVal)

    button23 = Button(root, text="23")
    button23.bind("<Button-1>", findEvent23)
    xVal=30
    yVal=250
    button23.place(x = (xVal * 9) - 20, y=yVal)

    button24 = Button(root, text="24")
    button24.bind("<Button-1>", findEvent24)
    xVal=30
    yVal=250
    button24.place(x = (xVal * 10) - 20, y=yVal)

    button25 = Button(root, text="25")
    button25.bind("<Button-1>", findEvent25)
    xVal=30
    yVal=250
    button25.place(x = (xVal * 11) - 20, y=yVal)

    button26 = Button(root, text="26")
    button26.bind("<Button-1>", findEvent26)
    xVal=30
    yVal=250
    button26.place(x = (xVal * 12) - 20, y=yVal)

    button27 = Button(root, text="27")
    button27.bind("<Button-1>", findEvent27)
    xVal=30
    yVal=250
    button27.place(x = (xVal * 13) - 20, y=yVal)

    button28 = Button(root, text="28")
    button28.bind("<Button-1>", findEvent28)
    xVal=30
    yVal=250
    button28.place(x = (xVal * 14) - 20, y=yVal)

    button29 = Button(root, text="29")
    button29.bind("<Button-1>", findEvent29)
    xVal=30
    yVal=300
    button29.place(x = (xVal * 1) - 20, y=yVal)

    button30 = Button(root, text="30")
    button30.bind("<Button-1>", findEvent30)
    xVal=30
    yVal=300
    button30.place(x = (xVal * 2) - 20, y=yVal)

    button31 = Button(root, text="    ")
    button31.bind("<Button-1>")
    xVal=30
    yVal=300
    button31.place(x = (xVal * 3) - 20, y=yVal)



def october(event):
    global month
    showButton.place(x=450, y=420)
    month=10

    calLabel = Label(root, text=str((calendar.month(2020, month))), bg="grey", fg="white")
    calLabel["font"] = myFont
    calLabel.place(x=550, y=117)

    #shows buttons with dates
    global userdate
    xVal=30
    yVal=200
    
    button1 = Button(root, text="1")
    button1.bind("<Button-1>", findEvent1)
    xVal=30
    yVal=200
    button1.place(x = (xVal*1)-20, y=yVal)
    
    button2 = Button(root, text="2")
    button2.bind("<Button-1>", findEvent2)
    xVal=30
    yVal=200
    button2.place(x = (xVal*2)-20, y=yVal)
    
    button3 = Button(root, text="3")
    button3.bind("<Button-1>", findEvent3)
    xVal=30
    yVal=200
    button3.place(x = (xVal*3)-20, y=yVal)

    button4 = Button(root, text="4")
    button4.bind("<Button-1>", findEvent4)
    xVal=30
    yVal=200
    button4.place(x = (xVal*4)-20, y=yVal)

    button5 = Button(root, text="5")
    button5.bind("<Button-1>", findEvent5)
    xVal=30
    yVal=200
    button5.place(x = (xVal*5)-20, y=yVal)

    button6 = Button(root, text="6")
    button6.bind("<Button-1>", findEvent6)
    xVal=30
    yVal=200
    button6.place(x = (xVal * 6) - 20, y=yVal)

    button7 = Button(root, text="7")
    button7.bind("<Button-1>", findEvent7)
    xVal=30
    yVal=200
    button7.place(x = (xVal * 7) - 20, y=yVal)

    button8 = Button(root, text="8")
    button8.bind("<Button-1>", findEvent8)
    xVal=30
    yVal=200
    button8.place(x = (xVal * 8) - 20, y=yVal)

    button9 = Button(root, text="9")
    button9.bind("<Button-1>", findEvent9)
    button9.place(x = (xVal * 9) - 20, y=yVal)

    button10 = Button(root, text="10")
    button10.bind("<Button-1>", findEvent10)
    xVal=30
    yVal=200
    button10.place(x = (xVal * 10) - 20, y=yVal)

    button11 = Button(root, text="11")
    button11.bind("<Button-1>", findEvent11)
    xVal=30
    yVal=200
    button11.place(x = (xVal * 11) - 20, y=yVal)

    button12 = Button(root, text="12")
    button12.bind("<Button-1>", findEvent12)
    xVal=30
    yVal=200
    button12.place(x = (xVal * 12) - 20, y=yVal)

    button13 = Button(root, text="13")
    button13.bind("<Button-1>", findEvent13)
    xVal=30
    yVal=200
    button13.place(x = (xVal * 13) - 20, y=yVal)

    button14 = Button(root, text="14")
    button14.bind("<Button-1>", findEvent14)
    xVal=30
    yVal=200
    button14.place(x = (xVal * 14) - 20, y=yVal)

    button15 = Button(root, text="15")
    button15.bind("<Button-1>", findEvent15)
    xVal=30
    yVal=250
    button15.place(x = (xVal * 1) - 20, y=yVal)


    button16 = Button(root, text="16")
    button16.bind("<Button-1>", findEvent16)
    xVal=30
    yVal=250
    button16.place(x = (xVal * 2) - 20, y=yVal)

    button17 = Button(root, text="17")
    button17.bind("<Button-1>", findEvent17)
    xVal=30
    yVal=250
    button17.place(x = (xVal * 3) - 20, y=yVal)

    button18 = Button(root, text="18")
    button18.bind("<Button-1>", findEvent18)
    xVal=30
    yVal=250
    button18.place(x = (xVal * 4) - 20, y=yVal)

    button19 = Button(root, text="19")
    button19.bind("<Button-1>", findEvent19)
    xVal=30
    yVal=250
    button19.place(x = (xVal * 5) - 20, y=yVal)


    button20 = Button(root, text="20")
    button20.bind("<Button-1>", findEvent20)
    xVal=30
    yVal=250
    button20.place(x = (xVal * 6) - 20, y=yVal)

    button21 = Button(root, text="21")
    button21.bind("<Button-1>", findEvent21)
    xVal=30
    yVal=250
    button21.place(x = (xVal * 7) - 20, y=yVal)


    button22 = Button(root, text="22")
    button22.bind("<Button-1>", findEvent22)
    xVal=30
    yVal=250
    button22.place(x = (xVal * 8) - 20, y=yVal)

    button23 = Button(root, text="23")
    button23.bind("<Button-1>", findEvent23)
    xVal=30
    yVal=250
    button23.place(x = (xVal * 9) - 20, y=yVal)

    button24 = Button(root, text="24")
    button24.bind("<Button-1>", findEvent24)
    xVal=30
    yVal=250
    button24.place(x = (xVal * 10) - 20, y=yVal)

    button25 = Button(root, text="25")
    button25.bind("<Button-1>", findEvent25)
    xVal=30
    yVal=250
    button25.place(x = (xVal * 11) - 20, y=yVal)

    button26 = Button(root, text="26")
    button26.bind("<Button-1>", findEvent26)
    xVal=30
    yVal=250
    button26.place(x = (xVal * 12) - 20, y=yVal)

    button27 = Button(root, text="27")
    button27.bind("<Button-1>", findEvent27)
    xVal=30
    yVal=250
    button27.place(x = (xVal * 13) - 20, y=yVal)

    button28 = Button(root, text="28")
    button28.bind("<Button-1>", findEvent28)
    xVal=30
    yVal=250
    button28.place(x = (xVal * 14) - 20, y=yVal)

    button29 = Button(root, text="29")
    button29.bind("<Button-1>", findEvent29)
    xVal=30
    yVal=300
    button29.place(x = (xVal * 1) - 20, y=yVal)

    button30 = Button(root, text="30")
    button30.bind("<Button-1>", findEvent30)
    xVal=30
    yVal=300
    button30.place(x = (xVal * 2) - 20, y=yVal)

    button31 = Button(root, text="31")
    button31.bind("<Button-1>", findEvent31)
    xVal=30
    yVal=300
    button31.place(x = (xVal * 3) - 20, y=yVal)



def november(event):
    global month
    showButton.place(x=450, y=420)
    month=11

    calLabel = Label(root, text=str((calendar.month(2020, month))), bg="grey", fg="white")
    calLabel["font"] = myFont
    calLabel.place(x=550, y=117)


    global userdate
    xVal=30
    yVal=200
    
    button1 = Button(root, text="1")
    button1.bind("<Button-1>", findEvent1)
    xVal=30
    yVal=200
    button1.place(x = (xVal*1)-20, y=yVal)
    
    button2 = Button(root, text="2")
    button2.bind("<Button-1>", findEvent2)
    xVal=30
    yVal=200
    button2.place(x = (xVal*2)-20, y=yVal)
    
    button3 = Button(root, text="3")
    button3.bind("<Button-1>", findEvent3)
    xVal=30
    yVal=200
    button3.place(x = (xVal*3)-20, y=yVal)

    button4 = Button(root, text="4")
    button4.bind("<Button-1>", findEvent4)
    xVal=30
    yVal=200
    button4.place(x = (xVal*4)-20, y=yVal)

    button5 = Button(root, text="5")
    button5.bind("<Button-1>", findEvent5)
    xVal=30
    yVal=200
    button5.place(x = (xVal*5)-20, y=yVal)

    button6 = Button(root, text="6")
    button6.bind("<Button-1>", findEvent6)
    xVal=30
    yVal=200
    button6.place(x = (xVal * 6) - 20, y=yVal)

    button7 = Button(root, text="7")
    button7.bind("<Button-1>", findEvent7)
    xVal=30
    yVal=200
    button7.place(x = (xVal * 7) - 20, y=yVal)

    button8 = Button(root, text="8")
    button8.bind("<Button-1>", findEvent8)
    xVal=30
    yVal=200
    button8.place(x = (xVal * 8) - 20, y=yVal)

    button9 = Button(root, text="9")
    button9.bind("<Button-1>", findEvent9)
    button9.place(x = (xVal * 9) - 20, y=yVal)

    button10 = Button(root, text="10")
    button10.bind("<Button-1>", findEvent10)
    xVal=30
    yVal=200
    button10.place(x = (xVal * 10) - 20, y=yVal)

    button11 = Button(root, text="11")
    button11.bind("<Button-1>", findEvent11)
    xVal=30
    yVal=200
    button11.place(x = (xVal * 11) - 20, y=yVal)

    button12 = Button(root, text="12")
    button12.bind("<Button-1>", findEvent12)
    xVal=30
    yVal=200
    button12.place(x = (xVal * 12) - 20, y=yVal)

    button13 = Button(root, text="13")
    button13.bind("<Button-1>", findEvent13)
    xVal=30
    yVal=200
    button13.place(x = (xVal * 13) - 20, y=yVal)

    button14 = Button(root, text="14")
    button14.bind("<Button-1>", findEvent14)
    xVal=30
    yVal=200
    button14.place(x = (xVal * 14) - 20, y=yVal)

    button15 = Button(root, text="15")
    button15.bind("<Button-1>", findEvent15)
    xVal=30
    yVal=250
    button15.place(x = (xVal * 1) - 20, y=yVal)


    button16 = Button(root, text="16")
    button16.bind("<Button-1>", findEvent16)
    xVal=30
    yVal=250
    button16.place(x = (xVal * 2) - 20, y=yVal)

    button17 = Button(root, text="17")
    button17.bind("<Button-1>", findEvent17)
    xVal=30
    yVal=250
    button17.place(x = (xVal * 3) - 20, y=yVal)

    button18 = Button(root, text="18")
    button18.bind("<Button-1>", findEvent18)
    xVal=30
    yVal=250
    button18.place(x = (xVal * 4) - 20, y=yVal)

    button19 = Button(root, text="19")
    button19.bind("<Button-1>", findEvent19)
    xVal=30
    yVal=250
    button19.place(x = (xVal * 5) - 20, y=yVal)


    button20 = Button(root, text="20")
    button20.bind("<Button-1>", findEvent20)
    xVal=30
    yVal=250
    button20.place(x = (xVal * 6) - 20, y=yVal)

    button21 = Button(root, text="21")
    button21.bind("<Button-1>", findEvent21)
    xVal=30
    yVal=250
    button21.place(x = (xVal * 7) - 20, y=yVal)


    button22 = Button(root, text="22")
    button22.bind("<Button-1>", findEvent22)
    xVal=30
    yVal=250
    button22.place(x = (xVal * 8) - 20, y=yVal)

    button23 = Button(root, text="23")
    button23.bind("<Button-1>", findEvent23)
    xVal=30
    yVal=250
    button23.place(x = (xVal * 9) - 20, y=yVal)

    button24 = Button(root, text="24")
    button24.bind("<Button-1>", findEvent24)
    xVal=30
    yVal=250
    button24.place(x = (xVal * 10) - 20, y=yVal)

    button25 = Button(root, text="25")
    button25.bind("<Button-1>", findEvent25)
    xVal=30
    yVal=250
    button25.place(x = (xVal * 11) - 20, y=yVal)

    button26 = Button(root, text="26")
    button26.bind("<Button-1>", findEvent26)
    xVal=30
    yVal=250
    button26.place(x = (xVal * 12) - 20, y=yVal)

    button27 = Button(root, text="27")
    button27.bind("<Button-1>", findEvent27)
    xVal=30
    yVal=250
    button27.place(x = (xVal * 13) - 20, y=yVal)

    button28 = Button(root, text="28")
    button28.bind("<Button-1>", findEvent28)
    xVal=30
    yVal=250
    button28.place(x = (xVal * 14) - 20, y=yVal)

    button29 = Button(root, text="29")
    button29.bind("<Button-1>", findEvent29)
    xVal=30
    yVal=300
    button29.place(x = (xVal * 1) - 20, y=yVal)

    button30 = Button(root, text="30")
    button30.bind("<Button-1>", findEvent30)
    xVal=30
    yVal=300
    button30.place(x = (xVal * 2) - 20, y=yVal)

    button31 = Button(root, text="    ")
    button31.bind("<Button-1>")
    xVal=30
    yVal=300
    button31.place(x = (xVal * 3) - 20, y=yVal)



def december(event):
    global month
    showButton.place(x=450, y=420)
    month=12

    calLabel = Label(root, text=str((calendar.month(2020, month))), bg="grey", fg="white")
    calLabel["font"] = myFont
    calLabel.place(x=550, y=117)

    #shows buttons with dates
    global userdate
    xVal=30
    yVal=200
    
    button1 = Button(root, text="1")
    button1.bind("<Button-1>", findEvent1)
    xVal=30
    yVal=200
    button1.place(x = (xVal*1)-20, y=yVal)
    
    button2 = Button(root, text="2")
    button2.bind("<Button-1>", findEvent2)
    xVal=30
    yVal=200
    button2.place(x = (xVal*2)-20, y=yVal)
    
    button3 = Button(root, text="3")
    button3.bind("<Button-1>", findEvent3)
    xVal=30
    yVal=200
    button3.place(x = (xVal*3)-20, y=yVal)

    button4 = Button(root, text="4")
    button4.bind("<Button-1>", findEvent4)
    xVal=30
    yVal=200
    button4.place(x = (xVal*4)-20, y=yVal)

    button5 = Button(root, text="5")
    button5.bind("<Button-1>", findEvent5)
    xVal=30
    yVal=200
    button5.place(x = (xVal*5)-20, y=yVal)

    button6 = Button(root, text="6")
    button6.bind("<Button-1>", findEvent6)
    xVal=30
    yVal=200
    button6.place(x = (xVal * 6) - 20, y=yVal)

    button7 = Button(root, text="7")
    button7.bind("<Button-1>", findEvent7)
    xVal=30
    yVal=200
    button7.place(x = (xVal * 7) - 20, y=yVal)

    button8 = Button(root, text="8")
    button8.bind("<Button-1>", findEvent8)
    xVal=30
    yVal=200
    button8.place(x = (xVal * 8) - 20, y=yVal)

    button9 = Button(root, text="9")
    button9.bind("<Button-1>", findEvent9)
    button9.place(x = (xVal * 9) - 20, y=yVal)

    button10 = Button(root, text="10")
    button10.bind("<Button-1>", findEvent10)
    xVal=30
    yVal=200
    button10.place(x = (xVal * 10) - 20, y=yVal)

    button11 = Button(root, text="11")
    button11.bind("<Button-1>", findEvent11)
    xVal=30
    yVal=200
    button11.place(x = (xVal * 11) - 20, y=yVal)

    button12 = Button(root, text="12")
    button12.bind("<Button-1>", findEvent12)
    xVal=30
    yVal=200
    button12.place(x = (xVal * 12) - 20, y=yVal)

    button13 = Button(root, text="13")
    button13.bind("<Button-1>", findEvent13)
    xVal=30
    yVal=200
    button13.place(x = (xVal * 13) - 20, y=yVal)

    button14 = Button(root, text="14")
    button14.bind("<Button-1>", findEvent14)
    xVal=30
    yVal=200
    button14.place(x = (xVal * 14) - 20, y=yVal)

    button15 = Button(root, text="15")
    button15.bind("<Button-1>", findEvent15)
    xVal=30
    yVal=250
    button15.place(x = (xVal * 1) - 20, y=yVal)


    button16 = Button(root, text="16")
    button16.bind("<Button-1>", findEvent16)
    xVal=30
    yVal=250
    button16.place(x = (xVal * 2) - 20, y=yVal)

    button17 = Button(root, text="17")
    button17.bind("<Button-1>", findEvent17)
    xVal=30
    yVal=250
    button17.place(x = (xVal * 3) - 20, y=yVal)

    button18 = Button(root, text="18")
    button18.bind("<Button-1>", findEvent18)
    xVal=30
    yVal=250
    button18.place(x = (xVal * 4) - 20, y=yVal)

    button19 = Button(root, text="19")
    button19.bind("<Button-1>", findEvent19)
    xVal=30
    yVal=250
    button19.place(x = (xVal * 5) - 20, y=yVal)


    button20 = Button(root, text="20")
    button20.bind("<Button-1>", findEvent20)
    xVal=30
    yVal=250
    button20.place(x = (xVal * 6) - 20, y=yVal)

    button21 = Button(root, text="21")
    button21.bind("<Button-1>", findEvent21)
    xVal=30
    yVal=250
    button21.place(x = (xVal * 7) - 20, y=yVal)


    button22 = Button(root, text="22")
    button22.bind("<Button-1>", findEvent22)
    xVal=30
    yVal=250
    button22.place(x = (xVal * 8) - 20, y=yVal)

    button23 = Button(root, text="23")
    button23.bind("<Button-1>", findEvent23)
    xVal=30
    yVal=250
    button23.place(x = (xVal * 9) - 20, y=yVal)

    button24 = Button(root, text="24")
    button24.bind("<Button-1>", findEvent24)
    xVal=30
    yVal=250
    button24.place(x = (xVal * 10) - 20, y=yVal)

    button25 = Button(root, text="25")
    button25.bind("<Button-1>", findEvent25)
    xVal=30
    yVal=250
    button25.place(x = (xVal * 11) - 20, y=yVal)

    button26 = Button(root, text="26")
    button26.bind("<Button-1>", findEvent26)
    xVal=30
    yVal=250
    button26.place(x = (xVal * 12) - 20, y=yVal)

    button27 = Button(root, text="27")
    button27.bind("<Button-1>", findEvent27)
    xVal=30
    yVal=250
    button27.place(x = (xVal * 13) - 20, y=yVal)

    button28 = Button(root, text="28")
    button28.bind("<Button-1>", findEvent28)
    xVal=30
    yVal=250
    button28.place(x = (xVal * 14) - 20, y=yVal)

    button29 = Button(root, text="29")
    button29.bind("<Button-1>", findEvent29)
    xVal=30
    yVal=300
    button29.place(x = (xVal * 1) - 20, y=yVal)

    button30 = Button(root, text="30")
    button30.bind("<Button-1>", findEvent30)
    xVal=30
    yVal=300
    button30.place(x = (xVal * 2) - 20, y=yVal)

    button31 = Button(root, text="31")
    button31.bind("<Button-1>", findEvent31)
    xVal=30
    yVal=300
    button31.place(x = (xVal * 3) - 20, y=yVal)






def findEvent1(event):
    dateline =" "
    global userdate
    userdate=1

def findEvent2(event):
    dateline =" "
    global userdate
    userdate=2


def findEvent3(event):
    dateline =" "
    global userdate
    userdate=3


def findEvent4(event):
    global userdate
    userdate=4
    

def findEvent5(event):
    global userdate
    userdate=5


def findEvent6(event):
    global userdate
    userdate=6


def findEvent7(event):
    global userdate
    userdate=7


def findEvent8(event):
    global userdate
    userdate=8


def findEvent9(event):
    global userdate
    userdate=9


def findEvent10(event):
    global userdate
    userdate=10


def findEvent11(event):
    global userdate
    userdate=11


def findEvent12(event):
    global userdate
    userdate=12


def findEvent13(event):
    global userdate
    userdate=13


def findEvent14(event):
    global userdate
    userdate=14


def findEvent15(event):
    global userdate
    userdate=15


def findEvent16(event):
    global userdate
    userdate=16


def findEvent17(event):
    global userdate
    userdate=17


def findEvent18(event):
    global userdate
    userdate=18


def findEvent19(event):
    global userdate
    userdate=19


def findEvent20(event):
    global userdate
    userdate=20


def findEvent21(event):
    global userdate
    userdate=21


def findEvent22(event):
    global userdate
    userdate=22


def findEvent23(event):
    global userdate


def findEvent24(event):
    global userdate
    userdate=23


def findEvent25(event):
    global userdate
    userdate=25


def findEvent26(event):
    global userdate


def findEvent27(event):
    global userdate
    userdate=27


def findEvent28(event):
    global userdate
    userdate=28


def findEvent29(event):
    global userdate
    userdate=29


def findEvent30(event):
    global userdate
    userdate=30


def findEvent31(event):
    global userdate
    userdate=31




canvascal = Canvas(root, width=400, height=250)
canvascal.configure(bg="grey")
canvascal.place(x=450, y=80)
box = canvascal.create_rectangle(2, 2, 401, 251)


#calendar title
myFont1 = font.Font(size=17)
titleLabel = Label(root, text="                                                   CALENDAR                                                 ", bg="blue", fg="white")
titleLabel["font"] = myFont1

#choose month title
choose_month_label = Label(root, text="                             Select a month                             ", bg=from_rgb((15, 70, 140)) , fg="white")

#date and time
datelabel = Label(root, text=date, bg=from_rgb((15, 70, 140)) , fg="white")
timelabel = Label(root, bg=from_rgb((15, 70, 140)) , fg="white")
showTime()

#month buttons
januaryButton = Button(root, text="  January  ")
januaryButton.bind("<Button-1>", january)

februaryButton = Button(root, text="  February ")
februaryButton.bind("<Button-1>", february)


marchButton = Button(root, text="   March   ")
marchButton.bind("<Button-1>", march)


aprilButton = Button(root, text="   April   ")
aprilButton.bind("<Button-1>", april)



mayButton = Button(root, text="     May     ")
mayButton.bind("<Button-1>", may)



juneButton = Button(root, text="     June    ")
juneButton.bind("<Button-1>", june)




julyButton = Button(root, text="      July     ")
julyButton.bind("<Button-1>", july)



augustButton = Button(root, text="  August   ")
augustButton.bind("<Button-1>", august)


septemberButton = Button(root, text="September")
septemberButton.bind("<Button-1>", september)



octoberButton = Button(root, text="October")
octoberButton.bind("<Button-1>", october)


novemberButton = Button(root, text="November")
novemberButton.bind("<Button-1>", november)


decemberButton = Button(root, text="December")
decemberButton.bind("<Button-1>", december)



titleLabel.place(x=450, y=40, width=400, height=30)
choose_month_label.grid(row=1, column=0, columnspan=10)


#shows buttons
januaryButton.grid(row=2, column=0, padx=3, pady=4)
februaryButton.grid(row=2, column=1, padx=3, pady=4)
marchButton.grid(row=2, column=2, padx=3, pady=4)
aprilButton.grid(row=2, column=3, padx=3, pady=4)
mayButton.grid(row=2, column=4, padx=3, pady=4)
juneButton.grid(row=2, column=5, padx=3, pady=4)
julyButton.grid(row=3, column=0, padx=3, pady=4)
augustButton.grid(row=3, column=1, padx=3, pady=4)
septemberButton.grid(row=3, column=2, padx=3, pady=4)
octoberButton.grid(row=3, column=3, padx=3, pady=4)
novemberButton.grid(row=3, column=4, padx=3, pady=4)
decemberButton.grid(row=3, column=5, padx=3, pady=4)



#show date and time
datelabel.place(x=1200, y=20)
timelabel.place(x=1200, y=40)


root.mainloop()


