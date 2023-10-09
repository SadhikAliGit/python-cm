# Death calculator

age = int(input("Enter Your age :"))
maxyear = 80
year = maxyear-age
month = 12*year
days = 365*year
hour = 24*days
minutes = 60*hour
second = 60*days
micro_sec = 60*second

if(age>maxyear):
    print("Oooh shitt You are dead")
else:
    print(f"You have {year} year left")
    print(f"You have {month} month left")
    print(f"You have {days} days left")
    print(f"You have {hour} hour left")
    print(f"you have {minutes} minutes left")
    print(f"you have {second} seconds left")
    print(f"you have {micro_sec} micro second left")
