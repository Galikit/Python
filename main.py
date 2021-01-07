from functions import Employee
import functions
#Menu

def attendance():
	print("Attendance Menu \n 1. Mark Attendance \n 2. Attendance Report \n 3. Monthly Report \n 4. Late Report \n 5.Back")
	selection=int(input("Enter choice: "))
	if selection==1:
		functions.mark_attendance()
		attendance()
	elif selection==2:
		functions.empAttendance()
		attendance()
	elif selection==3:
		functions.monthly_report()
	elif selection==4:
		functions.late_report()
	elif selection==5:
		mainMenu()
	else:
		print("Invalid choice. Enter 1-3")
		attendance()

def emp_mngmt():
	print("Employee Management Menu \n 1. Add Employee \n 2. Employee List \n 3. Delete Employee \n 4. Back")
	selection=int(input("Enter choice: "))
	if selection==1:
		functions.newEmp()	
	elif selection==2:
		functions.listEmp()
	elif selection==3:
		functions.del_emp()
	elif selection==4:
		mainMenu()
	else:
		print("Invalid choice. Enter 1-4")
		emp_mngmt()
	mainMenu()

def mainMenu():
	print("Welcome, \n 1. Attendance \n 2. Employee Management \n 3. Import File \n 4. Quit")
	selection=int(input("Enter choice: "))

	if selection==1: # Attendance Menu
		attendance()

	elif selection==2: # Employee Management Menu
		emp_mngmt()

	elif selection==3: # Import File
		import_export()
	elif selection==4:
		exit
	else:
		print("Invalid choice. Enter 1-4")
		mainMenu()

def import_export():
	print("Import Menu \n 1. Import Employees from File \n 2. Delete Employees from File \n 3. Back")
	selection=int(input("Enter choice: "))
	if selection==1: # Import from File
		functions.empImport()
		import_export()
	elif selection==2:
		functions.empDelete()
	elif selection==3:
		mainMenu()
	else:
		print("Invalid choice. Enter 1-3")
		import_export
mainMenu()
