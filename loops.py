# for Loops

# range takes start, stop, step paramters, passing just one defaults to just "stop", "step" states how our iteration should flow and start is actually the starting point, NOTE: stop value isn't included

for i in range(10):
    print()
    
    # start at 1, stop at 9, increment by 2 on every iteration
for i in range(1,10,2):
    print()
    
    
    # this counts from 10 down to 0
for i in range(10,-1,-1):
    print()
    
    
# Loop through a list
x = [1,2,3,4,5]
for i in range(len(x)):
    print(x[i])
    
    # ALTERNATIVELY
for i, element in enumerate(x):
    print(x, element)
    
    
# WHILE LOOP
i=0
while i < 10:
    print('run')
    i+=1