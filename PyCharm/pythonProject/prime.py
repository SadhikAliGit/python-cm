user = int(input("enter a number :"))
flag = False
for i in range(2, user):
    if user % i == 0:
        flag = True
        break

if flag:
    print("Not prime")
else:
    print("prime")

