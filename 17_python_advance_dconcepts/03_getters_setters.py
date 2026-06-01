# class Employee:
#   def __init__ (self,name,salary):
#     self.name=name
#     self.salary=salary


#   def first_name(self):
#     L=self.name.split(" ")  # will split the namew into their respective parts.

#     print(L)
#     return L[0]
#   def set_first_name(self,first):
#       L=self.name.split(" ")
#       new_name=f"{first} {L[1]}"
#       self.name=new_name


# e=Employee("Harry baba" ,30000)
# # e.projects=6

# # print(e.projects)   
# # print(e.salary)
# # print(e.name)
# print(e.first_name())
# e.set_first_name("Hairy")
# print(e.name)



class Employee:
  def __init__ (self,name,salary):
    self.name=name
    self.salary=salary

  @property
  def first_name(self):
    L=self.name.split(" ")  # will split the namew into their respective parts.
    print(L)
    return L[0]

  @first_name.setter  
  def set_first_name(self,first):
    L=self.name.split(" ")
    new_name=f"{first} {L[1]}"
    self.name=new_name


e=Employee("Harry baba" ,30000)

# print(e.first_name())
# e.set_first_name("Hairy")
# print(e.name)

print(e.first_name)
e.first_name= "John"
print(e.name)