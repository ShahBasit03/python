numbers=[1,2,3,4,5]

# def square(x):
#   return x*x

# new =list( map(square,numbers))  
new=list(map(lambda x: x*x, numbers))
print(new)





digits=[23,32,44,77,89]

odds=list(filter(lambda x: x%2==1,digits))
print(odds)