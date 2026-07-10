in_num = int(input("Enter a Number :"))

t = 0

for n in range(7,in_num+1,7):
    t += n
print("Sum of number divisible 7 to",in_num,"is",t)