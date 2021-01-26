import csv
from data.valid_input import get_10_digits, get_9_digits, get_alpha_name, get_non_negative_int
from data.employee import Employee

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