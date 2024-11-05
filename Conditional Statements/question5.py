# 5. Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

input_number = int(input("Enter the your number Percentage : "))

if input_number > 90:
 print("A grade")
elif input_number > 80:
 print("B grade")
elif input_number > 70:
 print("C grade")
elif input_number > 60:
 print("C grade")
elif input_number > 50:
 print("D grade")
else :
 print("F grade")