# SET - unique values without duplicates
# using a set is very beneficial and faster for looking things up

y = {} # typeof dictionary
x = set() # typeo set: empty set

setWithValues = {4, 32, 3, 3} # a set with values in it
setValues = {4, 32, 3, 2, 8, 3} 

# check if element exist in set
print(33 in setWithValues) # False
print(32 in setWithValues) # True

# Validate union of a set
print(setWithValues.union(setValues))
print(setWithValues.difference(setValues))
print(setWithValues.intersection(setValues))