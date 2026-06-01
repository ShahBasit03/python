#append  to an existing file  called Johndoe.txt
#it should add data about John Doe's hometown
f=open("John Doe.txt", "a")   #a here means to append

string='''
john doe initiaLLY lived in Phoenix.He is a very nice guy. '''

f.write(string)
f.close()