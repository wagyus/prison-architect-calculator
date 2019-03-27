import time

print("Welcome to the Prison Architect Calculator.")
time.sleep(3)
print("This is the laundry service calculator. Please have the number of prisoners ready.")
time.sleep(3)

#Begin user input
p_name = input('Please enter the name of your prison: ')
prisoners = int(input('Enter the current number of prisoners: '))
#--------[LAUNDRY CALCULATIONS]-----------#
laundry_basket_math = 16
laundry_iron_math = 2
rooms = prisoners / 100

laundry = prisoners / laundry_basket_math
calc_baskets = round(laundry, 0)
calc_janitors = prisoners / 100
laundry_prisoners = calc_baskets
cleaning_room_workers = prisoners /10
cleaning_room_squares = cleaning_room_workers * 4
cleaning_room_amount = cleaning_room_squares / 28
cleaning_room_build = round(cleaning_room_amount, 0)

if prisoners < 25:
    laundry_machine_math = calc_baskets / 3
else:
    laundry_machine_math = 1

#Fake timer
run = "Thinking..."
sec = 0
if run == "Thinking...":
    while sec != 5:
        print("Thinking..."), sec
        time.sleep(1)
        sec += 1

#Print everything after
print("--------------------------------------------------------")
print((p_name), "requires", (calc_baskets), "baskets for an efficient laundry service.")
print((p_name), "requires", (laundry_iron_math), "ironing boards for an efficient laundry service.")
print((p_name), "requires", (laundry_machine_math), "machines for an efficient laundry service.")
print((p_name), "requires", (laundry_prisoners), "prisoner workers for an efficient laundry service.")
print((p_name), "requires", (cleaning_room_workers), "prisoners workers in the cleaning room for an efficient service.")
print((p_name), "requires", (cleaning_room_build), "cleaning rooms for an efficient service.")
print("Prison Architect Calculator by @chrismelnyk on GitHub.com")
