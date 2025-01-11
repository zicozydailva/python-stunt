x = "tim"

def func(name):
    # x = name # this won't change the value of x
    
    global x # this will change the value of x - not ideal to use


print(x) # tim
func("joe") 
print(x) # tim