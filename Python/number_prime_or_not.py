### Check if a number is prime


num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")





# --------------------------------------------------
# WRONG VERSION - WITHOUT USING BREAK
# --------------------------------------------------

num = 6

for i in range(2, num):

    # % gives the remainder.
    # Remainder 0 → divides exactly.
    # Remainder NOT 0 → does not divide exactly.
    if num % i == 0:
        print("Not a prime number")

        # There is NO break here.
        # So the loop continues checking the next i.

    else:

        # THIS IS THE LOGIC ERROR.
        # We are saying "Prime" just because THIS particular i
        # did not divide num exactly.
        # But we need to check ALL
        print("Prime number")





num = int(input("Enter a number: "))

if num <=1:
    print("not prime number")
else:
    for i in range (2,num):
        if num % i == 0 :
            print("not prime number")
            break
        else:
            print("not prime number")
