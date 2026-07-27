# Program to calculate the sum of digits of an integer
num = int(input("Enter an integer: "))
digit_sum = 0
while num > 0:
    digit = num % 10       
    digit_sum += digit     
    num //= 10             
print(f"Sum of digits: {digit_sum}")
