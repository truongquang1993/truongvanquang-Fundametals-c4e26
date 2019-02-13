word = input("Enter a word, this will be count: ")

word1 = word.lower()
word2 = word1.replace(" ", "")

counts = {}

for i in word2:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] = counts[i] + 1

for key in sorted(counts):
    print(key, counts[key])