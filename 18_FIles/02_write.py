#write to a file  called Johndoe.txt
#it should contain data about John Doe
f=open("John Doe.txt", "w")

string='''
john doe is a nice guy and he lives in NYC and he works in python .His favourite library is pandas'''

f.write(string)
f.close()