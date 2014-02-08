# STRONGHOLD OF THE DWARVEN LORDS v2.1 
# Martin Hodgson - November 2013 
# Translated from Tim Hartnell's original BASIC version... 
# ...with a couple of updates. Now you can't walk through walls! 
  
import random 
  
# VARIABLES, LISTS 
data1 = [2,2,2,3,2,4,2,5,2,6,2,7] 
data2 = [3,7,4,7,5,7,5,6,5,5,5,4,5,3,6,3] 
data3 = [7,3,7,4,7,5,7,6,7,7,7,8,7,9,9,8] 
data4 = [9,9,10,8,10,7,10,6,10,5,10,4,8,8] 
data5 = [10,3,11,3,12,3,13,3,14,3,14,2,7,10] 
data6 = [6,10,5,10,4,10,3,10,2,10,2,11,2,12] 
data7 = [2,13,2,14,6,11,6,12,6,13,6,14,7,12] 
data8 = [14,12,8,12,8,14,9,12,9,13,9,14,10,12] 
data9 = [11,9,11,10,11,11,11,12,12,9,13,9,13,10] 
data10 = [13,11,13,12,13,13,13,14,14,14] 
data = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 
  
# FUNCTIONS 
def new_game(): # GOSUB 640 in original BASIC version 
    global a, b, z, y, x, s, m, a, e, d 
    print ("================================================================\n") 
    input ("STRONGHOLD OF THE DWARVEN LORDS\nNew Game - Press Enter...") 
    # Item zero and the zero at the beginning of each sub-list will be ignored... 
    # ... as the BASIC program uses indices 1-15 
    a = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]] 
    b = random.randint(1, 3) 
    z, y = 14, 14
    if b == 2: 
        y = 2
    if b == 3: 
        z = 2
    x, s = 1, 2
    for b in (range(1, 16)): 
        for c in (range(1, 16)): 
            a[b].append(x) 
            if random.randint(1, 10) > 8: 
                a[b][c] = s 
            if c<2 or c>14 or b<2 or b>14: 
                a[b][c] = x 
    d, e = 2, 2
    for f in (range(0, 136, 2)): 
        b = data[f] 
        c = data[f+1] 
        a[b][c] = s 
    a[z][y] = s # Makes sure the gold isn't in a wall 
    m = -15
    return
  
def show_map(): # GOSUB 480 'help' in original BASIC version 
    global b, m 
    print ("\n================================================================\n") 
    print ("North") 
    b = 15
    while b > 0: 
        strng = "" 
        for c in (range(1, 16)): 
            if a[b][c] == x: 
                strng += ("#") 
            elif b == d and c == e: 
                strng += "*"
            elif a[b][c] == s: 
                strng += " "
        print (strng) 
        b -= 1
    print ("South") 
    m += 15
    a[d][e] = s 
    # Here I've omitted two lines from the BASIC version: 
    # 600 FOR J = 1 TO 2000:NEXT J - Makes the prgram pause. 
    # 610 CLS - Clear screen. Not possible in Python Shell? 
  
def move(): # Lines 50 to 410 - Main game script from BASIC version 
    global m, d, e 
    m += 1
    print ("\n================================================================\n") 
    print ("STEP NUMBER", m) 
    if a[d+1][e] == s: 
        print ("NORTH: OPEN") 
    elif a[d+1][e] == x: 
        print("NORTH: WALL") 
    if a[d-1][e] == s: 
        print ("SOUTH: OPEN") 
    elif a[d-1][e] == x: 
        print("SOUTH: WALL") 
    if a[d][e+1] == s: 
        print ("EAST: OPEN") 
    elif a[d][e+1] == x: 
        print("EAST: WALL") 
    if a[d][e-1] == s: 
        print ("WEST: OPEN") 
    elif a[d][e-1] == x: 
        print("WEST: WALL") 
    print ("THE DWARVEN SOURCE BEAM READS:", (100 * abs(z-d) + 10 * abs(y-e))) 
    print ("Which direction do you want to move...") 
    a_string = input ("N - north, S - south, E - east, W - west, H - help ? ") 
    if a_string == "H": 
        show_map() 
    elif a_string == "N": 
        d += 1
    elif a_string == "S": 
        d -= 1
    elif a_string == "E": 
        e += 1
    elif a_string == "W": 
        e -= 1
    if z == d and y == e: 
        win() 
    if a[d][e] == x: # In the original you could walk through walls... Now you can't!
        print("\nOuch! You just walked into a wall...") 
        if a_string == "N": 
            d -= 1
        elif a_string == "S": 
            d += 1
        elif a_string == "E": 
            e -= 1
        elif a_string == "W": 
            e += 1 
    move() 
  
def win(): 
    print ("\nYou found the Dwarven riches in just", m, "steps!\n") 
    show_map() 
    # This feature has been added - The original version would just END. 
    new_game() 
    show_map() 
    move() 
  
# MAIN PROGRAM 
new_game() 
show_map() 
move()
