import csv
import datetime

def mark_attendance():
	"""Find the ID and name of the employee and mark attendance in attendance.csv"""
	id_to_mark = input("Enter your employee ID. Enter 'quit' to go back.\n Employee ID: ")
	if id_to_mark == "quit":
		return
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

def emp_attendance():
	"""Request employee ID and print all attendance entries."""
	id_to_mark = input("Enter Employee ID or enter 'quit' to go back.\n Employee ID: ")
	if id_to_mark == "quit":
		return
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
		go_back = input("Enter 'back' to return to menu: ")
		if go_back == 'back':
			return
		else:
			print("Try again.")

	else:
		print("Employee ID Not Found.")
		emp_attendance()

def monthly_report():
	"""Print monthly report for current month from attendance.csv"""
	with open('attendance.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader, None)
		for row in reader:
			date = row[3]
			current_month = date.split('/')[0]
			if int(current_month) == datetime.datetime.now().month:
				print(row)
	go_back = input("Enter 'back' to return to menu: ")
	if go_back == 'back':
		return
	else:
		print("Try again.")

def late_report():
	"""Print report for late employees past 9:30am from attendance.csv"""
	with open('attendance.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader, None)
		nineAM = datetime.time(9,30)
		for row in reader:
			time_obj = datetime.datetime.strptime(row[4], "%H:%M:%S")
			if time_obj.time() > nineAM:
				print(row)
		go_back = input("Enter 'back' to return to menu: ")
		if go_back == 'back':
			return
		else:
			print("Try again.")
