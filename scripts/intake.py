import time
import sys

print("Welcome to the Prison Architect Calculator.")
time.sleep(1)
print("This is the laundry service calculator. Please have the number of prisoners ready.")
time.sleep(1)

#Begin user input
p_name = input('Please enter the name of your prison: ')
prisoners_intake_low = int(input('Enter the number of low security prisoners to intake: '))
prisoners_intake_med = int(input('Enter the number of medium security prisoners to intake: '))
prisoners_intake_high = int(input('Enter the number of high security prisoners to intake: '))

while True:
    intake_config = input("Enter the configuration of intaking prisoners (safety in numbers, balanced, hurt me pleanty, or custom)): ")
    if intake_config not in ('safety in numbers', 'balanced ', 'hurt me pleanty', 'custom'):
        print("Not a valid choice")
    if intake_config in ('exit'):
        print("Goodbye.")
        sys.exit()
    else:
        break

high_armed_guard = 0.10



#LOW SECURITY INTAKE GUARD CALC
if prisoners_intake_low >= 0 and intake_config == "safety in numbers":
    #low_safe_guards = 1
    low_safe_calc = ((prisoners_intake_low/4))
    low_safe_guards = round(low_safe_calc, 1)
if prisoners_intake_low < 0:
    print("ERROR ENTER A NUMBER GREATER THAN 0")
    sys.exit()
    
#MEDIUM SECURITY INTAKE GUARD CALC
if prisoners_intake_med >= 0 and intake_config == "safety in numbers":
    #med_safe_guards = int(1)
    med_safe_calc = (prisoners_intake_med/3)
    med_safe_guards = round(med_safe_calc, 1)
if prisoners_intake_med < 0:
    print("ERROR ENTER A NUMBER GREATER THAN 0")
    sys.exit()

#HIGH SECURITY INTAKE GUARD CALC
if prisoners_intake_high >= 0 and intake_config == "safety in numbers":   
    #high_safe_guards = 1
    high_safe_calc = (prisoners_intake_high/2)
    high_safe_guards = round(high_safe_calc, 1)
if prisoners_intake_high < 0:
    print("ERROR ENTER A NUMBER GREATER THAN 0")
    sys.exit()

print((low_safe_guards), "amount of guards is needed for low security prisoners.")
print((med_safe_guards), "amount of guards is needed for medium security prisoners.")
print((high_safe_guards), "amount of guards is needed for high security prisoners.")