### practising loops




numbers = [45, 12, 78, 23, 9, 56, 12, 34]


smallest = float('inf')
second_smallest = float('inf')

for num in numbers:

    if num < smallest:
        second_smallest = smallest
        smallest = num

    elif num < second_smallest and num != smallest:
        second_smallest = num

print("second smallest:", second_smallest)