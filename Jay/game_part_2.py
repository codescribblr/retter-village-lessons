character_name = input("What's your character's name? ")

print(f'Welcome to the game, {character_name}')
base_color = input("What is the color of your base? (red, green, or blue) ")
skill = input("What is your skill (speed or strength?) ")
level = input("What difficulty level to start the game (1-10, 1 being easiest and 10 being hardest)? ")

base_hp = 10
hp = base_hp + int(level)

print(f"hello {character_name}. you have chosen the base color {base_color} which is not what i would choose. {skill} is a bad choice. level {level} is easy. your hp is {hp}. ")

# 1. How many squares will the board have?

base_squares = (int(level) + 2)**2
# 2. How many monsters will be on the board? Bonus if you tell them how many are visible and invisible.
monsters = int(level) + 1
# 3. What team are they on, and which side of the board does that team start?
if base_color == 'purple': 
    side = 'left'
elif base_color == 'gray':
    side = 'right'
elif base_color == 'orange':
    side = 'bottom'
# 4. What is the starting HP of the player based on the level they chose?
print(f"you are back {character_name}. your base has {base_squares}. and you have chosen color {base_color}. you will start on the {side}. you will have {base_hp}hp. you have {monsters} monsters." )
# 2. How many monsters will be on the board? Bonus if you tell them how many are visible and invisible.
# Bonus: Create variables for the total number of turns taken, moves per turn,  moves left in current turn, base damage of the monsters, and current_score.
visible_monsters = (int(level)+1)**2
invisible_monsters = (int(level)+1)**2
current_score = (int(monsters)+2)**3
turns_taken = (int([])+0)**1
moves_per_tern = int(1)
if skill == 'speed':
    moves_left = int(1)
    monster_damage=(int(level)+2)
