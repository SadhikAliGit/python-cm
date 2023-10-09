user = int(input("Enter your height :"))

if user > 120:
    print("welcome to rollercoaster")
    user2 = int(input("Enter your Age :"))
    if user2 > 18:
        print("tickets price is 50")
        total=50
    elif user2 > 12:
        print("tickets price is 30")
        total=30
    elif user2 < 12:
        print("tickets price is 10")
        total=10
    else:
        print("invalid !!!!!")

    user3 = input("do you need photos while riding on roller coaster [Yes or No]")

    if user3 == "yes":
        print("100 to ticket price")
        total=total+100
        print("Total Price Is " ,total)

    elif user3 == "No":

        print(f"Total Price Is " ,total)
else:
    print("you are not eligible")

