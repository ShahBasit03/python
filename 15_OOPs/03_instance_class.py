class Employee:
  company="ASUS" #This is aclass attribute

  def __init__(self,salary,name,bond,company):  #init means constructor
    self.salary =salary #create an instance attribute of name salary and assign it with salary.
    self.name= name
    self.bond= bond
    self.company=company


  def get_salary(self):
    
    return self.salary

  def get_name(self):
    return self.name

  def get_company(self):
    return self.company 



  def get_info(self):
       print(f"The name of the employee is {self.name}. Salary is {self.salary}. The total bond  is for {self.bond} years")  

e1=Employee(34000,"Harry",4,"TESLA")
print(e1.company) #will always prevent instance attribute whenever present.

#now to print class attribute
print(Employee.company)




#Object introspection.
print(dir(e1)) 