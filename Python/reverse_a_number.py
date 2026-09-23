### Reverse a number

num = 123456789

reverse = 0

while num > 0:
    digit = num % 10  
    reverse = reverse * 10 + digit
    num = num // 10 

print(reverse)
print(type(reverse))





### Reverse a negative number.

num = -12345

if num < 0:
    reverse = -int(str(abs(num))[::-1])
else:
    reverse = int(str(num)[::-1])

print(reverse)
print(type(reverse))







