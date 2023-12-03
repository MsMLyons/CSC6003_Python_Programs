class Math_Operations:
    # no init method because there is no need for
    # instantiation of an object
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
result1 = Math_Operations.add(5, 3)
result2 = Math_Operations.multiply(5, 3)

print(result1, result2)

# output --> 8 15