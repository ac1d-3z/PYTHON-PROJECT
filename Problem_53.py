a = int(input("Enter Your Age\t:" ))

if a>=18:
    print("You are eligible to vote")
else:
    yl = 18-a
    print("Your are not eligible to vote.")
    print("Please wait for",yl,"more year")

#Shorcut
print("Eligible" if int(input("Age: ")) >= 18 else "Not eligible")