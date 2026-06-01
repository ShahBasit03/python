# f=open("harry.txt","r")

# content=f.read()
# print(content)
# f.close()

#there is a better approach of doing this shit.
with open ("harry.txt","r") as f :
  content =f.read()
  print(content)
#no need to write f.close because using this it automatically closes the file.
