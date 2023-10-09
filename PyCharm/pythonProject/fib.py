user = int(input("How Many trems? :"))

n1 = 0
n2 = 1
count = 0

if user <= 0:
    print("Please enter a positive integer")

elif user == 1:
    print("Fibonacci sequence upto",user,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < user:
        print(n1)
        nth = n1 + n2

        n1 = n2
        n2 = nth
        count += 1
        