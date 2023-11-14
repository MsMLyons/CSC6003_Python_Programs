my_string = "My cat is attacking the Funions"
my_list = my_string.split()
print(my_list)
# output --> ['My', 'cat', 'is', 'attacking', 'the', 'Funions']

new_string = ''.join(my_list)
print(new_string)
# output --> MycatisattackingtheFunions
# add more space before join to add the space between words