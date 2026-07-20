"""Employee model class representing an employee in the system."""

from validation import (
    validate_non_empty_string,
    validate_positive_number,
    validate_positive_integer,
    validate_email
)

class Employee:
    """Represents an Employee with validation for all attributes."""

    def __init__(self, employee_id: int, name: str, email: str, department: str, role: str, salary: float):
        """Initialize an Employee instance.
        
        Raises:
            TypeError: If input types are incorrect.
            ValueError: If input values are invalid.
        """
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self.role = role
        self.salary = salary

    @property
    def employee_id(self) -> int:
        """Get employee ID."""
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value: int):
        """Set employee ID with validation."""
        self._employee_id = validate_positive_integer(value, "Employee ID")

    @property
    def name(self) -> str:
        """Get employee name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Set employee name with validation."""
        self._name = validate_non_empty_string(value, "Name")

    @property
    def email(self) -> str:
        """Get employee email."""
        return self._email

    @email.setter
    def email(self, value: str):
        """Set employee email with validation."""
        self._email = validate_email(value, "Email")

    @property
    def department(self) -> str:
        """Get employee department."""
        return self._department

    @department.setter
    def department(self, value: str):
        """Set employee department with validation."""
        self._department = validate_non_empty_string(value, "Department")

    @property
    def role(self) -> str:
        """Get employee role."""
        return self._role

    @role.setter
    def role(self, value: str):
        """Set employee role with validation."""
        self._role = validate_non_empty_string(value, "Role")

    @property
    def salary(self) -> float:
        """Get employee salary."""
        return self._salary

    @salary.setter
    def salary(self, value: float):
        """Set employee salary with validation."""
        self._salary = float(validate_positive_number(value, "Salary"))

    def to_dict(self) -> dict:
        """Return a dictionary representation of the employee.
        
        Useful for potential serialization/storage.
        """
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "email": self.email,
            "department": self.department,
            "role": self.role,
            "salary": self.salary
        }

    def __str__(self) -> str:
        """Return a user-friendly string representation of the employee."""
        return f"Employee ID: {self.employee_id} | Name: {self.name} | Email: {self.email} | Dept: {self.department} | Role: {self.role} | Salary: ${self.salary:.2f}"
