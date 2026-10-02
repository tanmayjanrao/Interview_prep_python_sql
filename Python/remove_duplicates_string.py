### Remove duplicate characters from a string


s = "programming"
result = ""

for char in s:
    if char not in result:
        result += char

print(result)

