# 8. Create a program that checks if a given string is a palindrome

string = input("Enter Your String : ")

reversed_string = string[ ::-1]

if string == reversed_string :
    print("This string is palindrome")
else :
    print("This string is not palindrome")