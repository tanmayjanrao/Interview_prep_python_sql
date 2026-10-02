#### Remove duplicates from a list 



a = [1, 2, 2, 3, 4, 4, 5]
print(type(a))
a = list(set(a))
print(a)
print(type(a))


## usinf loop
a = [1, 2, 2, 3, 4, 4, 5]

result = []

for num in a:
    if num not in result:
        result.append(num)

print(result)

