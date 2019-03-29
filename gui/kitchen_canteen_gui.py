#WORK IN PROGRESS

'''__author__ = 'chrismelnyk'
import tkinter as tk
from tkinter import ttk
from functools import partial
work_hours = 0
bins = 1
values = ['low', 'medium', 'high']

def method_low():
    label.configure(text="mustang selected")
def method_medium():
    label.configure(text="focus selected")
def method_high():
    label.configure(text="tesla selected")
def method_unknown():
    label.configure(text="unknown selected")
    
def call_result1(label_result, prisoners, result1):
    prisoners = int((prisoners.get()))
    meal_quantity = int((meal_quantity.get()))
    meal_variety = int((meal_variety.get()))
    quantity_cost = 0
    variety_cost = 0
    cookers = 1
    

    if prisoners < 10:
        cookers == 1
    if meal_quantity == "low":
        cookers == prisoners / 30
    if meal_quantity == "medium":
        cookers == prisoners / 20
    if meal_quantity == "high":
        cookers == prisoners / 10

    #Cooks calculations
    cooks = cookers + 2

    #Fridge calculations
    fridge = 1
    if meal_variety == "low":
        fridge_before = cookers * 1.3
        fridge = round(fridge_before, 1)
    if meal_variety == "medium":
        fridge_before = cookers * 1.7
        fridge = round(fridge_before, 1)
    if meal_variety == "high":
        fridge_before = cookers * 2
        fridge = round(fridge_before, 1)  
    #Canteen calculations
    #if int_tables == "efficient":
        #tables_real = 1
    #if int_tables == "aesthetic":
        #tables_calc = prisoners / 8
        #tables_real = round(tables_calc, 1)
    #Benches calcs
    #benches_calc = prisoners / 4
    #benches = round(benches_calc, 1)
    #Serving table calc
    #if prisoners < 40:
        #serving_calc = prisoners / 40
        #serving = round(serving_calc, 1)
    #else:
        #serving = 1
    #Don't know why I have this, kinda dumb but I guess for consistency because every other number is stored away in an 'int'

    #Food Costs calculations
    
    if meal_quantity == "low":
        quantity_cost = 1
    if meal_quantity == "medium":
        quantity_cost = 2
    if meal_quantity == "high":
        quantity_cost = 3
    
    if meal_variety == "low":
        variety_cost_before = quantity_cost * 2 - quantity_cost
        variety_cost = round(variety_cost_before, 1)
    if meal_variety == "medium":
        variety_cost_before = quantity_cost * 6 - quantity_cost
        variety_cost = round(variety_cost_before, 1)
    if meal_variety == "high":
        variety_cost_before = quantity_cost * 10 - quantity_cost
        variety_cost = round(variety_cost_before, 1)
    #Daily food cost calculation
    daily_food_cost = (variety_cost + quantity_cost) * (prisoners)

    result1 = daily_food_cost
    label_result.config(text="daily food cost is %d" % result1)

    return

    

def create_window():
    window=tk.Toplevel(root)

root = tk.Tk()
root.geometry('600x200+100+200')
root.title('Prison Architect Calculator')
number1 = tk.StringVar()
number2 = tk.StringVar()
meal_variety = ttk.Combobox(root, 
                            values=[
                                    "low", 
                                    "medium",
                                    "high",
                                    ])
meal_quantity = ttk.Combobox(root, 
                            values=[
                                    "low", 
                                    "medium",
                                    "high",
                                    ])
labelmeal_quantity = tk.Label(root, text="Meal Quantity").grid(column=6, row=0)
meal_quantity.grid(column=6, row=1)
meal_quantity.current(1)

labelmeal_variety = tk.Label(root, text="Meal Variety").grid(column=7, row=0)
meal_variety.grid(column=7, row=1)
meal_variety.current(1)


labelTitle = tk.Label(root, text="Kitchen/Canteen Calculator").grid(row=0, column=0)
labelprisoners = tk.Label(root, text="Enter the # prisoners").grid(row=1, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=2, column=2)
entryprisoners = tk.Entry(root, textvariable=number1).grid(row=1, column=2)


call_result1 = partial(call_result1, labelResult, number1, number2)
"""call_result2 = partial(call_result2, labelResult, number1, number2)
call_result3 = partial(call_result3, labelResult, number1, number2)
call_result4 = partial(call_result4, labelResult, number1, number2)
call_result5 = partial(call_result5, labelResult, number1, number2)
call_result6 = partial(call_result6, labelResult, number1, number2)"""

b1 = tk.Button(root, text="Calculate Baskets", command=call_result1).grid(row=3, column=0)
"""b2 = tk.Button(root, text="Calculate Ironing Boards", command=call_result2).grid(row=4, column=0)
b3 = tk.Button(root, text="Calculate Laundry Machines", command=call_result3).grid(row=5, column=0)
b4 = tk.Button(root, text="Calculate Working Laundry Prisoners", command=call_result4).grid(row=6, column=0)
b5 = tk.Button(root, text="Calculate Working Cleaning Room Prisoners", command=call_result5).grid(row=6, column=0)
b6 = tk.Button(root, text="Calculate Working Cleaning Size", command=call_result6).grid(row=7, column=0)"""

root.mainloop()