# string1 = input("Enter a name :")
# string2 = string1.lower()
# if string2 == "abc":
#     print("Enter a another name")

# string1 = "Python is a"
# position = string1.find("is")
# print(position)

string1 = "Python is a"

rev = string1.split()
print(rev)
rev = rev[::-1]
print(rev)
rev = " ".join(rev)
print(rev)

test = "Haii python"
print(test[1:7])
print(test[::-1])