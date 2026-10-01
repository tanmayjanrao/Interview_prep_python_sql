### Find the smallest number in a list



number = [57, 45, 23, 89, 12, 67]

smallest = number[0]

for num in number:
    if num < smallest:
        smallest = num

print(smallest)