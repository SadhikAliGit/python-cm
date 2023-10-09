amount = int(input("Enter your amount :"))
tip = int(input("enter your tip in percentage% :"))
amount_split = int(input("how many peaople paying this amount :"))

tip_res = amount*(tip/100)
total_amount = tip_res+amount
split_res = total_amount/amount_split
result = amount+tip
print(f"Total amount is {result}")
print(f"Splited amount is {split_res}")