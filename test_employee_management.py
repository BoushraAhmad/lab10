import unittest
from employee_management import EmployeeManagementSystem

class TestEmployeeManagementSystem(unittest.TestCase):
    def setUp(self):
        self.ems = EmployeeManagementSystem()
        self.ems.employees = []  # Reset the employees list before each test case

    def test_create_employee(self):
        self.ems.create_employee('Ahmad', -30, 1, 'IT')
        self.assertEqual(len(self.ems.employees), 0) # Should not create employee, len of the employees list should be 0
        self.ems.create_employee('Ahmad', 30, 1, 'IT')
        self.assertEqual(len(self.ems.employees), 1)
  

    def test_get_employee_by_id(self):
        # Test retrieving an employee by id
        self.ems.create_employee('Ahmad', 30, 1, 'IT')
        employee = self.ems.get_employee_by_id(1)
        self.assertIsNotNone(employee)
        self.assertEqual(employee['name'], 'Ahmad')

        # Test retrieving an employee with an invalid id
        self.ems.create_employee('Ahmad', 30, 1, 'IT')
        employee = self.ems.get_employee_by_id(2)
        self.assertIsNone(employee)  # No employee should be retrieved

    def test_delete_employee_by_id(self):
        self.ems.create_employee('Ahmad', 30, 1, 'IT')
        self.assertTrue(self.ems.delete_employee_by_id(1))
        self.assertEqual(len(self.ems.employees), 0)

    def test_employee_management_integration(self):
        # Now testing integration of creating, retrieving, and deleting an employee
        self.ems.create_employee('Ahmad', 30, 1, 'IT')
        employee = self.ems.get_employee_by_id(1)
        self.assertIsNotNone(employee)
        self.assertEqual(employee['name'], 'Ahmad')
        self.assertTrue(self.ems.delete_employee_by_id(1))
        self.assertEqual(len(self.ems.employees), 0)


if __name__ == '__main__':
    unittest.main()