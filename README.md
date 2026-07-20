# Employee Management System (Python Console Application)

A robust, Clean-Code-compliant, Object-Oriented Employee Management Console Application written in Python. This project utilizes a layered architecture separating validation, domain models, business logic (service layer), and the console user interface.

---

## Features

- **Object-Oriented Design**: Modeled around real-world domain structures with strict encapsulation.
- **Input Validation**: Layered validation including non-empty string checking, positive numbers (IDs, salaries), and valid email regex verification.
- **Persistent Storage**: Automatic serialization and deserialization to an `employees.json` file on data changes (Add, Update, Delete). Handles missing or corrupted storage files gracefully.
- **Alphabetical Sorting**: Instantly sort and display employees alphabetically by name without modifying the original persistence data structure.
- **Interactive UI**: User-friendly console menu with retry loops that display clear error warnings upon invalid entries.
- **Comprehensive Unit Testing**: High-coverage test suite covering all data mutations, validation constraints, and file persistence edge cases.

---

## Folder Structure

```text
EmployeeManagement/
│
├── employee.py             # Employee domain model class with properties & validation
├── employee_service.py     # Service layer managing business operations & JSON persistence
├── validation.py           # Pure input validation helper functions (regex, type, and value checks)
├── main.py                 # Presentation layer containing the interactive menu & I/O loops
├── README.md               # Project documentation
│
└── tests/                  # Directory containing all automated tests
    ├── __init__.py
    ├── test_employee.py    # Unit tests for the Employee model properties and constraints
    ├── test_employee_service.py # Unit tests for CRUD operations, sorting, and JSON serialization
    └── test_validation.py  # Unit tests for the core validation utility functions
```

---

## Installation

1. **Prerequisites**: Ensure you have Python 3.8+ installed on your system.
2. **Clone/Navigate to project**:
   ```bash
   cd EmployeeManagement
   ```

---

## How to Run

### Run the Application
Start the interactive terminal menu:
```bash
python main.py
```

### Run the Automated Tests
Run the entire unit test suite containing 38 test cases:
```bash
python -m unittest discover -s tests
```

---

## Example Usage

Upon starting, you will see the following interactive menu:

```text
==================================
    Employee Management Menu
==================================
1. Add Employee
2. View Employees
3. Search Employee by ID
4. Update Employee
5. Delete Employee
6. Exit
7. Sort Employees by Name
==================================
Enter your choice (1-7):
```

### Flow 1: Adding a New Employee
1. Choose option `1`.
2. Input the details. If you enter an invalid value (e.g., negative ID, empty name, or poorly formatted email), the system warns you immediately and prompts a retry:
   ```text
   Enter Employee ID: -10
   Invalid input: Employee ID must be greater than zero. Please try again.
   Enter Employee ID: 101
   Entering details for Employee ID 101:
   Enter Name: David Miller
   Enter Email: david.miller@example.com
   Enter Department: Engineering
   Enter Role: Analyst
   Enter Salary: 65000
   Success: Employee 'David Miller' added successfully.
   ```

### Flow 2: View and Sort Employees
1. Choose option `2` to view employees in the order they were added.
2. Choose option `7` to see them alphabetically sorted by name without changing their internal storage index.

---

## Best Practices Followed

### SOLID Principles
- **Single Responsibility Principle (SRP)**: Each file has one clearly defined job (validation, domain model, CRUD logic, user interaction).
- **Open/Closed Principle (OCP)**: Custom validations are pure functions, making it easy to extend constraints without changing existing structures.
- **Dependency Inversion Principle (DIP)**: `EmployeeService` accepts the file path as an injectable parameter, allowing tests to run safely on a clean temp file (`test_employees.json`) without affecting the production data.

### Clean Code & PEP 8
- **Encapsulation**: Used property getters and setters in `Employee` to encapsulate variables and run validations on assignment.
- **Docstrings & Type Hints**: Fully typed arguments and return types for all classes, methods, and functions alongside PEP 257-compliant docstrings.
- **Standard Library Separation**: Cleanly separated standard imports from local modules using a blank line spacing per PEP 8 standards.
- **Graceful Error Handling**: Handled file missing states and corrupted JSON states gracefully in the service layer, keeping standard error output separate.
