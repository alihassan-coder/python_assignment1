# 9. Write a program to print the first 10 Fibonacci numbers.

a, b = 0, 1

print("The first 10 Fibonacci numbers are:")
for _ in range(10):
    print(a)
    a, b = b, a + b
