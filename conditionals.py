x = 10
y = 30

if x > 20 :
    print("X is greater than 20")
elif x < 20:
    print("X is less than 20")
else:
    print("X is equal to 20")
    
    
    
    # OR OPERAND
if x > 20 or x < 20:
    print("X is not equal to 20")
    
# OR NOT OPERAND
if not x > 20:
    print("X is not greater than 20")
    
# AND OPERAND
if x > 5 and not x > 15:
    print("X is between the range of 5-15")