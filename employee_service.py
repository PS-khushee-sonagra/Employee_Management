"""Service layer for managing Employee business logic and data persistence."""

import json
import sys
from typing import List, Optional

from employee import Employee

class EmployeeService:
    """Manages employee data operations and JSON persistence."""

    def __init__(self, filepath: str = "employees.json"):
        """Initialize the employee service with a filepath and load existing data."""
        self.filepath = filepath
        self._employees: List[Employee] = []
        self.load_data()

    def load_data(self):
        """Load employees from the JSON file.
        
        Handles missing or corrupted files gracefully by warning the user
        and starting with an empty list.
        """
        self._employees = []
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError("JSON data must be a list of employee records.")
                
                for item in data:
                    try:
                        emp = Employee(
                            employee_id=item["employee_id"],
                            name=item["name"],
                            email=item["email"],
                            department=item["department"],
                            role=item["role"],
                            salary=item["salary"]
                        )
                        self._employees.append(emp)
                    except (KeyError, TypeError, ValueError) as e:
                        print(f"Warning: Skipping corrupted employee record: {item}. Error: {e}", file=sys.stderr)
        except FileNotFoundError:
            # Missing file is handled gracefully: start with an empty list.
            pass
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Warning: Corrupted file '{self.filepath}' (Failed to parse JSON/invalid format). Error: {e}", file=sys.stderr)
            print("Starting with an empty employee list.", file=sys.stderr)

    def save_data(self):
        """Save all employees to the JSON file.
        
        Raises:
            IOError: If writing to the file fails.
        """
        try:
            data = [emp.to_dict() for emp in self._employees]
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except (IOError, TypeError) as e:
            print(f"Error: Failed to save data to '{self.filepath}'. {e}", file=sys.stderr)

    def add_employee(self, employee: Employee):
        """Add an employee and save to disk.
        
        Args:
            employee: The Employee object to add.
            
        Raises:
            TypeError: If the input is not an instance of Employee.
            ValueError: If an employee with the same ID already exists.
        """
        if not isinstance(employee, Employee):
            raise TypeError("Only Employee instances can be added.")
            
        if self.find_employee_by_id(employee.employee_id) is not None:
            raise ValueError(f"Employee with ID {employee.employee_id} already exists.")
            
        self._employees.append(employee)
        self.save_data()

    def get_all_employees(self) -> List[Employee]:
        """Get a copy of the list of all employees.
        
        Returns:
            A list containing all registered Employee objects.
        """
        return list(self._employees)

    def find_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        """Find an employee by their unique ID.
        
        Args:
            employee_id: The ID of the employee to search for.
            
        Returns:
            The Employee object if found, otherwise None.
        """
        for emp in self._employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def update_employee(self, employee_id: int, updated_employee: Employee):
        """Update an existing employee's details and save to disk.
        
        Args:
            employee_id: The ID of the employee to update.
            updated_employee: The updated Employee object.
            
        Raises:
            TypeError: If the updated_employee is not an instance of Employee.
            ValueError: If the employee to update is not found, or if
                        the updated_employee's ID does not match the target employee_id.
        """
        if not isinstance(updated_employee, Employee):
            raise TypeError("Updated employee must be an Employee instance.")
            
        if updated_employee.employee_id != employee_id:
            raise ValueError(
                f"Employee ID mismatch. Cannot change ID from {employee_id} to {updated_employee.employee_id}."
            )

        for idx, emp in enumerate(self._employees):
            if emp.employee_id == employee_id:
                self._employees[idx] = updated_employee
                self.save_data()
                return
                
        raise ValueError(f"Employee with ID {employee_id} not found.")

    def delete_employee(self, employee_id: int):
        """Delete an employee and save to disk.
        
        Args:
            employee_id: The ID of the employee to delete.
            
        Raises:
            ValueError: If no employee with the specified ID exists.
        """
        for idx, emp in enumerate(self._employees):
            if emp.employee_id == employee_id:
                self._employees.pop(idx)
                self.save_data()
                return
                
        raise ValueError(f"Employee with ID {employee_id} not found.")

    def sort_employees_by_name(self) -> List[Employee]:
        """Return a new list of employees sorted alphabetically by name.
        
        Does not modify the original employee list.
        """
        return sorted(self._employees, key=lambda emp: emp.name.lower())
