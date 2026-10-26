# Exercise

#Task 1

x = int(input("Enter first angle:"))
y = int(input("Enter second angle:"))
z = int(input("Enter third angle:"))
if x > 0 and y > 0 and z > 0 and x + y + z == 180:
    print(f"Valid Triangle (Angles = {x},{y},{z})")
else:
    print(f"Not a Valid Triangle (Angles = {x},{y},{z})") 

#Task 2
    
marks = int(input("Enter total marks out of 100:"))
if marks >= 90:
    print(f"Grade : A (Marks = {marks})")
elif marks >= 80:
    print(f"Grade : B (Marks = {marks})")
elif marks >= 70:
    print(f"Grade : C (Marks = {marks})")
else:
    print(f"Grade : D (Marks = {marks})")

#Task 3

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
z = int(input("Enter third number:"))
if x >= y:
    if x >= z:
        largest = x
    else:
        largest = z
else:
    if y >= z:
        largest = y
    else:
        largest = z
print(f'Largest = {largest} (Among {x},{y},{z})')   