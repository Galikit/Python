from data.employee_func import new_employee, list_employee, delete_emp
from data.attendance_log import mark_attendance, emp_attendance, monthly_report, late_report
from data.path import emp_import, path_delete_emp

def attendance():
	print("Attendance Menu \n 1. Mark Attendance \n 2. Attendance Report \n 3. Monthly Report \n 4. Late Report \n 5.Back")
	selection=int(input("Enter choice: "))
	if selection==1:
		mark_attendance()
		attendance()
	elif selection==2:
		emp_attendance()
		attendance()
	elif selection==3:
		monthly_report()
		attendance()
	elif selection==4:
		late_report()
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
		new_employee()	
	elif selection==2:
		list_employee()
	elif selection==3:
		delete_emp()
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
		emp_import()
		import_export()
	elif selection==2:
		path_delete_emp()
		import_export()
	elif selection==3:
		main_menu()
	else:
		print("Invalid choice. Enter 1-3")
		import_export
main_menu()
