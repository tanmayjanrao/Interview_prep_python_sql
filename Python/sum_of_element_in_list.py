### Find the sum of elements in a list


a = [10, 20, 30, 40, 50]

total = 0

for num in a:
    total += num

print(total)




#### using fucntion


def find_sum(a):
    total = 0

    for num in a:
        total += num

    return total

numbers = [10, 20, 30, 40, 50]


## built-in python function function 
a = [10, 20, 30, 40, 50]

total = sum(a)
print(total)

print(find_sum(numbers))
