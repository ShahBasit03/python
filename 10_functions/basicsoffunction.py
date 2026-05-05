# a=1
# b=2
# c=3

# average=((a+b+c)/3)
# print(average)


#every fn in python starts with def

def average(a,b,c): 
  d=(a+b+c)/3.0
  return d
  # print(d)   #nothing will happen if we will execute this.


average(3,5,1)        #now it will take these values and the average gets printed.


average(22,78,23)
average(4,2,1)


a1=average(2,8,2)
print(a1)
b1=average(4,2,1)
print(b1)
#none will be printed using this way so we have to do it in another way

#so to get the value of a1 and b1 we have to replace print(d) with return d

# now only a1=average(2,8,2)
# print(a1)
# b1=average(4,2,1)
# print(b1) part will be printed when using return