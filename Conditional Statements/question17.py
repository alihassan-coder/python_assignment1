# 17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

number = int(input("Enter the Number : "))

if number % 2 == 0 and number % 3 == 0 :
    print("This Number is divisible by 2 and 3")
else:
    print("This is not divisible by 2 and 3")