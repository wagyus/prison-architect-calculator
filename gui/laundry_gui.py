__author__ = 'chrismelnyk'
import tkinter as tk
from functools import partial
work_hours = 0

def call_result1(label_result, prisoners, result1):
    prisoners = int((prisoners.get()))

    laundry_basket_math = 16
    laundry_iron_math = 2
    rooms = int(prisoners / 100)

    laundry = int(prisoners / laundry_basket_math)
    calc_baskets = int(round(laundry, 0))
    calc_janitors = int(prisoners / 100)
    laundry_prisoners = int(calc_baskets)
    cleaning_room_workers = int(prisoners / 10)
    cleaning_room_squares = int(cleaning_room_workers * 4)
    cleaning_room_amount = int(cleaning_room_squares / 28)
    cleaning_room_build = int(round(cleaning_room_amount, 0))
    if prisoners < 25:
        laundry_machine_math = int(calc_baskets / 3)
    else:
        laundry_machine_math = int(1)
        
    result1 = calc_baskets
    label_result.config(text="# of baskets is %d" % calc_baskets)

    return
def call_result2(label_result, prisoners, result2):
    prisoners = int((prisoners.get()))

    laundry_basket_math = 16
    laundry_iron_math = 2
    rooms = int(prisoners / 100)

    laundry = int(prisoners / laundry_basket_math)
    calc_baskets = int(round(laundry, 0))
    calc_janitors = int(prisoners / 100)
    laundry_prisoners = int(calc_baskets)
    cleaning_room_workers = int(prisoners / 10)
    cleaning_room_squares = int(cleaning_room_workers * 4)
    cleaning_room_amount = int(cleaning_room_squares / 28)
    cleaning_room_build = int(round(cleaning_room_amount, 0))
    if prisoners < 25:
        laundry_machine_math = int(calc_baskets / 3)
    else:
        laundry_machine_math = int(1)
        
    result2 = laundry_iron_math
    label_result.config(text="# of iron boards is %d" % laundry_iron_math)

    return
def call_result3(label_result, prisoners, result3):
    prisoners = int((prisoners.get()))

    laundry_basket_math = 16
    laundry_iron_math = 2
    rooms = int(prisoners / 100)

    laundry = int(prisoners / laundry_basket_math)
    calc_baskets = int(round(laundry, 0))
    calc_janitors = int(prisoners / 100)
    laundry_prisoners = int(calc_baskets)
    cleaning_room_workers = int(prisoners / 10)
    cleaning_room_squares = int(cleaning_room_workers * 4)
    cleaning_room_amount = int(cleaning_room_squares / 28)
    cleaning_room_build = int(round(cleaning_room_amount, 0))
    if prisoners < 25:
        laundry_machine_math = int(calc_baskets / 3)
    else:
        laundry_machine_math = int(1)
    result3 = laundry_machine_math
    label_result.config(text="# of laundry machines is %d" % laundry_machine_math)
    return
def call_result4(label_result, prisoners, result4):
    prisoners = int((prisoners.get()))

    laundry_basket_math = 16
    laundry_iron_math = 2
    rooms = int(prisoners / 100)

    laundry = int(prisoners / laundry_basket_math)
    calc_baskets = int(round(laundry, 0))
    calc_janitors = int(prisoners / 100)
    laundry_prisoners = int(calc_baskets)
    cleaning_room_workers = int(prisoners / 10)
    cleaning_room_squares = int(cleaning_room_workers * 4)
    cleaning_room_amount = int(cleaning_room_squares / 28)
    cleaning_room_build = int(round(cleaning_room_amount, 0))
    if prisoners < 25:
        laundry_machine_math = int(calc_baskets / 3)
    else:
        laundry_machine_math = int(1)
        
    result4 = calc_baskets
    label_result.config(text="# of workers in the laundry room is %d" % calc_baskets)
    return
def call_result5(label_result, prisoners, result5):
    prisoners = int((prisoners.get()))

    laundry_basket_math = 16
    laundry_iron_math = 2
    rooms = int(prisoners / 100)

    laundry = int(prisoners / laundry_basket_math)
    calc_baskets = int(round(laundry, 0))
    calc_janitors = int(prisoners / 100)
    laundry_prisoners = int(calc_baskets)
    cleaning_room_workers = int(prisoners / 10)
    cleaning_room_squares = int(cleaning_room_workers * 4)
    cleaning_room_amount = int(cleaning_room_squares / 28)
    cleaning_room_build = int(round(cleaning_room_amount, 0))
    if prisoners < 25:
        laundry_machine_math = int(calc_baskets / 3)
    else:
        laundry_machine_math = int(1)
        
    result5 = cleaning_room_workers
    label_result.config(text="# of prisoners working in cleaning room is %d" % cleaning_room_workers)
    return
def call_result6(label_result, prisoners, result6):
    prisoners = int((prisoners.get()))

    laundry_basket_math = 16
    laundry_iron_math = 2
    rooms = int(prisoners / 100)

    laundry = int(prisoners / laundry_basket_math)
    calc_baskets = int(round(laundry, 0))
    calc_janitors = int(prisoners / 100)
    laundry_prisoners = int(calc_baskets)
    cleaning_room_workers = int(prisoners / 10)
    cleaning_room_squares = int(cleaning_room_workers * 4)
    cleaning_room_amount = int(cleaning_room_squares / 28)
    cleaning_room_build = int(round(cleaning_room_amount, 0))
    if prisoners < 25:
        laundry_machine_math = int(calc_baskets / 3)
    else:
        laundry_machine_math = int(1)
        
    result5 = cleaning_room_build
    label_result.config(text="Size of one cleaning room (in squares) is %d" % cleaning_room_build)
    return

def create_window():
    window=tk.Toplevel(root)

root = tk.Tk()
root.geometry('800x200+100+200')
root.title('Laundry Calculator')
number1 = tk.StringVar()
number2 = tk.StringVar()
labelTitle = tk.Label(root, text="Laundry Config Calculator").grid(row=0, column=2)
labelprisoners= tk.Label(root, text="Enter the # prisoners").grid(row=1, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=2, column=2)
entryprisoners = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
img = tk.Image("photo", file="p_icon.png")
root.tk.call('wm','iconphoto', root._w, img)

call_result1 = partial(call_result1, labelResult, number1, number2)
call_result2 = partial(call_result2, labelResult, number1, number2)
call_result3 = partial(call_result3, labelResult, number1, number2)
call_result4 = partial(call_result4, labelResult, number1, number2)
call_result5 = partial(call_result5, labelResult, number1, number2)
call_result6 = partial(call_result6, labelResult, number1, number2)

b1 = tk.Button(root, text="Calculate Baskets", command=call_result1).grid(row=3, column=0)
b2 = tk.Button(root, text="Calculate Ironing Boards", command=call_result2).grid(row=4, column=0)
b3 = tk.Button(root, text="Calculate Laundry Machines", command=call_result3).grid(row=5, column=0)
b4 = tk.Button(root, text="Calculate Working Laundry Prisoners", command=call_result4).grid(row=6, column=0)
b5 = tk.Button(root, text="Calculate Working Cleaning Room Prisoners", command=call_result5).grid(row=6, column=0)
b6 = tk.Button(root, text="Calculate Working Cleaning Size", command=call_result6).grid(row=7, column=0)

root.mainloop()