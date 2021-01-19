import csv

class Employee:
	"""Create a class. Initialize, set and get the attributes."""
	def __init__(self, emp_id, first_name, last_name, phone, age, role):
		self.__emp_id = emp_id
		self.__first_name = first_name
		self.__last_name = last_name
		self.__phone = phone
		self.__age = age
		self.__role = role

	def set_emp_id(self, emp_id):
		self.__emp_id = emp_id

	def set_first_name(self, first_name):
		self.__first_name = first_name

	def set_last_name(self, last_name):
		self.__last_name = last_name

	def set_phone(self, phone):
		self.__phone = phone

	def set_age(self, __age):
		self.__age = __age

	def set_role(self, role):
		self.__role = role

	def get_emp_id(self):
		return self.__emp_id

	def get_first_name(self):
		return self.__first_name

	def get_last_name(self):
		return self.__last_name

	def get_phone(self):
		return self.__phone

	def get_age(self):
		return self.__age

	def get_role(self):
		return self.__role

	def __str__(self):
		"""return the objects state as a string."""
		return  'Employee ID: ' + str(self.__emp_id) + \
			'\nFirst Name: ' + self.__first_name + \
			'\nLast Name: ' + self.__last_name + \
			'\nPhone number: ' + str(self.__phone) + \
			'\nAge: ' + self.__age + \
			'\nRole: ' + self.__role 

	def toCSV(self): 
		"""Write to new employee to CSV employees.csv."""
		with open ('employees.csv', 'a', newline='') as f:
			fieldnames = ['Employee ID', 'First Name', 'Last Name', 'Phone Number', 'Age', 'Role']
			thewriter = csv.DictWriter(f, fieldnames=fieldnames)
			f.seek(0,2)
			if f.tell() == 0:
				thewriter.writeheader()
			thewriter.writerow({'Employee ID' : self.__emp_id, 'First Name' : self.__first_name, 'Last Name' : self.__last_name, 'Phone Number' : str(self.__phone), 'Age' : str(self.__age), 'Role' : self.__role})
			print("New Employee Added! ID number: ", self.__emp_id)