__author__ = 'chrismelnyk'
import tkinter as tk
from subprocess import call

safety = 'safety_in_numbersgui.py'
balanced = 'balancedgui.py'
hurtme = 'hurt_megui.py'

def callpy1():
    call(['python', safety] )

def callpy2():
    call(['python', balanced])
def callpy3():
    call(['python', hurtme])

root = tk.Tk()
img = tk.Image("photo", file="p_icon.png")
root.tk.call('wm','iconphoto', root._w, img)
root.geometry('400x300')
root.title('Prisoner Intake Guard Calculator')
l1 = tk.Label(text="Prisoner Intake Guard Calculator", fg="black", bg="white")

b1 = tk.Button(root, text='Safety in Numbers', command=callpy1, height=6, width=57).grid(row=0, column=1)
b2 = tk.Button(root, text='Balanced', command=callpy2, height=6, width=57).grid(row=1, column=1)
b3 = tk.Button(root, text='HURT ME PLEANTY', command=callpy3, height=6, width=57).grid(row=2, column=1)


root.mainloop()