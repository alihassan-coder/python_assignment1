# 2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

user_age = int(input("Enter Your Age : "))

if user_age < 18:
    print("you are Minor person")
elif user_age < 64:
    print("you are Adult person")
else:
    print("You are a senior citizen.")