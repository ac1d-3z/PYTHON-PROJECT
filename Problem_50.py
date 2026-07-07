y = int(input("Enter a Year\t: "))

if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    print(y,"Is a Leap Year.")

else:
    print(y,"Isn\'t a Leap Year.")