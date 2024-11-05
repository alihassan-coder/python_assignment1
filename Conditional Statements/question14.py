# 14. Check if a year input by the user is a century year.

year = int(input("Enter year : "))

if year % 100 == 0 :
    print("This is century year.")
else :
    print("This is not century year.")