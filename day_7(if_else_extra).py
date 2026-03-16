num = int(input("Enter your number: "))

if num % 2 == 0 and num>0:
    print("Your number is even")
elif num == 0:
    print("Your number is Zero")
else:
    print("Your number is odd")


# Image import
from IPython.display import Image
Image("cd.png")