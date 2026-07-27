# Program to check if a number is prime
num = int(input("Enter an integer: "))
if num > 1:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):                        # check up to sqrt(num)
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a Prime number")
    else:
        print(f"{num} is Not a Prime number")
else:
    print(f"{num} is Not a Prime number")
