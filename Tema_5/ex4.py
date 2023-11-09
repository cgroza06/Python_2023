class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Manager(Employee):
    def __init__(self, name, age, salary, employees=None):
        super().__init__(name, age)
        self.salary = salary
        self.employees = employees if employees is not None else []
        self.projects = {}

    def set_projects(self, employee, project):
        if employee in self.employees:
            if employee not in self.projects:
                self.projects[employee] = [project]
            else:
                self.projects[employee].append(project)
        else:
            print(f"{employee.name} is not under the management of {self.name}")

    def get_projects(self, employee):
        return self.projects.get(employee, "No projects assigned")

    def __str__(self):
        return f"Employee {self.name} is {self.age} years old, and has salary = {self.salary}, and is a manager"
class Engineer(Employee):
    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager
        self.manager.employees.append(self)

    def estimate_time_for_project(self, project, time):
        return f"{self.name} estimates time for '{project}'={time} weeks"

    def show_projects(self):
        return self.manager.get_projects(self)

    def __str__(self):
        return f"Employee {self.name} is {self.age} years old, and has salary = {self.salary}, and is managed by {self.manager.name}"
class Salesperson(Employee):
    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager
        self.manager.employees.append(self)

    def sell_project_of_engineer(self, engineer, project_to_sell):
        projects = self.manager.get_projects(engineer)
        if project_to_sell in projects:
            projects.remove(project_to_sell)
            return f"{self.name} sold project '{project_to_sell}' of {engineer.name}"
        else:
            return f"{self.name} couldn't sell project '{project_to_sell}' (not found in {engineer.name}'s projects)"

    def __str__(self):
        return f"Employee {self.name} is {self.age} years old, and has salary = {self.salary}, and is managed by {self.manager.name}"

manager = Manager("Alina", 36, 3000, [])
ana = Engineer("Ana", 24, 4000, manager)
vasile = Engineer("Vasile", 19, 3000, manager)
radu = Salesperson("Radu", 35, 3500, manager)

manager.set_projects(ana, "Project1")
manager.set_projects(vasile, "Project2")
manager.set_projects(vasile, "Project1")
print(manager)
print(ana)
print(vasile)
print(radu)
print(ana.estimate_time_for_project("Project1", 5 ))

print(vasile.show_projects())
radu.sell_project_of_engineer(vasile, "Project2")

print(vasile.show_projects())
