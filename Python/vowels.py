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


###using function 

def count_vowels(s):
    count = 0

    for char in s:
        if char in "aeiou":
            count += 1

    return count


s = "I like the subject data science"
print(count_vowels(s))
