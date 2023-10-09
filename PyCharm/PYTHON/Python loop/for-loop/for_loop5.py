#simple ATM
totel_amount=100000
while True:
    dep_wid=input("deposit or widrow :")
    amount=int(input("Enter Your amount :"))

    if(dep_wid=="widrow"):
        total=totel_amount-amount
        print(f"Your Total amount is {total}")
    elif(dep_wid=="deposit"):
        total=totel_amount+amount
        print(f"Your total amount is {total}")

    ask=input("Do you need another transaction")
    if ask=="no":
        break
