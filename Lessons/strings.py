########################################################################
# Please DON'T edit the files in Lessons. There's no way to get the text back if you delete it. :(
########################################################################

# Strings are sequences of character data. The string type in Python is called str.

# String literals may be delimited using either single or double quotes. All the characters between the opening delimiter and matching closing delimiter are part of the string:

# >>> print("I am a string.")
# I am a string.
# >>> type("I am a string.")
# <class 'str'>

# >>> print('I am too.')
# I am too.
# >>> type('I am too.')
# <class 'str'>

# You cannot mix single and double quotes.

# This won't work:
print('Hi everyone")

# A string in Python can contain as many characters as you wish. The only limit is your machine’s memory resources. A string can also be empty:

print('')

# What if you want to include a quote character as part of the string itself? Your first impulse might be to try something like this:

print('This string contains a single quote (') character.')

# As you can see, that doesn’t work so well. The string in this example opens with a single quote, so Python assumes the next single quote, the one in parentheses which was intended to be part of the string, is the closing delimiter. The final single quote is then a stray and causes the syntax error shown.

# If you want to include either type of quote character within the string, the simplest way is to delimit the string with the other type. If a string is to contain a single quote, delimit it with double quotes and vice versa:

print("This string contains a single quote (') character.")
# This string contains a single quote (') character.

print('This string contains a double quote (") character.')
# This string contains a double quote (") character.

# If you want to include a single quote in a string that is enclosed by single quotes you need to use something called "escaping". To escape a character, you put a backslash before it. This allows the python interpreter to treat that character as just a normal character instead of the special meaning that it might otherwise have.

print('This string contains a single quote (\') character.')
