### Find common elements between two lists



## using append

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]


result = []

for num in a:
    if num in b:
        result.append(num)

print(result)







######################################




c = [1, 2, 3, 4, 5,89]
d = [3, 4, 5, 6, 7,89]

result1 = []

# The loop takes each value from 'a' one by one
# 1st loop → num = 1
# 2nd loop → num = 2
# 3rd loop → num = 3
# 4th loop → num = 4
# 5th loop → num = 5
for num in c:

    # Check whether the current 'num' exists in 'd'
    # num = 1 → Is 1 in d? → No
    # num = 2 → Is 2 in d? → No
    # num = 3 → Is 3 in d? → Yes
    # num = 4 → Is 4 in d? → Yes
    # num = 5 → Is 5 in d? → Yes
    if num in d:

        # Add the common number to 'result1'
        # Start:    []
        # num = 3 → [3]
        # num = 4 → [3, 4]
        # num = 5 → [3, 4, 5]
        result1.append(num)

# Print the common elements
print(result1)





### sets

e = [1, 2, 3, 4, 5]
f = [3, 4, 5, 6, 7]


print((set(e)) & set(f))
