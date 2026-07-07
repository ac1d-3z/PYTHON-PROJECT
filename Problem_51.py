m = int(input("Enter a Marks (0-100)\t: "))

if m<0 or m>100:
    print("Invalid Marks !")

elif m>=80:
    print("Grade | A+")
elif m>=70:
    print("Grade | A")
elif m>=60:
    print("Grade | A-")
elif m>=50:
    print("Grade | B")
elif m>=40:
    print("Grade | C")
elif m>=33:
    print("Grade | D")

else:
    print("Grade | F (FAIL)")