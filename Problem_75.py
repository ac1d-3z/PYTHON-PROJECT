n = int(input("Enter a positive number : "))

if n < 0:
    print("Factorial does not exist for negetive numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    f = 1
    for c in range(1,n+1):
        f *= c
    print("The factorial of", n, "is", f)