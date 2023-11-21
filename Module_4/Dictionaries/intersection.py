# Intersection
# Write a function that finds the intersection of two dictionaries, returning a
# new dictionary with key-value pairs common to both input dictionaries

def dict_intersection(dict1, dict2):
    intersection = {}
    for key, value in dict1.items():
        if key in dict2 and dict2[key] == value:
            intersection[key] = value
    return intersection