#!/usr/bin/env python

########################################################################
# Please DON'T edit the files in Lessons. There's no way to get the text back if you delete it. :(
########################################################################

# In programming, output is the concept of getting text to display on the user's screen. In order for the user to know what to do, you need to display some kind of text on their screen.

# To accomplish this, in python we use the print function.

print("hello, world.")

# you can print stings, integers, booleans, lists, sets, and dictionaries. Objects are more complex, so python can't print those directly.abs

print(125)

print(True)

print(['seed', 'flower pot', 'soil', 'water', 'sunlight', 'love'])

# Often when outputting text to the user, we'll need to have variables along with strings to give the user information. To do this, we can use string formatting. There are several different ways to format a string:

# F strings are strings that start with the letter "f". This tells python to parse the string and replace variables with their values

name = "Jon"
print(f"Hi. My name is {name}")

print("Hi. My name is {}".format(name))

print("Hi. My name is {your_name}".format(your_name=name))

