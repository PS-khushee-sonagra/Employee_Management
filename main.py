"""Console-based User Interface for Employee Management System."""

import sys

from employee import Employee
from employee_service import EmployeeService
from validation import (
    validate_non_empty_string,
    validate_positive_number,
    validate_positive_integer,
    validate_email
)

def get_input(prompt_text: str) -> str:
    """Read trimmed input from user."""
    try:
        return input(prompt_text).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting application...")
        sys.exit(0)


def prompt_non_empty_string(prompt_text: str, field_name: str) -> str:
    """Prompt the user for a non-empty string until valid input is received."""
    while True:
        val = get_input(prompt_text)
        try:
            return validate_non_empty_string(val, field_name)
        except (TypeError, ValueError) as e:
            print(f"Invalid input: {e} Please try again.")


def prompt_email(prompt_text: str) -> str:
    """Prompt the user for a valid email until valid input is received."""
    while True:
        val = get_input(prompt_text)
        try:
            return validate_email(val, "Email")
        except (TypeError, ValueError) as e:
            print(f"Invalid input: {e} Please try again.")


def prompt_positive_integer(prompt_text: str, field_name: str) -> int:
    """Prompt the user for a positive integer until valid input is received."""
    while True:
        val_str = get_input(prompt_text)
        if not val_str:
            print(f"Invalid input: {field_name} cannot be empty. Please try again.")
            continue
        try:
            val = int(val_str)
        except ValueError:
            print(f"Invalid input: {field_name} must be a valid integer. Please try again.")
            continue

        try:
            return validate_positive_integer(val, field_name)
        except (ValueError, TypeError) as e:
            print(f"Invalid input: {e} Please try again.")


def prompt_positive_number(prompt_text: str, field_name: str) -> float:
    """Prompt the user for a positive float until valid input is received."""
    while True:
        val_str = get_input(prompt_text)
        if not val_str:
            print(f"Invalid input: {field_name} cannot be empty. Please try again.")
            continue
        try:
            val = float(val_str)
        except ValueError:
            print(f"Invalid input: {field_name} must be a valid number. Please try again.")
            continue

        try:
            return validate_positive_number(val, field_name)
        except (ValueError, TypeError) as e:
            print(f"Invalid input: {e} Please try again.")


def collect_employee_data(employee_id: int) -> Employee:
    """Helper to collect and return validated employee data."""
    print(f"\nEntering details for Employee ID {employee_id}:")
    name = prompt_non_empty_string("Enter Name: ", "Name")
    email = prompt_email("Enter Email: ")
    dept = prompt_non_empty_string("Enter Department: ", "Department")
    role = prompt_non_empty_string("Enter Role: ", "Role")
    salary = prompt_positive_number("Enter Salary: ", "Salary")
    
    return Employee(employee_id, name, email, dept, role, salary)


def handle_add_employee(service: EmployeeService):
    """Option 1: Add a new employee."""
    print("\n--- Add New Employee ---")
    emp_id = prompt_positive_integer("Enter Employee ID: ", "Employee ID")
    
    # Check duplicate ID before prompting for all other fields
    if service.find_employee_by_id(emp_id) is not None:
        print(f"Error: An employee with ID {emp_id} already exists.")
        return

    try:
        new_emp = collect_employee_data(emp_id)
        service.add_employee(new_emp)
        print(f"\nSuccess: Employee '{new_emp.name}' added successfully.")
    except (TypeError, ValueError) as e:
        print(f"\nError creating employee: {e}")


def handle_view_employees(service: EmployeeService):
    """Option 2: View all employees."""
    print("\n--- All Employees ---")
    employees = service.get_all_employees()
    if not employees:
        print("No employees found.")
        return
        
    for emp in employees:
        print(emp)


def handle_search_employee(service: EmployeeService):
    """Option 3: Search employee by ID."""
    print("\n--- Search Employee ---")
    emp_id = prompt_positive_integer("Enter Employee ID to search: ", "Employee ID")
    emp = service.find_employee_by_id(emp_id)
    if emp:
        print(f"\nEmployee Found:\n{emp}")
    else:
        print(f"Employee with ID {emp_id} not found.")


def handle_update_employee(service: EmployeeService):
    """Option 4: Update employee details."""
    print("\n--- Update Employee ---")
    emp_id = prompt_positive_integer("Enter Employee ID to update: ", "Employee ID")
    existing_emp = service.find_employee_by_id(emp_id)
    if not existing_emp:
        print(f"Employee with ID {emp_id} not found.")
        return

    print(f"\nCurrent details:\n{existing_emp}")
    try:
        updated_emp = collect_employee_data(emp_id)
        service.update_employee(emp_id, updated_emp)
        print(f"\nSuccess: Employee with ID {emp_id} updated successfully.")
    except (TypeError, ValueError) as e:
        print(f"\nError updating employee: {e}")


def handle_delete_employee(service: EmployeeService):
    """Option 5: Delete employee by ID."""
    print("\n--- Delete Employee ---")
    emp_id = prompt_positive_integer("Enter Employee ID to delete: ", "Employee ID")
    try:
        service.delete_employee(emp_id)
        print(f"Success: Employee with ID {emp_id} deleted successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def handle_sort_employees_by_name(service: EmployeeService):
    """Option 7: Sort employees alphabetically by name."""
    print("\n--- Employees Sorted by Name ---")
    sorted_employees = service.sort_employees_by_name()
    if not sorted_employees:
        print("No employees found.")
        return
        
    for emp in sorted_employees:
        print(emp)


def print_menu():
    """Display the application menu."""
    print("\n==================================")
    print("    Employee Management Menu")
    print("==================================")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee by ID")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    print("7. Sort Employees by Name")
    print("==================================")


def main():
    """Main application loop."""
    service = EmployeeService()

    while True:
        print_menu()
        choice = get_input("Enter your choice (1-7): ")
        
        if choice == "1":
            handle_add_employee(service)
        elif choice == "2":
            handle_view_employees(service)
        elif choice == "3":
            handle_search_employee(service)
        elif choice == "4":
            handle_update_employee(service)
        elif choice == "5":
            handle_delete_employee(service)
        elif choice == "6":
            print("\nExiting application. Goodbye!")
            break
        elif choice == "7":
            handle_sort_employees_by_name(service)
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
