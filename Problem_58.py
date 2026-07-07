a = float(input("Enter a first side : "))
b = float(input("Enter a second side : "))
c = float(input("Enter a third side : "))

if (a+b>c) and (b+c>a) and (a+c>b):
    print("Trangle is Valid")
else:
    print("Trangle is not Valid")