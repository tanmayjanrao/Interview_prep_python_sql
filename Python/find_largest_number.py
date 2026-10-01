### Find the largest number in a list




numbers = [10, 45, 23, 89, 12, 67]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)