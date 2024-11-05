# 9. Take three sides of a ritangle as input and check if they form a valid triangle.

first_side = int(input("Enter Your first side :"))
second_side = int(input("Enter Your second side :"))
third_side = int(input("Enter Your third side :"))

if (first_side + second_side > third_side and
    first_side + third_side > second_side and
    second_side + third_side > first_side):
    print("This is valid triangle")
else:
    print("This is not valid triangle")