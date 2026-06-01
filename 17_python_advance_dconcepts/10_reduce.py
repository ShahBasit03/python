from functools import reduce

numbers=[1,2,3,4,5]
#       it just sums up the two nos and keep going till the last no.    
#       [3,3,4,5,6]
#       [6,4,5,6]
#       [10,5,6]
#       [15,6]  
#       [21]    
def sum(a,b):

  return a+b

c = reduce(sum,numbers)  
print(c)