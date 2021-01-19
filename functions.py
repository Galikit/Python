import csv
import random
from itertools import count
import datetime
import sys
import os
from data.employee import Employee
from data.attendance_log import mark_attendance, emp_attendance, monthly_report, late_report
from data.path import emp_import, path_delete_emp

def delete_emp(): 
	"""Get employee ID with user input and delete employee from employees.csv."""
	lines = list()
	members = input("Enter employee ID or enter 'quit' to go back.\n ID to delete: ")
	if members == 'quit':
		return
	with open('employees.csv', 'r') as readFile:
		reader = csv.reader(readFile)
		found = False
		for row in reader:
			lines.append(row)
			for field in row:
				if field == members:
					lines.remove(row)
					found = True

	with open('employees.csv', 'w', newline='') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerows(lines)

	if found == True:
		print("Employee Found and Deleted.")
	else:
		print("Employee Not Found.")
		delete_emp()

def new_employee():
	"""Create New Employee & write to CSV."""
	emp1 = Employee('emp_id','first_name', 'last_name', 'phone', 'age', 'role')
	emp1.set_emp_id(get_9_digits('ID: '))
	emp1.set_first_name(get_alpha_name('First Name: '))
	emp1.set_last_name(get_alpha_name('Last Name: '))
	emp1.set_phone(get_10_digits('Phone Number: '))
	emp1.set_age(get_non_negative_int('Age: '))
	emp1.set_role(input('Role: '))
	emp1.toCSV()

def list_employee():
	"""Print all employees entries from employees.csv."""
	with open('employees.csv', 'r') as readFile:
		reader = csv.reader(readFile)
		for row in reader:
			print(row)
	go_back = input("Enter 'back' to return to menu: ")
	if go_back == 'back':
		return
	else:
		print("Try again.")

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



