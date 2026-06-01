class Employee:

  def __init__(self,salary,name,bond):  #init means constructor
    self.salary =salary #create an instance attribute of name salary and assign it with salary.
    self.name= name
    self.bond= bond


  def get_salary(self):
    
    return self.salary

  def get_name(self):
    return self.name


  def get_info(self):
       print(f"The name of the employee is {self.name}. Salary is {self.salary}. The total bond  is for {self.bond} years")  


e1=Employee(34000,"hARRY" , 4)  
print(e1.get_salary())
print(e1.get_name())
e1.get_info()