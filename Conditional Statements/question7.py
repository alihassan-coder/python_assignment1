# 7. Write a program to find the largest of three numbers.
number1 = int(input("Enter first number :"))
number2 = int(input("Enter second number :"))
number3 = int(input("Enter third number :"))

if number1 > number2 and  number1 > number3:
    print(f"Largest number is {number1}")
elif number2 > number1 and  number2 > number3:
    print(f"Largest number is {number2}")
else :
    print(f"Largest number is {number3}")