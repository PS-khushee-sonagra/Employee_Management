import unittest
from validation import (
    validate_non_empty_string,
    validate_positive_number,
    validate_positive_integer,
    validate_email
)

class TestValidation(unittest.TestCase):
    def test_validate_non_empty_string_valid(self):
        self.assertEqual(validate_non_empty_string("  John Doe  ", "Name"), "John Doe")

    def test_validate_non_empty_string_invalid_type(self):
        with self.assertRaises(TypeError):
            validate_non_empty_string(123, "Name")

    def test_validate_non_empty_string_empty(self):
        with self.assertRaises(ValueError):
            validate_non_empty_string("", "Name")
        with self.assertRaises(ValueError):
            validate_non_empty_string("   ", "Name")

    def test_validate_positive_number_valid(self):
        self.assertEqual(validate_positive_number(100.5, "Salary"), 100.5)
        self.assertEqual(validate_positive_number(50, "Salary"), 50)

    def test_validate_positive_number_invalid_type(self):
        with self.assertRaises(TypeError):
            validate_positive_number("100", "Salary")
        with self.assertRaises(TypeError):
            validate_positive_number(True, "Salary")

    def test_validate_positive_number_invalid_value(self):
        with self.assertRaises(ValueError):
            validate_positive_number(0, "Salary")
        with self.assertRaises(ValueError):
            validate_positive_number(-10.5, "Salary")

    def test_validate_positive_integer_valid(self):
        self.assertEqual(validate_positive_integer(10, "ID"), 10)

    def test_validate_positive_integer_invalid_type(self):
        with self.assertRaises(TypeError):
            validate_positive_integer(10.5, "ID")
        with self.assertRaises(TypeError):
            validate_positive_integer("10", "ID")
        with self.assertRaises(TypeError):
            validate_positive_integer(True, "ID")

    def test_validate_positive_integer_invalid_value(self):
        with self.assertRaises(ValueError):
            validate_positive_integer(0, "ID")
        with self.assertRaises(ValueError):
            validate_positive_integer(-5, "ID")

    def test_validate_email_valid(self):
        self.assertEqual(validate_email("test@example.com"), "test@example.com")
        self.assertEqual(validate_email("user.name+tag@sub.domain.co.uk"), "user.name+tag@sub.domain.co.uk")

    def test_validate_email_invalid_type(self):
        with self.assertRaises(TypeError):
            validate_email(12345)

    def test_validate_email_invalid_format(self):
        invalid_emails = ["plain", "plain@", "@domain.com", "user@domain", "user@.com", "user@domain."]
        for email in invalid_emails:
            with self.subTest(email=email):
                with self.assertRaises(ValueError):
                    validate_email(email)

if __name__ == "__main__":
    unittest.main()
