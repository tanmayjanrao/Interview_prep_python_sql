### Reverse a number


num = 123456789

# Method 1
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)


# Method 2
num = 123456789

print(str(num)[::-1])