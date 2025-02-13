# Dictionary with key and value pairs

x = {"key": 4, "key2": 5, "key3": 6}
print(x["key2"])

# To check if key exist
print('key' in x)

# Get all values from dictionary as list
print(list(x.values()))

# delete key
del x['key']
print(list(x.values()))


# To loop
for key, value in x.items():
    print(key, value)
    
# To get just keys
for key in x.keys():
    print(key)