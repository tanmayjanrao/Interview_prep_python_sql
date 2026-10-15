
### Find the key with the maximum value in a dictionary


a = {"apple": 50, "banana": 90, "mango": 70}

max_key = None
max_value = 0

for key in a:
    if a[key] > max_value:
        max_value = a[key]
        max_key = key

print(max_key)

####################################################



a = {"apple": 50, "banana": 90, "mango": 70}

print(max(a, key=a.get))

