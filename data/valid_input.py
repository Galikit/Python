import csv

def get_non_negative_int(prompt):
	"""Restrict user input: Age restriction 16-80."""
	while True:
		try:
			value = int(input(prompt))
		except ValueError:
			print("Sorry, try again.")
			continue
		if value <= 16 or value >= 80:
			print("Invalid input.")
			continue
		else:
			break
	return str(value)

def get_9_digits(prompt):
	"""Restrict user input to 9 digits ID and ID already exists."""
	while True:
		found = False
		try:
			value = int(input(prompt))
		except ValueError:
			print("Sorry, try again.")
			continue
		try:
			with open('employees.csv', 'r') as readFile:
				reader = csv.reader(readFile)
				for row in reader:
					for field in row:
						if field == str(value):
							found = True
		except FileNotFoundError:
			print("Creating new file.")
		if len(str(value)) != 9:
			print("9 digits ID please.")
			continue

		if found == True:
			print("Employee ID already exists.")
			continue
		else:
			break
	return str(value)

def get_alpha_name(prompt):
	"""Get alphabet name longer than 2 characters from user input."""
	while True:
		try:
			value = str(input(prompt))
		except ValueError:
			print("Sorry, try again.")
			continue
		if len(value) < 2 or value.isalpha() == False:
			print("Short names not allowed. English letters only.")
			continue
		else:
			break
	return str(value)

def get_10_digits(prompt):
	"""Get 10 digits Phone Number from user input."""
	while True:
		try:
			value = input(prompt)
		except ValueError:
			print("Sorry, try again.")
			continue
		if len(value) < 10 or value.isnumeric == False:
			print("10 digit phone number.")
			continue
		else:
			break
	return int(value)