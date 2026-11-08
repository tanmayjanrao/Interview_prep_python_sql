### Problem: Find the first non-repeating character



s = "aabbcde"


count = {}

for char in s:
    if char in count:
        count[char] +=1
    else:
        count[char] = 1

for char in s:
    if count[char] == 1:
        print(char)
        break
else:
    print(None)