import functions

def attendance():
	print("Attendance Menu \n 1. Mark Attendance \n 2. Attendance Report \n 3. Monthly Report \n 4. Late Report \n 5.Back")
	selection=int(input("Enter choice: "))
	if selection==1:
		functions.mark_attendance()
		attendance()
	elif selection==2:
		functions.emp_attendance()
		attendance()
	elif selection==3:
		functions.monthly_report()
		attendance()
	elif selection==4:
		functions.late_report()
		attendance()
	elif selection==5:
		main_menu()
	else:
		print("Invalid choice. Enter 1-3")
		attendance()

def emp_mngmt():
	print("Employee Management Menu \n 1. Add Employee \n 2. Employee List \n 3. Delete Employee \n 4. Back")
	selection=int(input("Enter choice: "))
	if selection==1:
		functions.new_employee()	
	elif selection==2:
		functions.list_employee()
	elif selection==3:
		functions.delete_emp()
		emp_mngmt()
	elif selection==4:
		main_menu()
	else:
		print("Invalid choice. Enter 1-4")
		emp_mngmt()
	main_menu()

def main_menu():
	print("Welcome, \n 1. Attendance \n 2. Employee Management \n 3. Import File \n 4. Quit")
	selection=int(input("Enter choice: "))

	if selection==1:
		attendance()
	elif selection==2:
		emp_mngmt()
	elif selection==3:
		import_export()
	elif selection==4:
		exit
	else:
		print("Invalid choice. Enter 1-4")
		main_menu()

def import_export():
	print("Import Menu \n 1. Import Employees from File \n 2. Delete Employees from File \n 3. Back")
	selection=int(input("Enter choice: "))
	if selection==1:
		functions.emp_import()
		import_export()
	elif selection==2:
		functions.path_delete_emp()
		import_export()
	elif selection==3:
		main_menu()
	else:
		print("Invalid choice. Enter 1-3")
		import_export
main_menu()
