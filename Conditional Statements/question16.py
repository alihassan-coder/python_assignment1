# 16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

#  equilateral : a triangle that has all its sides equal in length
#  isosceles   : a triangle with (at least) two equal sides
#  scalene     : a triangle in which all three sides are in different lengths

first_side = int(input("Enter the first side of triangle : "))
second_side = int(input("Enter the second side of triangle : "))
third_side = int(input("Enter the third side of triangle : "))

if first_side + second_side > third_side and first_side + third_side > second_side and third_side + second_side > first_side :

    if first_side == second_side == third_side :
        print("This is equilateral triangle")
    elif first_side == second_side or second_side == third_side or first_side == third_side:
        print("This is isosceles triangle")
    else :
        print("This is scalene triangle")
else :
    print("Invalid sides!")


