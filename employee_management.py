class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def create_employee(self, name, age, emp_id, department):
        if age >= 0:
            employee = {
                'name': name,
                'age': age,
                'id': emp_id,
                'department': department
            }
            self.employees.append(employee)

    def get_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee['id'] == emp_id:
                return employee
        return None

    def delete_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee['id'] == emp_id:
                self.employees.remove(employee)
                return True
        return False