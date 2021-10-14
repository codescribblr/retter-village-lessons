#####################################################
################ GAME EXPLANATION ###################
#####################################################

# Our game is going to be an "Escape from the monsters and find the exit" game. The board size and number of monsters will be determined by the difficulty level chosen at the beginning of the game. The player will start with 10 base health (HP). Each monster encountered will cost the player 2 HP. If the player chose speed, then each turn the player will get to move 2 spaces (basically 2 turns per turn). Otherwise the player will move 1 space each turn. If the player chose strength, then monsters will only deal 1 HP damage. Each level will give the player additional HP based on the level (Base HP + lvl). Score will be calculated by number of turns used and remaining HP. 

# At the beginning of the game the player will need to chose a player name, team color, skill, and difficulty level.

# The number of squares in the board will be ((x+2)**2) where x is the difficulty level. This means the difficulty level + 2 then mupltiply that number by itself. So, if the player chose level 1, there would be (1+2)**2 squares--or 3 x 3. So 9 squares. If the player chose level 10, then there would be 144 squares.

# The number of monsters in the board will be (x+1) where x is the difficulty level. This means if the player chose level 1, there will be 2 monsters to avoid. Half of the mosters will be visible. Half of them will be invisible (hidden from the player).

# The red base is on the left. The blue base is on the right. The green base is at the bottom. The exit is always at the top.

# Each new level, the player will spawn at a random start point along their team's base. The exit will spawn at a random point along the top of the board. The monsters will spawn at random squares throughout the board (but never in front of the player spawn or the exit spawn points).

# Each turn the player has, you'll need to ask them which direction to move. You'll need to tell them which options they have (up, down, left, right). If they are at the left side of the board, then you need to make sure "left" is not an option--since that's impossible. Make sure you handle incorrectly entered text by showing the user the error and giving them another chance to enter correctly. For instance, if they type "lft" instead of "left", you'll need to tell them that they entered an illegal value and they need to chose again.

# Final score will be (remaining HP * (level+5)**) - (number of turns used)
# So a player that finished on level 1 in 6 moves with 8 HP remaining would have a score of (8 * 36) - 6. Or 282.
# A player that finishes level 10 in 200 moves with 9 HP remaining would have a score of (9 * 225) - 200. Or 1825.

# At the end of each level, show the player their current score and how many levels they've completed. Then let them decide if they want to "continue?" or "quit?".

# If the player dies before getting to the exit, allow the player to choose "play again?" or "exit?". If they play again, restart the level. If they exit, give them their final score (all scores added together), and say goodbye.