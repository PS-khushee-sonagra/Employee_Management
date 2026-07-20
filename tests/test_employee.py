import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_employee_creation_success(self):
        emp = Employee(1, "John Doe", "john.doe@example.com", "Engineering", "Software Developer", 75000.0)
        self.assertEqual(emp.employee_id, 1)
        self.assertEqual(emp.name, "John Doe")
        self.assertEqual(emp.email, "john.doe@example.com")
        self.assertEqual(emp.department, "Engineering")
        self.assertEqual(emp.role, "Software Developer")
        self.assertEqual(emp.salary, 75000.0)

    def test_employee_property_updates(self):
        emp = Employee(1, "John Doe", "john.doe@example.com", "Engineering", "Software Developer", 75000.0)
        emp.name = "Jane Smith"
        emp.email = "jane.smith@example.com"
        emp.salary = 80000.0
        self.assertEqual(emp.name, "Jane Smith")
        self.assertEqual(emp.email, "jane.smith@example.com")
        self.assertEqual(emp.salary, 80000.0)

    def test_employee_invalid_name(self):
        with self.assertRaises(ValueError):
            Employee(1, "", "john@example.com", "Engineering", "Developer", 50000.0)

    def test_employee_invalid_salary(self):
        with self.assertRaises(ValueError):
            Employee(1, "John", "john@example.com", "Engineering", "Developer", -100.0)

    def test_employee_invalid_id(self):
        with self.assertRaises(ValueError):
            Employee(-1, "John", "john@example.com", "Engineering", "Developer", 50000.0)

    def test_employee_invalid_email(self):
        with self.assertRaises(ValueError):
            Employee(1, "John", "invalid_email", "Engineering", "Developer", 50000.0)

    def test_employee_to_dict(self):
        emp = Employee(1, "John Doe", "john.doe@example.com", "Engineering", "Software Developer", 75000.0)
        expected = {
            "employee_id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "department": "Engineering",
            "role": "Software Developer",
            "salary": 75000.0
        }
        self.assertEqual(emp.to_dict(), expected)

    def test_employee_str_representation(self):
        emp = Employee(1, "John Doe", "john.doe@example.com", "Engineering", "Software Developer", 75000.0)
        self.assertEqual(
            str(emp),
            "Employee ID: 1 | Name: John Doe | Email: john.doe@example.com | Dept: Engineering | Role: Software Developer | Salary: $75000.00"
        )

if __name__ == "__main__":
    unittest.main()
