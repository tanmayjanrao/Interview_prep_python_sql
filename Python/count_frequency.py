### Count frequency of characters in a string



s = "AI is booming right now"

count = {}

for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)


### pratise question
t = "banana"

c = {}


for char in t:
    if char in c:
        c[char] +=1
    else:
        c[char] = 1

print(c)



#### Given a string, find the first character that appears only once.


s = "aabbcdeeff"

for char in s:
    if s.count(char) == 1:
        print(char)
        break