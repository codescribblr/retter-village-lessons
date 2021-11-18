# use "python Jay/game_part_1.py" in the shell to run this file

# You need to use input() to ask the questions. Make sure you assign it to a variable to save the user's answer so you can give it back to them later.
# like this:
# name = input("What's your name?")
#print('Please enter your name for the game.')
#while(x==1) :
#name = input('What is your name? ')
#print(f"Hi, {name}. Welcome to the game.")
#x = 2
# print('Please enter your name for the game.')
# x = 1
# comparison operators are == > < <= >=
# while(x==1) :
# name = input('What is your name? ')
# print(f"Hi, {name}. Welcome to the game.")
# x = 2
#which_level= 1-10
# Looks like you started here. You copied a bunch of lines you don't need for this homework. I've commented out those lines and left just the one's you need.

# You need to ask 3 more questions and assign the inputs to variables. Then you need to print the final statement at the end with all 4 variables in it.


# 1. The name of their character
print('Please enter your name for the game.')
name = input('What is your name? ')
print(f"Hi, {name}. Welcome to the game.")
# 2. The color of their base (red, green, or blue)
base = input("what color is your base? ")
# 3. The character's skill (speed or strength)
skill = input("What skill does your dude have? Choose speed or strength. ")
# 4. The difficulty level to start the game (1-10, 1 being easiest and 10 being hardest)
level = input("What level do you wish to start on? 1-10 ")
hp = 10 + int(level)
print(f"Hi {name}. Your base is {base}. Your skill is {skill}. You are starting on level {level}. Your starting HP is {hp}.")