def func(*agrs, **kwargs):
    print(agrs, kwargs)
    
    
func(1,2,3,4,5, x=1, y=2, z=3)



# x = [1,22,2244,2233]
# pairs = [(1,2), (3,4), (5,6)]

# for pair in pairs:
#     func(*pair) # tuple or list example
#     func(**{'x': 1, 'y': 2}) # dictionary example
    
# print(*x)
   