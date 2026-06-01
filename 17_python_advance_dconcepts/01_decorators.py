def decorator(func): #decorator is a fn that takes a fn and then creates a new fn inside its body(wrapper). Then it returns that new fn.
  def wrapper():
    print("I am about to execute a fn")
    func()
    print("I have executed this fn")

  return wrapper 

def say_hello():
  print("Hello!")   

  
f= decorator(say_hello)
f()
 




#Another method of writing this thing is here where we directly write the decorator 

def decorator(func): #decorator is a fn that takes a fn and then creates a new fn inside its body(wrapper). Then it returns that new fn.
  def wrapper():
    print("I am about to execute a fn")
    func()
    print("I have executed this fn")

  return wrapper 

@decorator
def say_hello():
  print("Hello!")

say_hello()  