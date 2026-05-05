for i in range (1 , 20):
  if i ==10:
     continue  #it says continue the statement from here itself 
    # means  dont enter 10 but continue afterwards
  print(i)





# 3) Skip short words
words = ["hi", "hello", "a", "world", "ok", "python"]
for w in words:
    if len(w) < 3:
        continue
    print(w)


# 1) Skip even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)  # prints only odd numbers



