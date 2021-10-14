########################################################################
# Please DON'T edit the files in Lessons. There's no way to get the text back if you delete it. :(
########################################################################

# Integers are numbers.

print(6)

# You can perform math on integers.

print(5+5)
print(10*428)

# strings that are numbers are NOT integers

print(5 + "10") # does not work

print("5" + "10") # does not do what you think it will...

# so be careful to make sure the type of data is correct before you try to do math with it. You can convert a string to an integer before you do math on it.

print( int("5") + 10 )

# It's important to note that integers are whole numbers (positive or negative). Numbers that have a decimal point are not integers. They are called "Floats".

type(5.4)

# You can still do math on floats (called floating point numbes), but it's technically a different data type. It's not important now, but later, when you want to store data in a database, you'll need to know the exact data type that is stored in the database in order to store it correctly.

# You can always find out what type of data something is by using the type() function.

type(5)
type("five")
type(['five'])
type(('five',))