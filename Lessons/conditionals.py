########################################################################
# Please DON'T edit the files in Lessons. There's no way to get the text back if you delete it. :(
########################################################################

# The most basic logical construct in programming is the if/then statement. Basically, if something is true, then do this. In python, if statements end with a colon ":" before the then statement.

apples_picked = 0
apples = 'green'

if apples == 'green':
    # Then do something
    apples_picked = 10

# Since in python white space is important, we need to make sure that anything under the if statement is indented with 4 spaces. It technically works to indent the next line less than 4 spaces as long as all the following lines are intented the same amount. However, there is a standard in python that every python programmer should follow that says to use 4 spaces to indent.

# This will work, but is NOT the correct way to do it
if apples == 'red':
  apples_picked = 12

# Notice that when I write the condition (if something is true), I use the comparison operators that we discussed earlier. == >= <= < >
# So we can ask any question that would answer the question "Is this true?".

if apples_picked > 5:
    # stop picking apples
    exit()

# Be careful not to use the assignment operator to check for equality. This will not work:

# if apples = 'green':

# What do we do if we want to handle the condition if it is NOT true?
if not apples == 'green':
    apples = 'green'

# or
if apples != 'green':
    apples = 'green'

# Either one of these will work. Which one you decide to use is up to you. Choose the one that you think makes your code more readable.

# So then, what happens if you want to do something if the condition is true and something different if the condition is false?

# You could do this:

if apples == 'green':
    apples_picked = 10

if apples != 'green':
    apples_picked = 5

# But there's actually a better way to do this. It's called an "else" clause.

if apples == 'green':
    apples_picked = 10
else:
    apples_picked = 5

# Why do you think this would be better?

# What if you need to test for multiple conditions? Like if you need to find out if the apples are one of 4 different colors? To do this, we use an elif statement.

if apples == 'green':
    apples_picked = 10
elif apples == 'red':
    apples_picked = 5
elif apples == 'yellow':
    apples_picked = 2
else:
    apples_picked = 1

# You don't need to have only 3 conditions to use elif. You could have a list of 20 things you needed to check.



