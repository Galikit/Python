import os
import csv

def emp_import():
	"""Request File Path from user input - import data to employees.csv"""
	while True:
		try:
			file_path = input("Enter the path of your file or enter 'quit' to go back to menu.\n File Path: ")
		except FileNotFoundError:
			print("File Not Found Error.")
			continue
		if file_path == "quit":
			return
		elif not os.path.exists(file_path) and not os.path.isfile(file_path):
			print("Invalid Path.")
			continue
		elif file_path.lower().endswith(('.csv')) == False:
			print("Please Choose a CSV File!")
			continue
		else:
			print("File Found!")
			break
	new_lines = list()
	lines = list()
	with open(file_path, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			new_lines.append(row)
	with open("employees.csv", 'r') as readFile:
		reader = csv.reader(readFile)
		next(reader, None)
		for row in reader:
			lines.append(row)
	new_list = new_lines + lines
	to_add = set(tuple(row) for row in new_list)
	with open('employees.csv', 'w', newline='') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerows(to_add)
		print("Employees Added.")
		return

def path_delete_emp():
	"""Request File Path from user input and Removes listed data from employees.csv"""
	while True:
		try:
			file_path = input("Enter the path of your file or enter 'quit' to go back to menu.\n File Path: ")
		except FileNotFoundError:
			print("File Not Found Error.")
			continue
		if file_path == "quit":
			return
		elif not os.path.exists(file_path) and not os.path.isfile(file_path):
			print("Invalid Path.")
			continue
		elif file_path.lower().endswith(('.csv')) == False:
			print("Please Choose a CSV File!")
			continue
		else:
			print("File Found!")
			break		
	new_lines = list()
	lines = list()
	with open(file_path, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			new_lines.append(row)
	with open("employees.csv", 'r') as readFile:
		reader = csv.reader(readFile)
		next(reader, None)
		for row in reader:
			lines.append(row)
	new_list = [x for x in lines if x not in new_lines]
	with open('employees.csv', 'w', newline='') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerows(new_list)
		print("Employees Deleted.")
		return