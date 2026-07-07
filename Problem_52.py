m = int(input("Enter a Marks\t: "))

pm = 33

if m < 0 or m > 100:
	print("Invalid Marks !")

elif m>=pm:
	print("Congratulations! You Passed")
else:
	print("Sorry! You Failed")