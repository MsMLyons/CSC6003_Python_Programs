class Set:
    def __init__(self):
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)
    
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def contains(self, item):
        return item in self.items
    
    def size(self):
        return len(self.items)
    
    def union(self, other_set):
        new_set = Set()
        new_set.items = self.items[:]
        for item in other_set.items:
            if item not in self.items:
                new_set.add(item)
        return new_set
    
    def intersection(self, other_set):
        new_set = Set()
        for item in self.items:
            if item in other_set.items:
                new_set.add(item)
        return new_set
    
    def difference(self, other_set):
        new_set = Set()
        for item in self.items:
            if item not in other_set.items:
                new_set.add(item)
        return new_set
    
s1 = Set()
s1.add(1)
s1.add(2)
s1.add(3)

s2 = Set()
s2.add(2)
s2.add(3)
s2.add(4)

print(s1.contains(2))
print(s2.size())

s3 = s1.union(s2)
print(s3.items)

s4 = s1.intersection(s2)
print(s4.items)

s5 = s1.difference(s2)
print(s5.items)

# output -->
    # True
    # 3
    # [1, 2, 3, 4]
    # [2, 3]
    # [1]