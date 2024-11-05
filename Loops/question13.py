# 13. Use nested loops to print a pyramid pattern of *.

rows = int(input("Enter the number of row : "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
