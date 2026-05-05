'''0 1 1 2 3 5 8 13 #fibnocci series
   0 1 2 3 4 5 6 7........#indexes

fib(0)=0
fib(1)=1
fib(2)= fiib(0) +fib(1)
fib(3)= fiib(1) +fib(2)
fib(4)= fiib(2) +fib(3)

fib(n)=fib(n-2) = fib(n-1)'''


def  fib(n):

#asthe formula is not valid for 0 and 1 so we need to  define them seperately that is what we called as recursion
  if(n==0 or n==1):
    return n

  return fib(n-2)  + fib (n-1)
print (fib(22))


#another example
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return  n * factorial(n-1)  


print(factorial(120))