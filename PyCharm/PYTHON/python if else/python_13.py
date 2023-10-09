# price calculator
height = int(input("Enter Your Height in cm :"))
total = 0
if (height<120):
    print("You are not eligable")
else:
    print("Welcome to roller coster")

    age = float(input("Enter your age :"))
    if(age<12):
        print(f"ticket price is {10}")
        total = 10
    elif(age<18):
        print(f"ticket price is {30}")
        total = 30
    elif(age>18):
        print(f"ticket price is {50}")
        total = 50
    extra_amount = (input("Do you need photos while riding photos on roller coaster (yes/no)"))
    if(extra_amount == "yes"):
        print(f"Your photos price is {100} RS")
        total += 100
        print(f"Total Price Is {total}")
    else:
        print("Total Price is ", total)

