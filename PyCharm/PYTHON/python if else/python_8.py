# leap year criteria
year = int(input("Enter year"))
if(year%4==0 and year%100!=0) :
    print("leap year")
elif(year%100==0 and year%400==0):
    print("leap year")
else:
    print("not leap year")