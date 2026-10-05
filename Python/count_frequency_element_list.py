### Count frequency of elements in a list



a = [1, 2, 2, 3, 3, 3, 4]


count = {}


for num in a:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1


print(count)



