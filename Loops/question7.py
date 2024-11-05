# 7. Find the factorial of a number using a while loop.
# factorial of 3 is 1*2*3

num = int(input("Enter a number: "))
result = 1
i = num

while i > 0 :
    result *= i 
    i -= 1
    
print(result)

