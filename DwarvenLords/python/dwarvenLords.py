"""STRONGHOLD OF THE DWARVEN LORDS v2.2
Martin Hodgson - November 2013
Translated from Tim Hartnell's original BASIC version...
...with a couple of updates. Now you can't walk through walls!
"""

import random

OPEN = 2
WALL = 1

# VARIABLES, LISTS
data = [2,2,2,3,2,4,2,5,2,6,2,7,
        3,7,4,7,5,7,5,6,5,5,5,4,5,3,6,3,
        7,3,7,4,7,5,7,6,7,7,7,8,7,9,9,8,
        9,9,10,8,10,7,10,6,10,5,10,4,8,8,
        10,3,11,3,12,3,13,3,14,3,14,2,7,10,
        6,10,5,10,4,10,3,10,2,10,2,11,2,12,
        2,13,2,14,6,11,6,12,6,13,6,14,7,12,
        14,12,8,12,8,14,9,12,9,13,9,14,10,12,
        11,9,11,10,11,11,11,12,12,9,13,9,13,10,
        13,11,13,12,13,13,13,14,14,14]
# world is in reverse row major
# That is, consecutive elements of the row are stored together
# But each row is south of (below) the row after it
world = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
goldY, goldX = 14, 14
playerY, playerX = 2, 2
stepCount = -15
showGold = False

# FUNCTIONS
def new_game(): # GOSUB 640 in original BASIC version
    global world, goldY, goldX, playerY, playerX, stepCount
    print("================================================================\n")
    input("STRONGHOLD OF THE DWARVEN LORDS\nNew Game - Press Enter...")
    # Item zero and the zero at the beginning of each sub-list will be ignored...
    # ... as the BASIC program uses indices 1-15
    world = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
    b = random.randint(1, 3)
    goldY, goldX = 14, 14
    if b == 2:
        goldX = 2
    if b == 3:
        goldY = 2
    for b in range(1, 16):
        for c in range(1, 16):
            world[b].append(WALL)
            if random.randint(1, 10) > 8:
                world[b][c] = OPEN
            if (c < 2) or (c > 14) or (b < 2) or (b > 14):
                world[b][c] = WALL
    playerY, playerX = 2, 2
    for f in range(0, 136, 2):
        b = data[f]
        c = data[f+1]
        world[b][c] = OPEN
    world[goldY][goldX] = OPEN # Makes sure the gold isn't in a wall
    stepCount = -15

def show_map(): # GOSUB 480 'help' in original BASIC version
    global stepCount
    print("\n================================================================\n")
    print("North")
    for b in range(15, 0, -1):
        strng = []
        for c in range(1, 16):
            if world[b][c] == WALL:
                strng.append("#")
            elif (b == goldY) and (c == goldX) and showGold:
                strng.append("$")
            elif (b == playerY) and (c == playerX):
                strng.append("*")
            elif world[b][c] == OPEN:
                strng.append(" ")
        print(''.join(strng))
    print("South")
    stepCount += 15
    world[playerY][playerX] = OPEN
    # Here I've omitted two lines from the BASIC version:
    # 600 FOR J = 1 TO 2000:NEXT J - Makes the prgram pause.
    # 610 CLS - Clear screen. Not possible in Python Shell?

def move(): # Lines 50 to 410 - Main game script from BASIC version
    global playerY, playerX, stepCount
    stepCount += 1
    print("\n================================================================\n")
    print("STEP NUMBER", stepCount)
    if world[playerY+1][playerX] == OPEN:
        print("NORTH: OPEN")
    elif world[playerY+1][playerX] == WALL:
        print("NORTH: WALL")
    if world[playerY-1][playerX] == OPEN:
        print("SOUTH: OPEN")
    elif world[playerY-1][playerX] == WALL:
        print("SOUTH: WALL")
    if world[playerY][playerX+1] == OPEN:
        print("EAST: OPEN")
    elif world[playerY][playerX+1] == WALL:
        print("EAST: WALL")
    if world[playerY][playerX-1] == OPEN:
        print("WEST: OPEN")
    elif world[playerY][playerX-1] == WALL:
        print("WEST: WALL")
    # Dwarven source beam is Manhattan distance from player to gold
    print("THE DWARVEN SOURCE BEAM READS:", (100 * abs(goldY - playerY)) + (10 * abs(goldX - playerX)))
    print("Which direction do you want to move...")
    a_string = input("N - north, S - south, E - east, W - west, H - help, Q - quit ? ")
    a_string = a_string.upper() #Allow lowercase input too
    if a_string.startswith("H"):
        show_map()
    elif a_string.startswith("Q"):
        return True
    elif a_string.startswith(("N", "U")):
        playerY += 1
    elif a_string.startswith(("S", "D")):
        playerY -= 1
    elif a_string.startswith(("E", "R")):
        playerX += 1
    elif a_string.startswith(("W", "L")):
        playerX -= 1
    else:
        print("\nPardon? I don't understand...") # Inform the player if command is not recogised
    if (goldY == playerY) and (goldX == playerX):
        win()
    if world[playerY][playerX] == WALL: # In the original you could walk through walls... Now you can't!
        print("\nOuch! You just walked into a wall...")
        if a_string.startswith(("N", "U")):
            playerY -= 1
        elif a_string.startswith(("S", "D")):
            playerY += 1
        elif a_string.startswith(("E", "R")):
            playerX -= 1
        elif a_string.startswith(("W", "L")):
            playerX += 1
    return False

def win():
    print("\nYou found the Dwarven riches in just", stepCount, "steps!\n")
    show_map()
    # This feature has been added - The original version would just END.
    new_game()
    show_map()

# MAIN PROGRAM
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-g', '--gold', action='store_true',
                        help='show the gold on the map')
    args = parser.parse_args()

    showGold = args.gold

    new_game()
    show_map()
    while True:
        if move():
            break
