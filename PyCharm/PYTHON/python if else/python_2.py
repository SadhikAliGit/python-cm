
def find_largest_number(num1, num2, num3):
    # Compare num1 and num2 to find the maximum of the first two numbers
    max_of_first_two = max(num1, num2)
    # Compare the maximum of the first two numbers with num3 to find the overall maximum
    largest_number = max(max_of_first_two, num3)
    return largest_number

# Example usage:
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))
num3 = float(input("Enter third number :"))
result = find_largest_number(num1, num2, num3)
print("The largest number is:", result)



