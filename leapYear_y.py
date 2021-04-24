while True:
	try:
		year = int(input("Enter a year: "))
	except ValueError: 
		print("Input is invalid. Please enter an integer input(year)")
		continue
	break
if (year%4) != 0:
	print(str(year) + " is not a leap year.")
else:
	if(year%100) != 0:
		print(str(year) + " is a leap year.")
	else:
		if(year%400) == 0:
			print(str(year) + " is a leap year.")
		else:
			print(str(year) + " is not a leap year.")

