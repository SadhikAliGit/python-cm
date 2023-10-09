# find which box stored too many balls
box1 = int(input("Enter first box stored balls number :"))
box2 = int(input("Enter second box stored balls  number :"))
box3 = int(input("Enter third box stored balls  number :"))
if(box1>box2 and box1>box3):
    print("first box stored too many balls")
elif(box2>box3 and box2>box1):
    print("second box stored too many balls")
else:
    print("third box stored too many balls")
