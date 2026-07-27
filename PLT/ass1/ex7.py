# Program to check if a number is a palindrome
num = int(input("Enter an integer: "))
reversed_num = int(str(num)[::-1])
if num == reversed_num:
    print("Palindrome")
else:
    print("Not Palindrome")
