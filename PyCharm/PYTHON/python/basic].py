# def addition(num1,num2):
#     sum = num1+num2
#     print(sum)
#
# addition(3,7)

# a = lambda x:x*x
# print(a(3))


def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 5
print(factorial(num))

