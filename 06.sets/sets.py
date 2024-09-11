# Creating sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Printing sets
print("Set1:", set1)
print("Set2:", set2)

# Adding elements to a set
set1.add(7)
print("Set1 after adding 7:", set1)

# Removing elements from a set (with discard and remove)
set1.discard(2)  # Discarding an element (does nothing if element is not found)
print("Set1 after discarding 2:", set1)

set1.remove(3)   # Removing an element (raises KeyError if element is not found)
print("Set1 after removing 3:", set1)

# Removing an element with pop (removes an arbitrary element)
popped_element = set1.pop()
print("Popped element:", popped_element)
print("Set1 after popping an element:", set1)

# Clearing all elements from a set
set1.clear()
print("Set1 after clearing:", set1)

# Creating a set from a list
list1 = [1, 2, 2, 3, 4]
set_from_list = set(list1)
print("Set created from list:", set_from_list)

# Union of sets
union_set = set2.union({7, 8})
print("Union of set2 and {7, 8}:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Difference of sets
difference_set = set2.difference({4, 5})
print("Difference of set2 and {4, 5}:", difference_set)

# Symmetric Difference of sets
symmetric_difference_set = set2.symmetric_difference({5, 6})
print("Symmetric difference between set2 and {5, 6}:", symmetric_difference_set)

# Subset and Superset checks
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)

is_superset = set2.issuperset({3, 4})
print("Is set2 a superset of {3, 4}?", is_superset)

# Copying a set
set_copy = set2.copy()
print("Copy of set2:", set_copy)

# Nested Sets (Sets within sets - Sets cannot contain mutable elements)
# This will raise a TypeError because sets are mutable and cannot be nested in another set
try:
    nested_set = {1, 2, frozenset({3, 4})}
    print("Nested set:", nested_set)
except TypeError as e:
    print("Error:", e)

# Iterating over a set
print("Iterating over set2:")
for element in set2:
    print(element)

# Accessing elements of a set (Note: Sets are unordered collections and do not support indexing)
try:
    print("Accessing element at index 0 of set2:", set2[0])
except TypeError as e:
    print("Error:", e)

# Example of slicing (Sets do not support slicing directly)
# Slicing is not applicable to sets since they are unordered and do not support indexing

# Concatenation is not applicable to sets as they are unordered collections
# Concatenation is typically used with lists, not with sets

# Checking membership
is_member = 3 in set2
print("Is 3 a member of set2?", is_member)

# Set comprehension (Creating a set with a comprehension)   
squared_set = {x**2 for x in range(5)}
print("Set of squares from 0 to 4:", squared_set)

# Frozen set (Immutable version of a set)
frozen_set = frozenset([1, 2, 3])
print("Frozen set:", frozen_set)
