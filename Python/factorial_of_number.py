### Find factorial of a number


### Input: n = 5
### Output: 120
### Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(num:int):

    result = 1

    for i in range(num,0,-1):
        result = result * i

    return result
 

   
    

num = int(input("Enter the number: "))

print("Factorial :" , (factorial(num)))


# --------------------------------------------------
# EXPLANATION
# --------------------------------------------------

# If the input is 5:
#
# num = 5
#     ↓
# factorial(5)
#     ↓
# result = 1
#     ↓
# i = 5 → 1 × 5 = 5
#     ↓
# i = 4 → 5 × 4 = 20
#     ↓
# i = 3 → 20 × 3 = 60
#     ↓
# i = 2 → 60 × 2 = 120
#     ↓
# i = 1 → 120 × 1 = 120
#     ↓
# return 120
#     ↓
# Factorial: 120


# --------------------------------------------------
# FOR LOOP
# --------------------------------------------------

# range() can take 3 values:
#
# range(start, stop, step)
#
# range(num, 0, -1)
#
# num   → START at num
# 0     → STOP at 0 (0 is NOT included)
# -1    → STEP: decrease by 1 each time
#
# For num = 5:
#
# The loop produces:
#
# 5 → 4 → 3 → 2 → 1
#
# So we effectively do:
#
# 1 × 5 × 4 × 3 × 2 × 1 = 120