age=int(input("enter your age"))

if(age>18):
  print("you can drive kiddo.")
elif(age==18):
  print("you can have  a license")
elif(age==0):
  print("youre just born how can you even drive")
else:
  print("you cant drive you are underage")


def check_fruit():
    fruit = input("Enter a fruit (apple/banana/orange): ").strip().lower()

    if fruit == "apple":
        print("Apples are red or green.")
    elif fruit == "banana":
        print("Bananas are yellow.")
    elif fruit == "orange":
        print("Oranges are orange.")
    else:
        print("Unknown fruit.")

check_fruit()




def check_diseases():
  disease=input("Enter the disease you think you  have(tb/diabetes):")
  if disease=="tb":
      print("Its because of some dirty water.")
  elif disease=="diabetes" :
      print("It is becaue of consumption of more sugars.")
  else:
      print("youre healthy")  
for _ in range (3):
  check_diseases()
  