Number1 = int(input("Enter the first Number:"))
Number2 = int(input("Enter the second Number:"))

if Number1 < Number2:
    print(Number1, "is the smallest number.")
elif Number2 < Number1:
    print(Number2, "is the smallest number.")
else:
    print("Both numbers are equal.")