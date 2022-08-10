# Rollercoaster ticket system
print("Welcome to RollerCoaster!!!")
height = int(input("Enter your height in cm "))
if (height >= 120):
    print("Welcome!")
    age = int(input("Enter your age in yrs "))
    if (age < 12):
        print("You need to pay $5")
    elif (age > 12 & age <18):
        print("You need to pay $7")
    elif (age > 18):
        print("You need to pay $12")
else:
    print("Get Lost!!!")
