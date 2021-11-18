# use "python Ben/game_part_2.py" in the shell to run this file


movement = 1 
BASE_HP = 10
hp = BASE_HP
name = input('What is your name? ')
print(f"Hi, {name}. Welcome to the game. The point of this game is to escape the dungeon without leting the monster find you!")
print("What skill do you chose?")
skill = input("Type Speedy, Strong? ").upper()


# since you uppercased their answer to the skill question, you'll need to compare it to the skills in all uppercase
# if skill == "Strong":
if skill == "STRONG":
    # you haven't learned this yet. I was going to teach conditionals this week. But you need to indent everything under the if statement by 4 spaces. You can use the "Tab" key to get that in most places.
#   HP + 1
    hp += 1
    
# You don't need the break statements here. Those are for breaking out of loops and we're not in a loop here.
# break
# if skill == "Speedy":
elif skill == "Speedy":
    # another way to add to a variable is to add it to itself. So if you want to add to movement, you can do:
    # Movement = Movement + 1
    # or even shorter
    # Movement += 1
    movement += 1
#   Movement + 1
# else statements need to be on their own line.
else: 
    print('You did not chose an option. try again.')
# return is for functions. we haven't learned those yet, so no need to do that here.
# return skill
print(f"Hi, {name}, the {skill}. Now let's change your avatar")
top = input(f'What color do you want your shirt to be, {name}? Red Blue or Green? ').upper()
bottom = input(f'What color do you want your pants to be? Red Blue or Green? ')
print(f"hmmmm {top} and {bottom}... good color combo!")
# ('HP + {final_HP} = overall_HP')
level = input('What level do you chose? 1-10? ')
final_hp = hp + int(hp)
print(f"psst hey, {name} here's a hint. the exit is always on the top! See you next time!")
int_level = int(level)
hp = BASE_HP + int_level
# Nice. I like all the creativity here. I went through and made comments to help you where things went wrong. Overall, great job!

# 1. How many squares will the board have?
board_squares = ((int_level+2)**2)
# 2. How many monsters will be on the board? Bonus if you tell them how many are visible and invisible.
total_monsters = int_level + 1
# 3. What team are they on, and which side of the board does that team start?
team = top
starting_side = 'right'
if team == 'GREEN':
    starting_side = 'bottom'
elif team == 'RED':
    starting_side = 'left'
else:
    starting_side = 'right'

# 4. What is the starting HP of the player based on the level they chose?
hp = hp

print(f"Your board has {board_squares} squares. The {team} team starts on the {starting_side} side. There are {total_monsters} monsters to avoid. There is {total_monsters_visible} monster visible and the rest are not visible. Your starting HP is {hp}.")

print(f"Your score will go up by one if you dont run into any monsters. Your score will go back down to zero everytime you die. if you take damage then your score will go down by how much damage you took.")

#  Bonus: Create variables for the total number of turns taken, moves per turn,  moves left in current turn, base damage of the monsters, and current_score.
# Take the skill that the player chose and calculate the value of their stat based on their chosen skill. If the player chose speed, then make sure they have 2 moves per turn and 2 moves left in the current turn. If the player chose strength, then make sure the monsters are set to deal 2 damage.
current_score = 0
# Double Bonus: Create a stat board to display all of these values to the user after each turn.