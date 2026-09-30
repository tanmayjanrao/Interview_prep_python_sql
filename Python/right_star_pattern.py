# Problem: Print a Right-Angled Star Pattern
# Question: Write a Python program to print the following pattern:
#
# *
# **
# ***
# ****
# *****


for i in range(1,6):
    print('*' * i)


for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)