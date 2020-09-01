"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:

Rules to follow for slices:

a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed

"""

a = [2, 4, 1, 7, 9, 6]
print(f"All elements: {a}")

# Output the second element: 4:
x = slice(1,2)
print(f"second element: {a[x]}")

# Output the second-to-last element: 9
x = a[-2]
print(f"second-to-last element: {x}")


# Output the last three elements in the array: [7, 9, 6]
x = a[-3:]
print(f"last three elements in the array: {x}")

# Output the two middle elements in the array: [1, 7]
x = a[2:4]
#x = slice(2,4)
print(f"two middle elements in the array: {x}")

# Output every element except the first one: [4, 1, 7, 9, 6]
x = a[1:]
print(f"every element except the first one: {x}")

# Output every element except the last one: [2, 4, 1, 7, 9]
x = a[:-1]
print(f"every element except the last one:{x}")

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
x = s[7:12]
print(f"Output just the 8th-12th characters: {x}")