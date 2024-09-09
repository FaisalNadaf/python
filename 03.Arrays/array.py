# Define an initial list of integers
myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Print the original array
print("Original Array:", myArray)

# Print the length of the array
print("Length of Array:", len(myArray))

# Remove the first occurrence of the value 3 from the array
myArray.remove(3)
print("Array after removing 3:", myArray)

# Remove and print the item at index 3 (now index 3 has value 4 after the removal)
print("Popped item (index 3):", myArray.pop(3))

# Print the last item of the array
print("Last item of the array:", myArray[-1])

# Update the item at index 5 to 99
myArray[5] = 99

# Update the last item of the array to 9999
myArray[-1] = 9999

# Print the updated array
print("Array after updates:", myArray)

# Extend the array by concatenating additional elements
myArray = myArray + [11, 22, 33, 44, 55]
print("Array after concatenation:", myArray)

# Print a slice of the array from index 1 to 3 (inclusive of 1, exclusive of 4)
print("Array slice [1:4]:", myArray[1:4])

# Print a slice of the array from the fourth-to-last item to the second-to-last item
print("Array slice [-4:-1]:", myArray[-4:-1])

# Append an item to the end of the array
myArray.append(66)
print("Array after appending 66:", myArray)

# Insert an item at index 2
myArray.insert(2, 77)
print("Array after inserting 77 at index 2:", myArray)

# Count occurrences of the value 99
count_99 = myArray.count(99)
print("Number of occurrences of 99:", count_99)

# Find the index of the first occurrence of value 9999
index_9999 = myArray.index(9999)
print("Index of 9999:", index_9999)

# Remove all items from the array
myArray.clear()
print("Array after clearing all items:", myArray)

# Re-initialize the array for further operations
myArray = [10, 20, 30, 40, 50]

# Reverse the order of the array
myArray.reverse()
print("Array after reversing:", myArray)

# Sort the array in ascending order
myArray.sort()
print("Array after sorting:", myArray)

# Create a copy of the array
copiedArray = myArray.copy()
print("Copy of the array:", copiedArray)

# Create a new array with one element "a" and repeat it 10 times
newArray = ["a"]
newArray = newArray * 10
print("Repeated Array:", newArray)

# Define a two-dimensional array (a list of lists)
twoDimensionalArray = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

# Print the two-dimensional array
print("Two-Dimensional Array:", twoDimensionalArray)

# Print the first sublist of the two-dimensional array
print("First sublist:", twoDimensionalArray[0])

# Print the second item of the third sublist
print("Item at [2][1]:", twoDimensionalArray[2][1])

# Print the first item of the last sublist
print("First item of the last sublist:", twoDimensionalArray[-1][0])
