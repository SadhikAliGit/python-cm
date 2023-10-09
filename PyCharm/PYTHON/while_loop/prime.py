user=int(input("Enter number"))
flag=False
for i in range(2,user):
    if user%i==0:
        flag=True
        break

if flag:
    print("Not Prime")
else:
    print("Prime")


