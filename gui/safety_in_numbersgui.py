__author__ = 'chrismelnyk'
import tkinter as tk
from functools import partial
work_hours = 0

def call_result1(label_result, prisoners_low, result1):
    prisoners_intake_low = prisoners_low.get()

    low_safe_calc = prisoners_intake_low / 4
    low_safe_guards = round(low_safe_calc, 1)

    result1 = low_safe_guards
    label_result.config(text="# of baskets is %d" % result1)
    return

def call_result2(label_result, prisoners_med, result2):
    prisoners_intake_med = int((prisoners_med.get()))

    med_safe_calc = ((prisoners_intake_med/4))
    med_safe_guards = round(med_safe_calc, 1)

    result2 = med_safe_guards
    label_result.config(text=(result2))
    return
'''
def call_result3(label_result, prisoners_high, result3):
    prisoners_intake_high = int((prisoners_high.get()))

    high_safe_calc = ((prisoners_intake_high/4))
    high_safe_guards = round(high_safe_calc, 1)

    result3 = high_safe_guards
    label_result.config(text="# of baskets is %d" % high_safe_guards)
    return
'''
def create_window():
    window=tk.Toplevel(root)

root = tk.Tk()
root.geometry('800x200+100+200')
root.title('Safety in Numbers Calculator')

number1 = tk.IntVar()
number2 = tk.StringVar()
#number3 = tk.StringVar()

labelTitle = tk.Label(root, text="Safety In Numbers Config").grid(row=0, column=2)

labelprisoners_low = tk.Label(root, text="# of low security prisoners").grid(row=1, column=0)
labelprisoners_med = tk.Label(root, text="# of medium security prisoners").grid(row=2, column=0)
labelprisoners_high = tk.Label(root, text="# of high security prisoners").grid(row=3, column=0)

labelResult = tk.Label(root)
labelResult.grid(row=2, column=2)

prisoners_low = tk.Spinbox(root, textvariable=number1, from_=0, to=100).grid(row=1, column=2)

#prisoners_low = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
prisoners_med = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
#entryprisoners_high = tk.Entry(root, textvariable=number3).grid(row=3, column=2)

img = tk.Image("photo", file="p_icon.png")
root.tk.call('wm','iconphoto', root._w, img)
call_result1 = partial(call_result1, labelResult, number1, number2)
call_result2 = partial(call_result2, labelResult, number1, number2)
#call_result3 = partial(call_result3, labelResult, number1, number2)
#call_result4 = partial(call_result4, labelResult, number1, number2)
#call_result5 = partial(call_result5, labelResult, number1, number2)
#call_result6 = partial(call_result6, labelResult, number1, number2)

b1 = tk.Button(root, text="Calculate Low Guards", command=call_result1).grid(row=3, column=0)
b2 = tk.Button(root, text="Calculate Medium Guards", command=call_result2).grid(row=4, column=0)
#b3 = tk.Button(root, text="Calculate High Guards", command=call_result3).grid(row=5, column=0)
#b4 = tk.Button(root, text="Calculate Working Laundry Prisoners", command=call_result4).grid(row=6, column=0)
#b5 = tk.Button(root, text="Calculate Working Cleaning Room Prisoners", command=call_result5).grid(row=6, column=0)
#b6 = tk.Button(root, text="Calculate Working Cleaning Size", command=call_result6).grid(row=7, column=0)

root.mainloop()