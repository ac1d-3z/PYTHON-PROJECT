num1 = float(input("Enter the first number\t: "))
num2 = float(input("Enter the second number\t: "))
num3 = float(input("Enter the thrid number\t: "))

if num1 >= num2 and num1 >=num3:
    print("largest number is ",num1)
elif num2 >= num1 and num2 >= num3:
    print("largest number is ", num2)
else:
    print("largest number is ",num3)