"""
Word Occurrences
Estimate: 32 minutes
Actual: 13 minutes

Count each word occurrence, save it in a dictionary and print results.
"""

text = input("Text: ")
# text = "this is a collection of words of nice words this is a fun thing it is"  # Test
words = text.split()
max_length = max(len(word) for word in words)
word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
for word in sorted(word_to_count):
    print(f"{word:{max_length}} :{word_to_count[word]:2}")
