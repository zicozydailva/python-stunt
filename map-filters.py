# Maps and Filters

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

mp = map(lambda x, y: x + y, x, y)
nmp = map(lambda i: i * 2, x) # loop through all values of x and multiply by 2

print(list(mp))
print(list(nmp))

fmp = filter(lambda i: i % 2 == 0, x) # filter out all odd numbers
print(list(fmp))