# Set operations in Python
s1 = {2, 34, 42, 56, 11, 23, 88, 22}
s2 = {23, 34, 11, 22, 99}

print("s1:", s1)
print("s2:", s2)

# 1) Union: all unique elements from both sets
print("Union (s1 | s2):", s1 | s2)
print("Union using method:", s1.union(s2))

# 2) Intersection: common elements
print("Intersection (s1 & s2):", s1 & s2)
print("Intersection using method:", s1.intersection(s2))

# 3) Difference: elements in first set but not in second
print("Difference (s1 - s2):", s1 - s2)
print("Difference (s2 - s1):", s2 - s1)

# 4) Symmetric difference: elements in either set, but not both
print("Symmetric difference (s1 ^ s2):", s1 ^ s2)
print("Symmetric difference using method:", s1.symmetric_difference(s2))

# 5) Subset / Superset checks
print("Is s2 subset of s1?", s2.issubset(s1))
print("Is s1 superset of s2?", s1.issuperset(s2))     

# 6) Disjoint check: True if no common elements
s3 = {1000, 2000}
print("Are s1 and s3 disjoint?", s1.isdisjoint(s3))
