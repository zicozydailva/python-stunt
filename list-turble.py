# list - ordered collection
x = [4,True, "hello", 5.5]

# Accessing elements in a list
print(x[0]) # 4

# length of list
print(len(x)) # 4

# Adding elements to a list
x.append("world") # [4, True, 'hello', 5.5, 'world']
print(x)

# Removing elements from a list
x.remove(4) # [True, 'hello', 5.5, 'world']

# Remove last element from a list
x.pop() # [True, 'hello', 5.5]

# Removing with index
x.pop(1) # [True, 5.5]

# Extending a list
x.extend([1,2,3]) # [True, 'hello', 5.5, 'world', 1, 2, 3]
print(x)