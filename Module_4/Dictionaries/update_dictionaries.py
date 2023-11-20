d1 = {1: 'one', 2: 'two', 3: 'three'}
d2 = {4: 'four', 5: 'five', 6: 'six'}

#update d1 - most recent version of python
d1 |= d2
print(d1)
# ouptut --> {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}

d3 = {7: 'seven', 8: 'eight', 9: 'nine'}
d4 = {10: 'ten', 11: 'eleven', 12: 'twelve'}

#update d3 - from python 3.8
d3.update(d4)
print(d3)
# output --> {7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'}