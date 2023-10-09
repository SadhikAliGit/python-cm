
def brute_force_sqrt(number):
    if number < 0:
        raise ValueError("Input number must be non-negative")

    for guess in range(int(number) + 1):
        if guess * guess == number:
            return guess

    return None

if __name__ == "__main__":
    try:
        input_number = float(input("Enter a non-negative number: "))
        result = brute_force_sqrt(input_number)

        if result is not None:
            print(f"The square root of {input_number} is {result}.")
        else:
            print("Square root not found. The number may not be a perfect square.")
    except ValueError as e:
        print(f"Error: {e}")
