### Check if a number is an Armstrong number


### An Armstrong number is a number where the sum of each digit raised to the power of the number of digits equals the original number.


num = 153
original = num
total = 0
digits = len(str(num))

while num > 0:
    digit = num % 10
    total += digit ** digits
    num = num // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")