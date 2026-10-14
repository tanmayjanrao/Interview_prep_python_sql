### Find common keys between two dictionaries




a = {"name": "Tanmay", "age": 24, "city": "Pune"}
b = {"name": "Rahul", "age": 25, "country": "India"}

result = []

for key in a:
    if key in b:
        result.append(key)

print(result)