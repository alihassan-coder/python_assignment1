# 19. Check if a string input is uppercase, lowercase, or a mix.

string = input("Enter the string : ")
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

if string in upper :
    print("uppercase")
elif string in lower :
    print("lowercase")
else:
    print("uppercase and lowercase")