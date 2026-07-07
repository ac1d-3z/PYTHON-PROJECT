num1 = float(input("Enter the first number\t: "))
num2 = float(input("Enter the second number\t: "))
num3 = float(input("Enter the second number\t: "))

if num1 <= num2 and num1 <= num3:
    print("Smallest Number is",num1)
elif num2 <= num1 and num2 <= num3:
    print("Smallest Number is",num2)
else:
    print("Smallest Number is",num3)