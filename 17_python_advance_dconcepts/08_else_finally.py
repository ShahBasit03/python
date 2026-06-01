a =int(input ("Enter your numnber 1:"))
b =int(input("Enter your number 2: "))

try:
  c= a/b
  print(c)

except Exception as e:
  print(e) 

# this  is always executed no matter try executes or not
#if there is an error or not it is stilol executed
finally:
  print("this is always executed")   