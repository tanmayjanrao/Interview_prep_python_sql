#### Count word frequency in a sentence



s = "python is easy and python is powerful"

count = {}

for word in s.split():
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)



s = "python is easy and python is powerful"

print(s.split())