# 13. Take two numbers and an operator (+, -, *, /) as input and perform the corresponding 

firstNumber = int(input("Enter your first Number : "))
secondNumber = int(input("Enter your second Number : "))
operator = input("Wich operator (+, -, *, /) you want to applay ? : ")

if operator == "+":
    print(firstNumber+secondNumber)
elif operator ==  "-":
    print(firstNumber-secondNumber)
elif operator == "*":
    print(firstNumber*secondNumber)
elif operator == "/":
    print(firstNumber/secondNumber)
else:
    print("Invalid operator")