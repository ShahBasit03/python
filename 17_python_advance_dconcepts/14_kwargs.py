def marks(**kwargs):
  #kwargs is a dictionary with all the key value pairs to marks
  for item in kwargs.keys():
    print(f"The marks of {item} is {kwargs[item]}")


marks(shubham=34, vikrant=54, jack=34, marie=90)  

