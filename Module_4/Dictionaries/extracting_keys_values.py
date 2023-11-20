# extracting keys
my_dict = {"a": 1, "b": 2, "c": 3}
keys = my_dict.keys()
print(keys)
# output --> dict_keys(['a', 'b', 'c'])


# convert keys to a list
key_list = list(keys)
print(key_list)
# output --> ['a', 'b', 'c']


# extracting values
my_dict = {"a": 1, "b": 2, "c": 3}
values = my_dict.values()
print(values)
# output --> dict_values([1, 2, 3])


# convert values to a list
value_list = list(values)
print(value_list)
# output --> [1, 2, 3]


# extracting both keys and values
my_dict = {"a": 1, "b": 2, "c": 3}
items = my_dict.items()
print(items)
# output --> dict_items([('a', 1), ('b', 2), ('c', 3)])


# convert keys and values to a list
item_list = list(items)
print(item_list)
# output --> [('a', 1), ('b', 2), ('c', 3)]