user = int(input("Enter year"))

if user%4==0 and user%100!=0 :
    print("leap year")
elif user%100==0 and user%400==0:
    print("leaf year")
else:
    print("Not leap year")
