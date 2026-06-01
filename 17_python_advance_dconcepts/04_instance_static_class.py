class Employee:
  company="HP"

  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
# Instance method (default)
  def print_info(self):
    info=f"The name is {self.name} and the salary is {self.salary}"  
    print(info)

  # def sum(a,b): #in this case error will be shown because we havent included the self in sum so to get rif of =writing self we use this instead
  #   return a+b

  #static method:
  @ staticmethod
  def sum (a,b):
    return a+b  

  @ staticmethod
  def mul(c,d):
    return c*d
  
  #Class Methods
  @classmethod
  def print_company(cls):
    print(cls.company)

  @classmethod
  def change_company(cls,new_company):
    cls.company=new_company
 


e1=Employee("jack",3000)
e2=Employee("Jill" , 5000)
print(e1.salary) 
print(e2.salary) 
print(e2.name) 
print(Employee.company) 


e1.print_info()
e2.print_info()

print(e2.sum(5,23))
print(e2.mul(5,6))

e1.print_company()
e1.change_company("ASUS")
e1.print_company()

print(Employee.company)  #to verify company has been changed