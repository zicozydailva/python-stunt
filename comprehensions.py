# comprehensions - one line initialisation of a list, tuple etc

x = [x for x in range(5)]
print(x) # [0, 1, 2, 3, 4]


y = [y + 5 for y in range(5)]
print(y) # [5, 6, 7, 8, 9]