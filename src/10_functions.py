# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(number):
    return (number % 2 == 0)


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
if is_even(num):
    print("even")
else:
    print("odd")
# YOUR CODE HERE

