in_num = int(input("Enter a Number : "))

t = 0

for num in range(5,in_num+1,5):
    t += num
print("Sum of number divisible by 5 to",in_num,"is",t)