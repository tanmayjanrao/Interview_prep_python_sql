### practising loops




numbers = [45, 12, 78, 23, 9, 56, 12, 34]


smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

count = 0

for num in numbers:
    if num == smallest:
        count += 1

print("smallest:", smallest)
print("count:", count)