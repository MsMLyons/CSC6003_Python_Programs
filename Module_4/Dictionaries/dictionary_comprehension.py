# blueprint
# {key_expression: value_expression for item in iterable if condition}

# create a dictionary using dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)
# output --> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# filter dictionary comprehension using conditional statements
even_squares = {x: x**2 for x in range(1, 6) if x % 2 ==0}
print(even_squares)
# output --> {2: 4, 4: 16}


# transform dictionary values using dictionary comprehension
names = {"John": 5, "Alice": 6, "Bob": 7}
doubled_names = {name: count*2 for name, count in names.items()}
print(doubled_names)
# output --> {'John': 10, 'Alice': 12, 'Bob': 14}


# use cases - word frequency
# option 1
my_string = "If felt happy because I saw others were happy and I knew I should feel happy too"
dict = {}
for token in my_string.split(" "):
    dict[token] = dict.get(token, 0) + 1
print(dict)
# output --> {'If': 1, 'felt': 1, 'happy': 3, 'because': 1, 'I': 3, 'saw': 1, 'others': 1, 'were': 1, 'and': 1, 'knew': 1, 'should': 1, 'feel': 1, 'too': 1}


# option 2
frequency_dict = {token: my_string.split().count(token) for token in set(my_string.split())}
print(frequency_dict)
# output --> {'should': 1, 'feel': 1, 'happy': 3, 'because': 1, 'and': 1, 'knew': 1, 'saw': 1, 'felt': 1, 'too': 1, 'were': 1, 'I': 3, 'If': 1, 'others': 1}


# use cases - modifying keys and values of a dictionary
# remove characters from a key name
# append a single character to multiple values
d = {"my_article1": "1", "my_article2": "2"}
my_dict = {k[3:] : "$" + v for k, v in d.items()}
print(my_dict)
# ouput --> {'article1': '$1', 'article2': '$2'}


# use cases - filter dictionaries by a group of keys
# option 1
d = {1: "a", 2: "b", 3: "c", 4: "d"}
keys = [1, 2]
my_dict = {key: d[key] for key in keys}
print(my_dict)
# output --> {1: 'a', 2: 'b'}


# option 2
my_dict = {key: d[key] for key in set(keys).intersection(d.keys())}
print(my_dict)
# output --> {1: 'a', 2: 'b'}


# use cases - invert the mapping of a dictionary
# option 1
dict = {1: "a", 2: "b", 3: "c", 4: "d"}
my_dict = {}
for k,v in dict.items():
    my_dict[v] = k
print(my_dict)
# output --> {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# option 2
my_dict = {v: k for k,v in dict.items()}
print(my_dict)
# output --> {'a': 1, 'b': 2, 'c': 3, 'd': 4}