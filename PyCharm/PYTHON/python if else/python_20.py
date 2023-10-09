print("welcome to modi express")
s_place=input("Enter your starting place")
e_place=input("enter your ending place")
# input("how many people travelling with you")

total_km=13
kondotty=0
thorakkakl=2
kottappuram=5.2
pulikkal=6.9
siyamkandam=7.2
aikkarapadi=8.8
kaithakund=9.4
eleventh_mile=10
vaidiyarangadi=11
ramanatukara=13
places=kondotty,thorakkakl,kottappuram,pulikkal,siyamkandam,aikkarapadi,kaithakund,eleventh_mile,vaidiyarangadi

if(s_place==places and e_place==places):
    total=total_km*places
    print(total)
else:
    print("invalid input")


