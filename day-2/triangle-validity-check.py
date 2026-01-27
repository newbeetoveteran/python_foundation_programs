#program to check whether the angles form a triangle
#concept : sum of all 3 angles must be 180 to form the trianble.

angle1 = int(input("enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))
sum_of_angles = angle1 + angle2 + angle3

if angle1 > 0 and angle2 > 0 and angle3 >0 and sum_of_angles == 180:
    print("This is a valid traiangle/or forms a triangle")
else:
    print("This is not a valid triangle/does not form a triangle")