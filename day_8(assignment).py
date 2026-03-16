length = int(input("Enter length: "))
width = int(input("Enter width: "))

if length== width:
    print("It is square")
else:
    print("It is not square")

print("############################################")

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
if x>y and x>z:
    print("x is the greatest number")
elif y>z and y>z:
    print("y is the greatest number")
else:
    print("z is the greatest number")


print("############################################")
class_held = int(input("Total class held in the semester: "))
attended = int(input("Total class attended in the semester: "))

percentage = float((attended/class_held)*100)

if percentage>=75:
    print("Congratulations, You are allowed to sit in exam")
else:
    print("Sorry, You are not allowed to sit in exam")

