# use "python Emma/game_part_1.py" in the shell to run this file

# You haven't done anything! Get to work!!! ;)

character_name = input("What's your character's name? ")

print(f'Welcome to the game, {character_name}')
base_color = input("What is the color of your base? (red, green, or blue) ")
skill = input("What is your skill (speed or strength?) ")
level = input("What difficulty level to start the game (1-10, 1 being easiest and 10 being hardest)? ")

base_hp = 10
hp = base_hp + int(level)

print(f"hello {character_name}. you have chosen the base color {base_color}. {skill} is a good choice. level {level} is fun. your hp is {hp}. ")