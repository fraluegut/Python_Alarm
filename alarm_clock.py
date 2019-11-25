# https://github.com/fraluegut
# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Javier Luengo"
__copyright__ = "Copyright 2019"
__credits__ = ["Javier Luengo"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Javier Luengo"
__email__ = "franciscojavierluengo@outlook.com"
__status__ = "Development"

# Libraries
from tkinter import *
import time
from time import gmtime
import tkinter as tk
from playsound import playsound

# Create the main window
root = tk.Tk()
root.title("Python Alarm-Clock")

# Create the main container
frame = tk.Frame(root)

# Lay out the main container
frame.config(width=180,height=120)

# Allow middle cell of grid to grow when window is resized
frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

# GUI
l1 = tk.Label(root, text="Alarm (00:00:00)")
l1.grid(row=0, column=0, padx=(10, 100), pady=(5, 0))

ent1 = tk.Entry(root)
ent1.grid(row=1, column=0, pady=(5, 5))

Time = time.strftime("%H:%M:%S", gmtime())

# Activate Alarm
def save():
    print("The Alarm is: " + ent1.get())
    global Alarm
    global Time
    Alarm = ent1.get()

    while Time != Alarm:

        print("The time is: " + Time)
        Time = time.strftime("%H:%M:%S", gmtime())
        time.sleep(1)

    if Time == Alarm:

        print("Time to wake up!")
        message()

# Alarm message in new window and sound
def message():
    window = tk.Toplevel(root)

    message= Label(window, text="Alarm !!!", font=("Helvetica", 56))
    message.grid(row=1, column=0, pady=(5, 5))

    btnsd = Button(window, text="Cerrar", bg="green", fg="white", command=exit)
    btnsd.grid(row=10, columnspan=2)

    playsound('alarma_2.mp3')

#Button to activate alarm
balarm = tk.Button(root, text="Guardar", bg="green", fg="white", command=save)
balarm.grid(row=1, column=3)


# Cronometer
l1 = tk.Label(root, text="Cronometer ")
l1.grid(row=2, column=0, padx=(10, 100))

ent2 = tk.Entry(root)
ent2.grid(row=3, column=0, pady=(5, 10))

bcrono = tk.Button(root, text="Fijar", bg="green", fg="white")
bcrono.grid(row=3, column=3)

# Clock
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,tick)


clock = tk.Label(root)
clock.grid(row=0, column=6, padx=(10, 10))
tick()

root.mainloop()




