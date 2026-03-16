x = int(input("Enter your number: "))

if x >= 80:
    print("You got A+")
elif x>=75 and x<80 :
    print("You got A")
elif x>=70 and x<75 :
    print("You got A-")
elif x>=65 and x<70 :
    print("You got B+")
elif x>=60 and x<65 :
    print("You got B-")
elif x>=55 and x<60 :
    print("You got C+")
elif x>=50 and x<55 :
    print("You got C-")
elif x>=45 and x<50 :
    print("You got D")
elif x>=40 and x<45 :
    print("You got D")
else:
    print("Failed")