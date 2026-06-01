# while True:  #it will start an infinite loop.
#   try:   #if we gonna enter something apart from no.s the program will crash so to avaoid that thing we use this thing to encounter the problem and by this thing we stop it from crashing


#     a=int(input("Enter number 1:"))
#     b=int(input("enter number 2:"))

#     print(f"The division is {a/b}")
#   # except:
#   #   print("Some error occured")  
#   except ValueError:
#     print("PLease dont use wrong typecasts")

#   except ZeroDivisionError:
#     print("Hey dont divide by 0")

#   except Exception as e:
#     print("Some error occurred! " , e)

while True:
  a=int(input("Enter number 1:"))
  b=int(input("enter number 2:"))

  if b==0:   #This is  adeliberate error that we want to throw just to stop the user from doing shitty things.
    raise ValueError("please dont divide by 0")
  print(f"The division is {a/b}")