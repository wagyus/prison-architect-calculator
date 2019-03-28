__author__ = 'chrismelnyk'
import tkinter as tk
from subprocess import call

laundry = 'laundry_gui.py'
workshop = 'workshop_gui.py'
def callpy1():
    call(['python', laundry] )

def callpy2():
    call(['python', workshop])

root = tk.Tk()
b1 = tk.Button(root, text='Laundry Calculator', command=callpy1).grid(row=0, column=1)
b2 = tk.Button(root, text='Workshop Calculator', command=callpy2).grid(row=0, column=2)

root.mainloop()