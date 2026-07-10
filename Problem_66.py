in_num = int(input("Enter a Number : "))

t = 0

for num in range(1,in_num+1,2):
    t += num
print("Sum of odd number of 1 to",in_num,"is",t)