class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)
class Manager(Employee):
    mgr_count=0
    def __init__(self, name,salary, department):
        department=f"F05"
        self.name=name
        self.salary=salary
        self.department=department
        Manager.mgr_count+=1
    def display_employee(self):
        print (f"Department: {self.department}")
    def display_employee(self):
        print("Name : ", self.name, " Salary: ", self.salary, "Department:", self.department)   
m1=Manager("John", 5000, "F01")
m2=Manager("Mark", 7500, "F02")
m3=Manager("Daria", 9000, "F03")
m4=Manager("Sarah", 4500, "F04")
m1.display_employee()
m2.display_employee()
m3.display_employee()
m4.display_employee()
e1=Employee("ION", 2500)
e2=Employee("Rares", 8500)
e3=Employee("Mihai", 8970)
e4=Employee("Maria", 5790)
e1.display_employee()
e2.display_employee()
e3.display_employee()
e4.display_employee()
print(f"Nr. manager= {Manager.mgr_count}") 
print (f"Nr. employee= {Employee.empCount}")



    
  
    
    

