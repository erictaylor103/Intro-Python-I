"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys

import os
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE


args = sys.argv

for i in args:
    print("Argument:", i)


# Print out the OS platform you're using:
# YOUR CODE HERE
import platform
osPlatform = sys.platform
print("Platform:", osPlatform, "\n")

# Print out the version of Python you're using:
# YOUR CODE HERE
pythonVersion = sys.version
print("Python Version:", pythonVersion, "\n")



# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
processId = os.getpid()
print("Process ID:", processId, "\n")


# Print the current working directory (cwd):
# YOUR CODE HERE
curDirectory = os.getcwd()
print("Current Directory:", curDirectory, "\n")

# Print out your machine's login name
# YOUR CODE HERE
loginName = os.getlogin()
print("Login Name:", loginName, "\n")