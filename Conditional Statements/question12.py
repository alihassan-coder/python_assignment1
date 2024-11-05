# 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot

temperature = int(input("Enter Temerature is celsius : "))


if temperature <= 0:
    print("Freezing")
elif 1 <= temperature <= 24:
    print("Moderate")
else:
    print("Hot")