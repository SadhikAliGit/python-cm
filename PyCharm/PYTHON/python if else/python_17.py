input1=int(input("Enter a Number"))
input2=int(input("Enter a Number"))
input3=int(input("Enter a Number"))

total = input1+input2+input3

choose = input("select your choice")
print("choice_1 choice_2 choice_3")
if choose=="choice_1":
    p1=(input1/total)*100
    print("Probility is ", p1)

elif choose=="choice_2":
    p1=(input2/total)*100
    print("Probility is ", p1)
else:
        p1 = (input3 / total) * 100
        print("Probility is ", p1)