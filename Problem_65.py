in_num = int(input("Enter a Number : "))

t = 0

for num in range(2,in_num+1,2):
    t += num
print("The sum of even numbers from 1 to",num,"is",t)