"""
Word Occurrences
Estimate: 32 minutes
Actual: 13 minutes
"""

text = input("Text: ")
words = text.split()
words.sort()
print(words)
max_length = max([len(word) for word in words])
word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
for word in word_to_count:
    print(f"{word:{max_length}} :{word_to_count[word]:2}")
