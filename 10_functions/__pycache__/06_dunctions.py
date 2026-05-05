def sum(a,b):
  #a and b are local varables
  c=a+b
  z=1 #it creates  a local variable called z which is destropyed after this function returns
  print(z)
  return c

z=8 #z is a global variable

print(sum(4,6))  
print(z)