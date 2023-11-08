class Employee:
    def __init__(self, id_emp, name, salary, function):
        self.id_emp = id_emp
        self.name = name
        self.salary = salary
        self.function = function

    def __str__(self):
        return f"ID={self.id_emp}, Name={self.name}, Salary={self.salary}, Function={self.function}"

class Manager(Employee):
    def __init__(self, id_emp, name, salary, department):
        super().__init__(id_emp, name, salary, "Manager")
        self.department = department

    def __str__(self):
        return f"ID={self.id_emp}, Name={self.name}, Salary={self.salary}, Function= {self.function}, Department={self.department}"

class Engineer(Employee):
    def __init__(self, id_emp, name, salary, project):
        super().__init__(id_emp, name, salary, "Engineer")
        self.project = project

    def __str__(self):
        return f"ID={self.id_emp}, Name={self.name}, Salary={self.salary}, Function= {self.function}, Project={self.project}"

class Salesperson(Employee):
    def __init__(self, id_emp, name, salary, region):
        super().__init__(id_emp, name, salary, "Salesperson")
        self.region = region

    def __str__(self):
        return f"ID={self.id_emp}, Name={self.name}, Salary={self.salary}, Function= {self.function}, Region={self.region}"

Manager1 = Manager(2, "Jill", 6000, "Marketing")
Engineer1 = Engineer(3, "Jack", 4000, "Python")
Salesperson1 = Salesperson(4, "Jane", 2000, "North")

print(Manager1)
print(Engineer1)
print(Salesperson1)
