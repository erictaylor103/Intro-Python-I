# For the exercise, look up the methods and functions that are available for use
# with Python lists.


x = [1, 2, 3]
x2 = x.copy()
y = [8, 9, 10]
print(hex(id(x)))
print(hex(id(x2)))
# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(hex(id(x)))
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE

#NEED TO CHECK HOW TO DO THIS ONE

x.remove(8)
print("This is it:",x)


# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in range(len(x)):
    x.append(i * 5)
print(x)