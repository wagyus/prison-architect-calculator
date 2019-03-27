import time
import re
import sys

print("Welcome to the Prison Architect Calculator.")
time.sleep(1)
print("This is the kitchen/canteen calculator. Please have the number of prisoners ready.")
time.sleep(1)
#Begin user input
p_name = input('Please enter the name of your prison: ')
prisoners = int(input('Enter the current number of prisoners: '))

while True:
    meal_quantity = input("Enter the quantity of food (low, medium, high): ")
    if meal_quantity not in ('low', 'medium', 'high'):
        print("Not a valid choice")
    if meal_quantity in ('exit'):
        print("Goodbye.")
        sys.exit()
    else:
        break
while True:
    meal_variety = input("Enter the variety of food (low, medium, high): ")
    if meal_variety not in ('low', 'medium', 'high'):
        print("Not a valid choice")
    else:
        break

#--------[Kitchen/Canteen CALCULATIONS]-----------#
#Cooker calculations
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
#serving table + 1
#Ask for use input, then set amount of tables based on input
while True:
    int_tables = input("Enter the desired canteen layout (efficient, aesthetic): ")
    if int_tables not in ('efficient', 'aesthetic'):
        print("Not a valid choice")
    if int_tables in ('exit'):
        print("Goodbye.")
        sys.exit()
    else:
        break
if int_tables == "efficient":
    tables_real = 1
if int_tables == "aesthetic":
    tables_calc = prisoners / 8
    tables_real = round(tables_calc, 1)
#Benches calcs
benches_calc = prisoners / 4
benches = round(benches_calc, 1)
#Serving table calc
if prisoners < 40:
    serving_calc = prisoners / 40
    serving = round(serving_calc, 1)
else:
    serving = 1

bins = 1
#Don't know why I have this, kinda dumb but I guess for consistency because every other number is stored away in an 'int'

#Food Costs calculations
quantity_cost = 0
variety_cost = 0
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

#Print everything after calcs
print("=========================================================")
print((p_name), "food quantity cost is $",(quantity_cost))
print((p_name), "food variety cost is $",(variety_cost))
print((p_name), "daily total food cost is $",(daily_food_cost))
print("=========================================================")
print("You selected", int_tables, "for a canteen style.")
time.sleep(2)
print((p_name), "requires", tables_real, " table(s) for proper canteen.")
print((p_name), "requires", benches, " benches for proper canteen.")
print((p_name), "requires", serving, " serving tables for proper canteen.")
print("**********************************************************")
print("Prison Architect Calculator by @chrismelnyk on GitHub.com")