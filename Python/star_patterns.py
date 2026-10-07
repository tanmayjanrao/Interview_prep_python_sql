# Problem: Print a Right-Angled Star Pattern
# Question: Write a Python program to print the following pattern:
#
# *
# **
# ***
# ****
# *****




#### Right-Angled Star Pattern
for i in range(1,6):
    print('*' * i)




#### Left-Angled Star Pattern
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)


#### Sqaure shape
for i in range(0,6):
    if i == 0 or i == 5:
        print("*" * 5)
    else:
        print("*" + " " * 3 + "*")














#n = int(input("enter the terms : "))

#a = 0 
#b = 1


#for i in range (n):
#    print (a , end = " ")


#    c = a + b
#    a=b
#    b=c