# BMI calculator

mass = float(input("Enter Your weight :"))
height = float(input("Enter your height in meter :"))

result = mass/(height*height)
if(result<16):
    print("Severe Thiness :", result)
elif(result>17):
    print("Moderate Thiness :", result)
elif(result>18.5):
    print("Mid Thiness :", result)
elif(result>25):
    print("Normal :", result)
elif(result>30):
    print("Overweight :", result)
else:
    print("Obse  :", result)
