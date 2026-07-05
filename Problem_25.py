list1 = [20,40,60,80,100]
list2 = [20,40,60,80,100]
list3 = list1

print("list1==list2 (Same values?):", list1 == list2)
print("list1 is list2 (Same object?):", list1 is list2)
print("list1 is list3 (Same object?):", list1 is list3)

print("list1 id:", id(list1))
print("list2 id:", id(list2))
print("list3 id:", id(list3))
