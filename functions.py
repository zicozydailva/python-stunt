def func(x, y):
    print("Hello World", x, y)
    return x * y, x/y # returning multiplication and divison value
    
print(func(10, 20)) # compacted result

r1, r2 = func(10, 20)
print(r1, r2) # seperated result