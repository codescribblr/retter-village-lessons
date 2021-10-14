#####################################################
################ GAME EXPLANATION ###################
#####################################################

# Our game is going to be an "Escape from the monsters and find the exit" game. The board size and number of monsters will be determined by the difficulty level chosen at the beginning of the game. The player will start with 10 health (HP). Each monster encountered will cost the player 2 HP. If the player chose speed, then each turn the player will get to move 2 spaces (basically 2 turns per turn). Otherwise the player will move 1 space each turn. If the player chose strength, then monsters will only deal 1 HP damage. 

# At the beginning of the game the player will need to chose a player name, team color, skill, and difficulty level.

# The number of squares in the board will be ((x+2)**2) where x is the difficulty level. This means the difficulty level + 2 then mupltiply that number by itself. So, if the player chose level 1, there would be (1+2)**2 squares--or 3 x 3. So 9 squares. If the player chose level 10, then there would be 144 squares.

# The number of monsters in the board will be (x+1) where x is the difficulty level. This means if the player chose level 1, there will be 2 monsters to avoid. Half of the mosters will be visible. Half of them will be invisible (hidden from the player).

# The red base is on the left. The blue base is on the right. The green base is at the bottom. The exit is always at the top.

# Each new level, the player will spawn at a random start point along their team's base. The exit will spawn at a random point along the top of the board. The monsters will spawn at random squares throughout the board (but never in front of the player spawn or the exit spawn points).