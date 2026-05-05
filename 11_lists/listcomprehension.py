#create a list contatining the table of 5


a=7
table=[]
for i in range (1,11):
  table.append(a*i)
print(table)  


#there is an another easy method to do it by list comperhension method


table =[5*i for i in range(1,11 )] 
print(table)


squared=[10**x for x in range(1,10)]
print(squared)


division =[1000/x for x in range(1,16)]
print(division)