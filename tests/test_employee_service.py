import unittest
import os
import json
from employee import Employee
from employee_service import EmployeeService

class TestEmployeeService(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_employees.json"
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        self.service = EmployeeService(self.test_filename)
        self.emp1 = Employee(1, "Alice", "alice@example.com", "HR", "Manager", 60000.0)
        self.emp2 = Employee(2, "Bob", "bob@example.com", "Engineering", "Developer", 80000.0)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_add_employee_success(self):
        self.service.add_employee(self.emp1)
        self.assertEqual(len(self.service.get_all_employees()), 1)
        self.assertEqual(self.service.find_employee_by_id(1).name, self.emp1.name)

    def test_add_employee_duplicate_id_raises_value_error(self):
        self.service.add_employee(self.emp1)
        duplicate_emp = Employee(1, "Charlie", "charlie@example.com", "Sales", "Rep", 45000.0)
        with self.assertRaises(ValueError):
            self.service.add_employee(duplicate_emp)

    def test_add_employee_invalid_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.service.add_employee("Not an Employee object")

    def test_get_all_employees_returns_copy(self):
        self.service.add_employee(self.emp1)
        self.service.add_employee(self.emp2)
        employees_list = self.service.get_all_employees()
        self.assertEqual(len(employees_list), 2)
        
        # Verify modifying the returned list does not affect the internal service list
        employees_list.pop()
        self.assertEqual(len(self.service.get_all_employees()), 2)

    def test_find_employee_by_id_found(self):
        self.service.add_employee(self.emp1)
        found = self.service.find_employee_by_id(1)
        self.assertEqual(found.name, self.emp1.name)

    def test_find_employee_by_id_not_found(self):
        self.service.add_employee(self.emp1)
        found = self.service.find_employee_by_id(999)
        self.assertIsNone(found)

    def test_update_employee_success(self):
        self.service.add_employee(self.emp1)
        updated_emp = Employee(1, "Alice Smith", "alice.smith@example.com", "HR", "Senior Manager", 70000.0)
        self.service.update_employee(1, updated_emp)
        
        found = self.service.find_employee_by_id(1)
        self.assertEqual(found.name, "Alice Smith")
        self.assertEqual(found.role, "Senior Manager")
        self.assertEqual(found.salary, 70000.0)

    def test_update_employee_not_found_raises_value_error(self):
        updated_emp = Employee(1, "Alice Smith", "alice.smith@example.com", "HR", "Senior Manager", 70000.0)
        with self.assertRaises(ValueError):
            self.service.update_employee(1, updated_emp)

    def test_update_employee_id_mismatch_raises_value_error(self):
        self.service.add_employee(self.emp1)
        # Try updating ID 1 with an Employee object that has ID 2
        with self.assertRaises(ValueError):
            self.service.update_employee(1, self.emp2)

    def test_update_employee_invalid_type_raises_type_error(self):
        self.service.add_employee(self.emp1)
        with self.assertRaises(TypeError):
            self.service.update_employee(1, "Not an Employee")

    def test_delete_employee_success(self):
        self.service.add_employee(self.emp1)
        self.service.add_employee(self.emp2)
        self.service.delete_employee(1)
        self.assertEqual(len(self.service.get_all_employees()), 1)
        self.assertIsNone(self.service.find_employee_by_id(1))
        self.assertEqual(self.service.find_employee_by_id(2).name, self.emp2.name)

    def test_delete_employee_not_found_raises_value_error(self):
        self.service.add_employee(self.emp1)
        with self.assertRaises(ValueError):
            self.service.delete_employee(999)

    def test_sort_employees_by_name(self):
        emp_c = Employee(3, "Charlie", "charlie@example.com", "Sales", "Rep", 45000.0)
        self.service.add_employee(emp_c)
        self.service.add_employee(self.emp2)  # Name: Bob
        self.service.add_employee(self.emp1)  # Name: Alice
        
        sorted_list = self.service.sort_employees_by_name()
        self.assertEqual(sorted_list[0].name, "Alice")
        self.assertEqual(sorted_list[1].name, "Bob")
        self.assertEqual(sorted_list[2].name, "Charlie")
        
        # Verify the original list is not modified in terms of contents order
        original_list = self.service.get_all_employees()
        self.assertEqual(original_list[0].name, "Charlie")
        self.assertEqual(original_list[1].name, "Bob")
        self.assertEqual(original_list[2].name, "Alice")

    def test_persistence_saves_on_add(self):
        self.service.add_employee(self.emp1)
        # Create a new service instance reading the same file
        new_service = EmployeeService(self.test_filename)
        all_emps = new_service.get_all_employees()
        self.assertEqual(len(all_emps), 1)
        self.assertEqual(all_emps[0].name, "Alice")

    def test_persistence_saves_on_update(self):
        self.service.add_employee(self.emp1)
        updated_emp = Employee(1, "Alice Smith", "alice.smith@example.com", "HR", "Senior Manager", 70000.0)
        self.service.update_employee(1, updated_emp)
        
        new_service = EmployeeService(self.test_filename)
        emp = new_service.find_employee_by_id(1)
        self.assertEqual(emp.name, "Alice Smith")
        self.assertEqual(emp.role, "Senior Manager")

    def test_persistence_saves_on_delete(self):
        self.service.add_employee(self.emp1)
        self.service.add_employee(self.emp2)
        self.service.delete_employee(1)
        
        new_service = EmployeeService(self.test_filename)
        self.assertEqual(len(new_service.get_all_employees()), 1)
        self.assertIsNone(new_service.find_employee_by_id(1))

    def test_load_data_corrupted_json(self):
        # Write corrupted JSON to the file
        with open(self.test_filename, "w", encoding="utf-8") as f:
            f.write("invalid json data {{{{")
        
        corrupted_service = EmployeeService(self.test_filename)
        self.assertEqual(len(corrupted_service.get_all_employees()), 0)

    def test_load_data_invalid_format(self):
        # Write valid JSON but not a list
        with open(self.test_filename, "w", encoding="utf-8") as f:
            json.dump({"not": "a list"}, f)
        
        corrupted_service = EmployeeService(self.test_filename)
        self.assertEqual(len(corrupted_service.get_all_employees()), 0)

if __name__ == "__main__":
    unittest.main()
