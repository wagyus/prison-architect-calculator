__author__ = 'chrismelnyk'
import tkinter as tk
from functools import partial
from subprocess import call

def call_result1(label_result1):
    prisoners_intake_low = int(low_box.get())

    low_safe_calc = prisoners_intake_low / 4
    low_safe_guards = int(round(low_safe_calc, 1))

    result1 = str(low_safe_guards)
    label_result1.config(text="Number of guards for low security prisoners is: %d" % low_safe_guards)
    return

def call_result2(label_result2):
    prisoners_intake_med = int(med_box.get())

    med_safe_calc = ((prisoners_intake_med / 3))
    med_safe_guards =int(round(med_safe_calc, 1))

    result2 = med_safe_guards
    label_result2.config(text="Number of guards for medium security prisoners is: %d" % med_safe_guards)
    return

def call_result3(label_result3):
    prisoners_intake_high = int(high_box.get())

    high_safe_calc = ((prisoners_intake_high / 2))
    high_safe_guards =int(round(high_safe_calc, 1))

    result3 = high_safe_guards
    label_result3.config(text="Number of guards for high security prisoners is: %d" % high_safe_guards)
    return

reset2 = 'safety_in_numbersgui.py'
def reset():
    call(['python', reset2] )

def create_window():
    window=tk.Toplevel(root)
    
img = tk.Image("photo", file="p_icon.png")
root.tk.call('wm','iconphoto', root._w, img)

root = tk.Tk()
root.geometry('800x200+100+200')
root.title('Safety in Numbers Calculator')

n1 = tk.StringVar()
n2 = tk.StringVar()

labelResult1 = tk.Label(root, text="")
labelResult1.grid(row=1, column=7)

labelResult2 = tk.Label(root, text="")
labelResult2.grid(row=2, column=7)

labelResult3 = tk.Label(root, text="")
labelResult3.grid(row=3, column=7)

low_box = tk.Entry(root)
low_box.insert(0, 'Enter Low #')
low_box.grid(row=1, column=5, sticky='NS')

med_box = tk.Entry(root)
med_box.insert(0, 'Enter Med #')
med_box.grid(row=2, column=5, sticky='NS')

high_box = tk.Entry(root)
high_box.insert(0, 'Enter High #')
high_box.grid(row=3, column=5, sticky='NS')

call_result1 = partial(call_result1, labelResult1)
call_result2 = partial(call_result2, labelResult2)
call_result3 = partial(call_result3, labelResult3)


b1 = tk.Button(root, text="Calculate Low Guards", command=call_result1).grid(row=1, column=4)
b2 = tk.Button(root, text="Calculate Medium Guards", command=call_result2).grid(row=2, column=4)
b3 = tk.Button(root, text="Calculate High Guards", command=call_result3).grid(row=3, column=4)
b3 = tk.Button(root, text="Reset", command=reset).grid(row=4, column=4)

root.mainloop()