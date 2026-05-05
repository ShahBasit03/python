def add(a,b,plus=10):
  return a+b + plus

c=add(3,5,8)
print(c)

d=add(66,22,10)
print(d)


#keyword arguments
def student(name,age):
  print (f"Name:{name}, Age:{age}")

student(age=25,name="basit")  
student(age=35,name="sabit")  
student(age=1  5,name="sahil")  