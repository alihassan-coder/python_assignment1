# 18. Use a loop to print numbers in reverse order within a given range.

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

if start < end:
    for num in range(end, start - 1, -1):
        print(num, end=" ")
else:
    print("The starting number should be less than the ending number.")
