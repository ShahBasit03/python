#class is  blueprint or a template Eg; Form for an EXAM THT contains name,age,electivr=es, fathers name etc.

#object:Specific instance created from the template  (class).Eg, Form which contains the data from Jhon Doe.

class Employee:
  company ="HP"

  def get_salary(self):  #self refers to the object of the class which is being created.
    
    return 40000

e = Employee() # An object of class Employee is created here
print(e.get_salary())    #Employee e's get salary method is called  

e1=Employee()
print(e1.get_salary())

print(e1.company)
print(e.company)
