s={34,24,14,54}
s.add(99)
s.add(87)
print(s)
s.remove(24) 
print(s) #it will remove the no. only if it is present in the set otherwise it will show error
#so if we want to remove ano. we can use s.discard() the only difference is that it will not show error if that no. is not present here.


s.discard(23233)
print(s)

s.discard(99)
print(s)

s.pop()
print(s) #will just pop a random element from the set.
