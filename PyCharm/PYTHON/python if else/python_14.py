size = input("Enter Your pizza size(Small/Medium/Large) :")
extra=input("do you need pepper or maonise (Yes/No) :")
ex = ''
drink = ''
price = ''
if(extra=="yes"):
    ex=input("(maonise/pepper) :")

drink = input("Do you need drink (pepsi/cola) :")

if(size=="small"):
 price=50
elif(size=="medium"):
 price=80
elif(size=="large"):
   price=120

if(ex=="pepper"):
    extra_price = 20
elif(ex=="maonise"):
    extra_price =10
else:
    extra_price = 0

if(drink=="pepsi"):
    drink_price=40
elif(drink=="cola"):
    drink_price=40
else:
    drink_price=0

Total_price = price+extra_price+drink_price
print("Your total price is :", Total_price)
