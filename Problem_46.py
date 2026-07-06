Number1 = int(input("Enter the first number:"))
Number2 = int(input("Enter the second number:"))

if Number1 > Number2:
    print(Number1, "is the largest number.")

elif Number2 > Number1:
    print(Number2, "is the largest number.")

else:
    print("Both numbers are equal.")