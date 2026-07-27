# Program to calculate factorial using a loop
num = int(input("Enter a positive integer: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is: {factorial}")
