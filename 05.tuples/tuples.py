# Tuples in Python

# 1. Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

# 2. Nested tuple
nested_tuple = (1, (2, 3), (4, 5))
print("Nested Tuple:", nested_tuple)

# 3. Accessing elements
# Accessing single element
print("Element at index 2:", my_tuple[2])

# Accessing elements from a nested tuple
print("Element from nested tuple:", nested_tuple[1][1])

# 4. Slicing a tuple (returns a new tuple)
slice_tuple = my_tuple[1:4]
print("Sliced Tuple (1:4):", slice_tuple)

# 5. Built-in functions with tuples
print("Length of tuple:", len(my_tuple))  # len() to get the length
print("Maximum value:", max(my_tuple))    # max() to get the max element
print("Minimum value:", min(my_tuple))    # min() to get the min element
print("Sum of elements:", sum(my_tuple))  # sum() to get the sum of all elements

# 6. Iterating through a tuple
print("Iterating through tuple:")
for item in my_tuple:
    print(item)

# 7. Concatenation of tuples
concat_tuple = my_tuple + (6, 7, 8)
print("Concatenated Tuple:", concat_tuple)

# 8. Multiplying tuples
multiplied_tuple = my_tuple * 2
print("Tuple after multiplication:", multiplied_tuple)

# 9. Checking for membership
print("Is 3 in tuple?", 3 in my_tuple)

# 10. Editing tuples
# Tuples are immutable, so we cannot directly edit. However, we can convert to a list, modify it, and convert back to a tuple.
tuple_as_list = list(my_tuple)
tuple_as_list[0] = 10
edited_tuple = tuple(tuple_as_list)
print("Edited Tuple:", edited_tuple)

# 11. Deleting a tuple
# Tuples themselves are immutable, but we can delete the whole tuple.
del my_tuple
# Uncomment the line below to see the result (this will raise an error as the tuple is deleted)
# print(my_tuple)

# 12. Tuple unpacking
a, b, c, d, e = (10, 20, 30, 40, 50)
print("Unpacked values: a =", a, ", b =", b, ", c =", c, ", d =", d, ", e =", e)

# 13. Nested tuple iteration
print("Iterating through a nested tuple:")
for sub_tuple in nested_tuple:
    if isinstance(sub_tuple, tuple):
        for item in sub_tuple:
            print(item)
    else:
        print(sub_tuple)

# 14. Using tuple as keys in dictionaries (because tuples are immutable)
tuple_dict = {(1, 2): "A", (3, 4): "B"}
print("Value associated with key (1,2):", tuple_dict[(1, 2)])

# 15. Index method - finding the position of an element
print("Index of 4 in tuple:", concat_tuple.index(4))

# 16. Counting occurrences of an element in a tuple
print("Count of 4 in tuple:", concat_tuple.count(4))
