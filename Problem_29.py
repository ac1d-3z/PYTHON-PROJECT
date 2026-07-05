total_sec = int(input("Enter the total seconds: "))

min = total_sec // 60
re_sec = total_sec % 60

print(total_sec, "seconds is equal to", min, "minutes and", re_sec, "seconds.")