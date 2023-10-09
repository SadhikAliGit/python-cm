# life calculate
# age = int(input(("Enter Your Age :")))
#
# year = 80-age
# month = year*12
#ask user

maximum = 80
maximum_month =80*12
maximum_day = 80*365
user = int(input("Enter age"))
user_age = 80-user
user_month=maximum_month-(user*12)
user_day=maximum_day-(user*365)

print(f"you have{user_age}year left,{user_month}month,{user_day}days")