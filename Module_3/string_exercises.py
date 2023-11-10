# Write code that prompts for:
# 1. The user is prompted to enter a sentence
# 2. The user is prompted to enter a word
# Then, output the count for the number of times that the word appears.

sentence = input("Please enter a sentence: ")
word = input("Please enter a word: ")

count = sentence.lower().count(word.lower())

message = f"The number of times '{word}' appears in your sentence is {count} time(s)."

print(message)