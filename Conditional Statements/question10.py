# 10. Write a program to determine if a given character is a vowel or consonant.

character = input("Enter the character : ").lower()

if character in "aeiou":
    print("This Chraracter is vowel")
else:
    print("This Chraracter is consonant")
