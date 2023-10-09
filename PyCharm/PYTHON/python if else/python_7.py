# find  simple interest
amount = int(input("Enter Your Amount :"))
rate = int(input("Enter Your rate of intrest :"))
time = int(input("Enter Your time duration :"))

result =(amount*time*rate/100)
print("Your interest is :", result)
print("Total balance is :", amount+result)
