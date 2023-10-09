# print a star using for loop
user = int(input("Enter Row :"))

for i in range(0,user+1):
    for j in range(0,i):
        print("*" ,end="")
    print("\n")
