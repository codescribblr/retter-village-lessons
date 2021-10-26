########################################################################
# Please DON'T edit the files in Lessons. There's no way to get the text back if you delete it. :(
########################################################################

# To collect data from the user, we use the input() function. This allows us to ask questions like "what's you name?" or "how many spaces would you like your rook to move left?". 

input("What's the name of your favorite superhero?")

# We can store this data in a variable for use later.

character_name = input("What's your character's name?")

print(f'Welcome to the game, {character_name}')

# You can use multiple input statements to collect more information.

name = input("Hi! What is your name? ")
print(f"Hello, {name}. Welcome to Pastorelli's Pizza and Pasta.")
entre = input("What would you like for dinner? ")
drink = input("What would you like to drink? ")
dessert = input("And for dessert? ")

print(f"OK. So you'd like {entre} for dinner, {drink} to drink, and {dessert} for dessert.")

confirm = input("Is that correct?")