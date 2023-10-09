oparator=input("Enter a oparator(+,-,/,*,%) : ")
num1=float(input("Enter first number :"))
num2=float(input("Enter second number"))

if(oparator=="+"):
    print(num1+num2)
elif(oparator=="-"):
    print(num1-num2)
elif(oparator=="/"):
    print(num1/num2)
elif(oparator=="*"):
    print(num1*num2)
elif(oparator=="%"):
    print(num1%num2)
else:
    print("Oops..!!")
