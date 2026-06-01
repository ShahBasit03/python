# def func(**kwargs,*args): # this is a wrong order
def func(*args,**kwargs):
  print(args)
  print(kwargs)

func(1,34,43,54,jack=32,jill=23,marie=23)  