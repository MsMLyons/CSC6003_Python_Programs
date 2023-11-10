# filter words based on word length
words = ["apple", "banana", "orange", "kiwi", "grapefruit", "pineapple"]
lengths = [len(word) for word in words if len(word) > 4]
print(lengths)
# ouptut --> [5, 6, 6, 10, 9]