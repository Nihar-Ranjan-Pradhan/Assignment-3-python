#Calculate The factorial of a number using function.
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

# Taking input from user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")