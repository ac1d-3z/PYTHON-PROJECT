num = int(input("Enter a Number : "))

print("Number divisible by both 3 to 5 up to",num,"are : ")
for i in range(1,num+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i,end="")