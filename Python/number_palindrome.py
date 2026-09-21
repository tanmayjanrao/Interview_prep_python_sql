### Check if a number is a palindrome



num = input("Enter the number: ")

if num == num[::-1]:
    print("The number is palindrome")
else:
    print("The number is not palindrome")


# using function


def check_palindrome(value):
    if value == value[::-1]:
        return "The number is a palindrome"
    else:
        return "The number is not a palindrome"


number = input("Enter the number: ")

print(check_palindrome(number))

