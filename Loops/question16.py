# 16. Create a program to calculate the sum of the digits of an inputted integer.

num = int(input("Enter an integer: "))

sum_of_digits = 0

while num > 0:
    digit = num % 10         
    sum_of_digits += digit   
    num = num // 10         


print("Sum of the digits:", sum_of_digits)
