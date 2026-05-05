# tu=(3,17,23)
# a,b,c=tu
# print(a,b,c)   #that means a ,b,c have been assigned above values resp)

# tup=(1,3,4,1,6,22,3,78)
# print(tup.count(1) ) #will show us how maNY TIMES 1 IS IN THE TUPLE
# print(tup.index(22))  # will give me the index of first occurence of 22
# print(len(tup))
# print(max(tup))




# 1) Return multiple values from a function
def get_min_max(nums):
    return (min(nums), max(nums))   # tuple

mn, mx = get_min_max([4, 9, 1, 7])
print("min,max:", mn, mx)


# 2) Coordinates (x, y) or (x, y, z)
player_pos = (120, 340,560,878)
enemy_pos = (500, 120,43,567,543)

print("player x:", player_pos[3])
print("enemy y:", enemy_pos[1])


# 3) RGB colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
print("red:", RED, "green:", GREEN)


# 4) Database-like records (fixed fields)
student = ("Asha", 19, "CS")
name, age, dept = student
print(name, age, dept)

kiryana=("moong dal",56,"razma")
dal1,packets,dal2=kiryana
print(dal1,packets,dal2)


# 5) Dictionary keys (tuples are hashable, lists are not)
distances = {}
distances[("NYC", "Boston")] = 350
distances[("LA", "SF")] = 383
print(distances[("LA", "SF")])


# 6) Swap values quickly (tuple packing/unpacking)
a, b = 10, 20
a, b = b, a
print("a,b:", a, b)


# 7) Loop with index + value (tuple from enumerate)
items = ["pen", "book", "bag"]
for i, item in enumerate(items,start=2):
    print(i, item)


# 8) Function args as tuple (*args)
def total(*nums):   # nums is a tuple
    return sum(nums)

print(total(10, 20, 30))
