### Find duplicate characters in a string



s = "I like programming"

count = {}

for char in s:
    if char != " ":
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

print(count)

for char in count:
    if count[char] > 1:
        print(char) 
     