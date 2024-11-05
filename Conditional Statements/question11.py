# 11. Check if a given number is a multiple of both 3 and 5.

number = int(input("Enter the Number : "))

if number % 3 == 0 and number % 5 == 0:
    print("This number is multiple of both 3 and 5.")
else:
    print("This is not Multiple of 3 and 5")