class Dictionary:
    def __init__(self):
        self.entries = {}

    def insert(self, key, value):
        self.entries[key] = value

    def delete(self, key):
        if key in self.entries:
            del self.entries[key]
        else:
            raise KeyError(f"Key '{key}' not found in dictionary")
        
    def get(self, key):
        if key in self.entries:
            return self.entries[key]
        else:
            raise KeyError(f"Key '{key}' not found in dictionary")
        
    def contains(self, key):
        return key in self.entries
    
    def size(self):
        return len(self.entries)
