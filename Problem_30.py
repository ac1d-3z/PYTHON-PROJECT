candy = int(input("Enter the number of candies: "))
children = int(input("Enter the number of children: "))

per_child = candy // children
remaining_candies = candy % children

print("Each child will receive:", per_child, "candies")
print("candies left:", remaining_candies)