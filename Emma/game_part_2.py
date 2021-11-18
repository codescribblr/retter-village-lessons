character_name = input("What's your character's name? ")

print(f'Welcome to the game, {character_name}')
base_color = input("What is the color of your base? (red, green, or blue) ")
skill = input("What is your skill (speed or strength?) ")
level = input("What difficulty level to start the game (1-10, 1 being easiest and 10 being hardest)? ")

base_hp = 10
hp = base_hp + int(level)

print(f"hello {character_name}. you have chosen the base color {base_color}. {skill} is a good choice. level {level} is fun. your hp is {hp}. ")
int_level = int(level)
# 1. How many squares will the board have?

base_squares = (int_level + 2)**2
# 2. How many monsters will be on the board? Bonus if you tell them how many are visible and invisible.
monsters = int(level) + 1
# 3. What team are they on, and which side of the board does that team start?
if base_color == 'red': 
    side = 'left'
elif base_color == 'blue':
    side = 'right'
elif base_color == 'green':
    side = 'bottom'
# 4. What is the starting HP of the player based on the level they chose?
print(f"you are back {character_name}. your base has {base_squares}. and you have chosen color {base_color}. you will start on the {side}. you will have {base_hp}hp. you have {monsters} monsters, scary." )
