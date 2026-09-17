### Count vowels in a string


s = "I like the subject data science"

count = 0

for char in s:
    if char in "aeiou":
        count+=1
    else:
        pass

print(count)
print(len(s))


