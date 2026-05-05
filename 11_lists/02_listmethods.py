marks=[23,4,5,7,8]

extra_marks=[53,23,32]

print(marks)

marks.append(63) # This will change the original list means will add 63 at last place
print(marks )
marks.pop(2)  #pops the 2nd index element
print(marks)
marks.extend(extra_marks)  #will add the extend marks in marks
print(marks)


marks.reverse()
print(marks)

marks.insert(2,99)  #will add 99 at the 2nd index
print(marks)

marks.sort() #in increasing order
print(marks)


marks.remove(63)
print(marks)



