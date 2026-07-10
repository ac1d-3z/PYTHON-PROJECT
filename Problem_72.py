n = int(input("Enter a number :"))

tp = abs(n)
re_num = 0

while tp > 0:
    digit = tp % 10
    re_num = (re_num * 10) + digit
    tp = tp // 10 

if n < 0:
    re_num = -re_num
print("Reverse number is:",re_num)