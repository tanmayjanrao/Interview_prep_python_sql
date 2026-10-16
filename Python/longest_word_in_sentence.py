#### Find the longest word in a sentence


s = "Python is easy to learn"

words = s.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)