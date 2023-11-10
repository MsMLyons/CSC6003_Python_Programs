name = "Alice"
age = 25

# use % operator
# %s for strings, %d for integers, %f for floats, %r for any type data
greeting = "Hello, my name is %s and I am %d years old." % (name, age)
print(greeting)
# output --> Hello, my name is Alice and I am 25 years old.

# use format() method
greeting1 = "Hello, my name is {} and I am {} years old.".format(name, age)
print(greeting1)
# output --> Hello, my name is Alice and I am 25 years old.

# use f-string method
greeting2 = f"Hello, my name is {name} and I am {age} years old."
print(greeting2)
# output --> Hello, my name is Alice and I am 25 years old.

# use format() method to precisely determine format
pi = 3.14159
formatted_pi = "The value of pi is approximately {:.2f}".format(pi)
print(formatted_pi)
# output --> The value of pi is approximately 3.14