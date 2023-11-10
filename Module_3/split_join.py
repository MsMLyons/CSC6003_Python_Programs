# Splitting and joining strings

# assign a string to a variable
sentence = "This is an awesome sentence!"

# split the string into a list of words
words = sentence.split()
print(words)
# output --> ['This', 'is', 'an', 'awesome', 'sentence!']

# join words in words list into a new string separated by ***
new_sentence = "***".join(words)
print(new_sentence)
# output --> This***is***an***awesome***sentence!