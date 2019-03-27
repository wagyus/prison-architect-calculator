import time
import sys

print("Welcome to the Prison Architect Calculator.")
time.sleep(1)
print("This is the workshop calculator. Please have the number of WORKING PRISONERS ready.")
time.sleep(1)
#Begin user input
p_name = input('Please enter the name of your prison: ')
prisoners = int(input('Enter the number of WORKING prisoners: '))
work_hours = int(input("Enter the number of hours of work per day: "))

#Begin calculations
saw_calc = prisoners / 3.3
saw_real = round(saw_calc, 1)

press_calc = saw_real * 2
press_real = round(press_calc, 1)

tables_calc = saw_real

squares_needed = prisoners * 12
squares_real = round(squares_needed, 1)

profits = work_hours * 25 * press_real
profits_real = round(profits, 2)

#Print everything after
print("====================================================================")
print((p_name), "requires", (squares_real), "squares for a proper workshop area.")
print((p_name), "requires", (saw_real), "work saw(s).")
print((p_name), "requires", (press_real), "work press(es).")
print((p_name), "requires", (tables_calc), "table(s).")
print((p_name), "will make", (profits_real), "per day at", (work_hours), "work hours per day.")
print("Prison Architect Calculator by @chrismelnyk on GitHub.com")

