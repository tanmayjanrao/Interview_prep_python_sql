### Find duplicate characters in a string



s = "I like programming"

count = {}

for char in s:
    if char != " ": ## dont count spaces skips the loop 
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

print(count)

for char in count:
    if count[char] > 1:
        print(char) 


### Practice Question

### Print only the characters that appear more than once, along with how many times they appear.

str = "programming"

result = {}

for char in str:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1

print(result)

for char in result:
    if result[char] >=2:
        print(char, result[char])
    else: 
        pass


dict = {

    "tanmay":26,
    "TJ" :45,
    "Tjay" : 97
}

dict["tanmay"]+=1

print(dict["tanmay"])