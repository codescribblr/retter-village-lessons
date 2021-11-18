# Homework Part 2 -- Due Date: 11/2/21

# To do this homework, you'll need to read and learn from Lessons/conditionals.py

# You'll also need to review Lessons/output.py, Lessons/operators.py, Lessons/booleans.py, and Lessons/variables.py

# This week's homework will expand on what you completed last time. To complete this assignment, you'll need to take the information that the player gave you and calculate the starting values for the game. You'll need to store these starting values in new variables. You can name these whatever you want. Just make them descriptive so that you know what they mean later.

# To call this assignment complete, You'll need to print out the following 4 pieces of information to the player:

# 1. How many squares will the board have?
# 2. How many monsters will be on the board? Bonus if you tell them how many are visible and invisible.
# 3. What team are they on, and which side of the board does that team start?
# 4. What is the starting HP of the player based on the level they chose?

# Bonus: Create variables for the total number of turns taken, moves per turn,  moves left in current turn, base damage of the monsters, and current_score.
# Take the skill that the player chose and calculate the value of their stat based on their chosen skill. If the player chose speed, then make sure they have 2 moves per turn and 2 moves left in the current turn. If the player chose strength, then make sure the monsters are set to deal 2 damage.

# Double Bonus: Create a stat board to display all of these values to the user after each turn.

# Put your final code in the "game_part_2.py" file. Make sure that when I run the file I get the questions and the final output in the console.

# Feel free to email me any questions you have (jonathanwadsworth@gmail.com), and I'll answer as soon as I can.
# use "python Ben/game_part_1.py" in the shell to run this file

# try to use all lowercase for your variable names. We'll start using uppercase when we get to more advanced data types. But for simple strings and ints, let's stick with lowercase. (You can use unerscores _ to separate words in a variable name)
# Movement = 1
#movement = 1 
# it's fine to use all caps for variable names, but the accepted way to use capital letters is for something called "constants". These are just variables that never change. So for instance, the base hp at the beginning of each level is 10. So maybe create a variable called BASE_HP and set it equal to 10. Then create another variable called hp that stores the player's actual HP.
#BASE_HP = 10
#hp = BASE_HP
#name = input('What is your name? ')
#print(f"Hi, {name}. Welcome to the game. The point of this game is to escape the dongeun without leting the monster find you!")
#print("What skill do you chose?")
#skill = input("Type Speedy, Strong? ").upper()
# using .upper() is a great idea here. What that does is uppercase all the letters in the string no matter what the user entered. This will make it easier to compare later.

# since you uppercased their answer to the skill question, you'll need to compare it to the skills in all uppercase
# if skill == "Strong":
#if skill == "STRONG":
    # you haven't learned this yet. I was going to teach conditionals this week. But you need to indent everything under the if statement by 4 spaces. You can use the "Tab" key to get that in most places.
#   HP + 1
 #   hp += 1
    
# You don't need the break statements here. Those are for breaking out of loops and we're not in a loop here.
# break
# if skill == "Speedy":
#elif skill == "SPEEDY":
    # another way to add to a variable is to add it to itself. So if you want to add to movement, you can do:
    # Movement = Movement + 1
    # or even shorter
    # Movement += 1
 #   movement += 1
#   Movement + 1
# else statements need to be on their own line.
#else: 
 #   print('You did not chose an option. try again.')
# return is for functions. we haven't learned those yet, so no need to do that here.
# return skill
#print(f"Hi, {name}, the {skill}. Now let's change your avatar")
#top = input(f'What color do you want your shirt to be, {name}? Red Blue or Green? ')
#bottom = input(f'What color do you want your pants to be? Red Blue or Green? ')
#print(f"okay {top} and {bottom}... you could have done better!")
# ('HP + {final_HP} = overall_HP')
#level = input('What difficulty level do you chose? 1-10? ')
#final_hp = hp + int(hp)
#print(f"psst hey, {name} heres a hint. the exit is always on the top! See you next time!")
#int_level = int(level)
#hp = BASE_HP + int_level
# Nice. I like all the creativity here. I'll went through and made comments to help you where things went wrong. Overall, great job!

# 1. How many squares will the board have?
#board_squares = ((int_level+2)**2)
# 2. How many monsters will be on the board? Bonus if you tell them how many are visible and invisible.
#total_monsters = int_level + 1
# 3. What team are they on, and which side of the board does that team start?
#team = top
#starting_side = 'right'
#if team == 'green':
 #   starting_side = 'bottom'
#elif team == 'red':
 #   starting_side = 'left'
#else:
 #   starting_side = 'right'

# 4. What is the starting HP of the player based on the level they chose?
#hp = hp

#print(f"Your board has {board_squares} squares. The {team} team starts on the {starting_side} side. There are {total_monsters} monsters to avoid. Your starting HP is {hp}.") 
# 2. How many monsters will be on the board? Bonus if you tell them how many are visible and invisible.
# Bonus: Create variables for the total number of turns taken, moves per turn,  moves left in current turn, base damage of the monsters, and current_score.
# board_squares = []