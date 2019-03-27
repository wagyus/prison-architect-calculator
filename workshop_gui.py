__author__ = 'chrismelnyk'
import tkinter as tk
from functools import partial
work_hours = 0
def call_result(label_result, prisoners, work_hours):
    prisoners = int((prisoners.get()))
    work_hours = int((work_hours.get()))
    saw_calc = int(prisoners) / 3.3
    saw_real = round(saw_calc, 1)

    press_calc = int(saw_real) * 2
    press_real = int(round(press_calc, 1))

    tables_calc = saw_real

    squares_needed = int(prisoners) * 12
    squares_real = int(round(squares_needed, 1))

    profits = work_hours * 25 * press_real
    profits_real = int(round(profits, 2))

    result = profits_real
    label_result.config(text="Daily Profits is %d" % result)
    return
root = tk.Tk()
root.geometry('400x200+100+200')
root.title('Prison Architect Calculator')
number1 = tk.StringVar()
number2 = tk.StringVar()
labelTitle = tk.Label(root, text="Workshop Profit Calculator").grid(row=0, column=2)
labelprisoners= tk.Label(root, text="Enter the # of WORKING prisoners").grid(row=1, column=0)
labelwork_hours = tk.Label(root, text="Enter the # of hours working per day").grid(row=2, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)
entryprisoners = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entrywork_hours = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
call_result = partial(call_result, labelResult, number1, number2)
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)
root.mainloop()