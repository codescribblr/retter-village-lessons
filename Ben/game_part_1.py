
# use "python Ben/game_part_1.py" in the shell to run this file
current_score = 0
# try to use all lowercase for your variable names. We'll start using uppercase when we get to more advanced data types. But for simple strings and ints, let's stick with lowercase. (You can use unerscores _ to separate words in a variable name)
# Movement = 1
movement = 1 
# it's fine to use all caps for variable names, but the accepted way to use capital letters is for something called "constants". These are just variables that never change. So for instance, the base hp at the beginning of each level is 10. So maybe create a variable called BASE_HP and set it equal to 10. Then create another variable called hp that stores the player's actual HP.
BASE_HP = 10
name = input('What is your name? ')
print(f"Hi, {name}. Welcome to the game. The point of this game is to escape the dongeun without leting the monster find you!")
print("What skill do you chose?")
skill = input("Type Speedy, Strong? ")
# using .upper() is a great idea here. What that does is uppercase all the letters in the string no matter what the user entered. This will make it easier to compare later.

# since you uppercased their answer to the skill question, you'll need to compare it to the skills in all uppercase
# if skill == "Strong":
if skill == "Strong":
    # you haven't learned this yet. I was going to teach conditionals this week. But you need to indent everything under the if statement by 4 spaces. You can use the "Tab" key to get that in most places.
#   HP + 1
    
# You don't need the break statements here. Those are for breaking out of loops and we're not in a loop here.
# break
# if skill == "Speedy":
elif skill == "Speedy":
    movement += 1
#   Movement + 1
# else statements need to be on their own line.
else: 
    print('You did not chose an option. try again.')
# return is for functions. we haven't learned those yet, so no need to do that here.
# return skill
print(f"Hi, {name}, the {skill}. Now let's change your avatar")
top = input(f'What color do you want your shirt to be, {name}? Red Blue or Green? ')
bottom = input(f'What color do you want your pants to be? Red Blue or Green? ')
print(f"hmmmm {top} and {bottom}... good color combo!")
# ('HP + {final_HP} = overall_HP')
level = input('What level do you chose? 1-10? ')
final_hp = hp + int(overall_hp)
print(f"psst hey, {name} heres a hint. the exit is always on the top! See you next time!")
hp = BASE_HP + int(level)