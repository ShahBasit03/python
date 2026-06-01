import os

a=os.listdir("dir")
#it just helps us in ghetting all the directories and sub directories existing in a particulur file.
print(a)
print(os.getcwd())
#used to get cwd=current working directory
print(os.path.exists("harry")) #test whethe a path exists or not
#os.remove("sample_file.txt ") #chal nhi rha
os.rmdir("dir")
#used to remove only empty directory.