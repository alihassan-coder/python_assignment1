# 20. Create a program that evaluates if an inputted number is prime.

number = int(input("Enter a number to check if it's prime: "))

if number < 2:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False 
            break
    
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
