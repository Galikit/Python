import csv
import random
from itertools import count
import datetime
import sys
import os

#create a class named Employee
class Employee:
        #initialize the attributes
        def __init__(self, emp_id, f_name, l_name, phone, age, role):
                self.__emp_id = emp_id
                self.__f_name = f_name
                self.__l_name = l_name
                self.__phone = phone
                self.__age = age
                self.__role = role

        #set the attributes
        def set_emp_id(self, emp_id):
                self.__emp_id = emp_id

        def set_f_name(self, f_name):
                self.__f_name = f_name

        def set_l_name(self, l_name):
                self.__l_name = l_name

        def set_phone(self, phone):
                self.__phone = phone

        def set_age(self, __age):
                self.__age = __age

        def set_role(self, role):
                self.__role = role

        #return the attributes
        def get_emp_id(self):
                return self.__emp_id

        def get_f_name(self):
                return self.__f_name

        def get_l_name(self):
                return self.__l_name

        def get_phone(self):
                return self.__phone

        def get_age(self):
                return self.__age

        def get_role(self):
                return self.__role
        #return the objects state as a string

        def __str__(self):
                return  'Employee ID: ' + str(self.__emp_id) + \
                        '\nFirst Name: ' + self.__f_name + \
                        '\nLast Name: ' + self.__l_name + \
                        '\nPhone number: ' + str(self.__phone) + \
                        '\nAge: ' + self.__age + \
                        '\nRole: ' + self.__role 

        def toCSV(self): # Write to CSV employees.csv
                with open ('employees.csv', 'a', newline='') as f:
                        fieldnames = ['Employee ID', 'First Name', 'Last Name', 'Phone Number', 'Age', 'Role']
                        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
                        f.seek(0,2)
                        if f.tell() == 0:
                                thewriter.writeheader()
                        thewriter.writerow({'Employee ID' : self.__emp_id, 'First Name' : self.__f_name, 'Last Name' : self.__l_name, 'Phone Number' : str(self.__phone), 'Age' : str(self.__age), 'Role' : self.__role})
                        print("New Employee Added! ID number: ", self.__emp_id)

def del_emp(): # Delete Employee from CSV
        lines = list()
        members = input("ID to delete: ")
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
                del_emp()

def newEmp(): # Create New Employee & write to CSV
	#Create employee object
	emp1 = Employee('emp_id','f_name', 'l_name', 'phone', 'age', 'role')
	#create Employee objects for each attribute
	emp1.set_emp_id(get_9_digits('ID: '))
	emp1.set_f_name(get_alpha_name('First Name: '))
	emp1.set_l_name(get_alpha_name('Last Name: '))
	emp1.set_phone(get_10_digits('Phone Number: '))
	emp1.set_age(get_non_negative_int('Age: '))
	emp1.set_role(input('Role: '))
	emp1.toCSV()

def listEmp(): # Print all employees from CSV
        with open('employees.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                        print(row)

# Input - Age restriction 16 ~ 80
def get_non_negative_int(prompt):
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

#  Input - 9 digits ID restriction and ID already exists restriction
def get_9_digits(prompt):
        while True:
                found = False
                try:
                        value = str(input(prompt))
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

# Input - Get Alphabet Name Longer Than 2 Characters.
def get_alpha_name(prompt):
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

# Input - Get 10 digits Phone Number
def get_10_digits(prompt):
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

def mark_attendance(): # Finding the ID and Name of the employee and marks attendance
        id_to_mark = input("Employee ID: ")
        lines = list()
        dt = datetime.datetime.now()
        with open('employees.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                found = False
                for row in reader:
                        lines.append(row)
                        for field in row:
                                if field == id_to_mark:
                                        first_name = row[1]
                                        last_name = row[2]
                                        found = True                          
        if found == True:
                print("Employee ID Found.")
                with open ('attendance.csv', 'a', newline='') as f:
                        fieldnames = ['Employee ID', 'First Name', 'Last Name', 'Date', 'Time']
                        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
                        f.seek(0,2)
                        if f.tell() == 0:
                                thewriter.writeheader()
                        thewriter.writerow({'Employee ID' : id_to_mark, 'First Name' : first_name, 'Last Name' : last_name, 'Date' : dt.strftime("%x"), 'Time' : dt.strftime("%X") })
                        print("Attendance Marked: ", id_to_mark)
        else:
                print("Employee Not Found.")
                mark_attendance()

def empAttendance(): # Requests employee ID, prints all attendance entries
        id_to_mark = input("Employee ID: ")
        with open('attendance.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                found = False
                for row in reader:
                        for field in row:
                                if field == id_to_mark:
                                        found = True
                                        print(row)
        if found == True:
                print("Employee ID Found. All Entries Printed.")
        else:
                print("Employee ID Not Found.")
                empAttendance()

def monthly_report(): # print monthly report for current month
        with open('attendance.csv', 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader, None)
                for row in reader:
                        date = row[3]
                        current_month = date.split('/')[0]
                        if int(current_month) == datetime.datetime.now().month:
                                print(row)

def late_report(): # print report for late employees past 9:30am
        with open('attendance.csv', 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader, None)
                nineAM = datetime.time(9,30)
                for row in reader:
                        time_obj = datetime.datetime.strptime(row[4], "%H:%M:%S")
                        if time_obj.time() > nineAM:
                                print(row)  

def empImport(): # File Path user input - adds listed data to employees.csv
        file_path = input("Enter the path of your file: ")
        # assert os.path.exists(file_path), "File not found at, " + str(file_path)
        if os.path.exists(file_path) == False:
                print("File Not Found, try again.")
                empImport()
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

def empDelete(): # File Path user input - removes listed data from employees.csv
        file_path = input("Enter the path of your file: ")
        if os.path.exists(file_path) == False:
                print("File Not Found, try again.")
                empDelete()
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


