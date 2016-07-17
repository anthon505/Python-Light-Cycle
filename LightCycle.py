#Program Name: LightCycle
#Name: Anthony Ngoy
#Description: Light Cycle is a 2 player game similar to snake, but players must avoid walls
#             and the light trail lefts behind by the cycles to win
#Date: January 22,2016

import pygame, sys, time
from pygame.locals import *
fpsClock = pygame.time.Clock()

pygame.init()                               #Initializing font

w = 1250                                    #width
h = 700                                     #height

P1_Wins = 0                                 #Score of Player 1
P2_Wins = 0                                 #Score of Player 2

wso = pygame.display.set_mode((w, h))       #Setting the dimensions of the window
pygame.display.set_caption("Light Cycle")   #text of display window

cycle = [[w*0.9, h / 2]]                    #Starting location of Player 1
keys = (K_UP, K_DOWN, K_RIGHT, K_LEFT)      #Movement keys for Player 1
         
cycle2 = [[w*0.1, h / 2]]                   #Starting location of Player 2
keys_cycle2 = (K_w, K_s, K_d, K_a)          #Movement keys for Player 2

#The colour scheme using colour codes from Tron 
colourOrange = pygame.Color(223,116,12)
colourCyan = pygame.Color(111,195,223)
colourBlack = pygame.Color(12, 20, 31)
colourWhite = pygame.Color (233,255,255)

step = -2.5                                 #Direction and speed 
cycle_dir = [step, 0]
cycle2_dir = [-step, 0]


#Function name: drawBox
#Parameters: wso is window dimensions; x is x coordinate of cycle; y is y coordinate;
#            s is size; c is colour
#Description: Takes in the parameters and creates the cycle visual 
def drawBox (wso, x, y, s, c):
    pygame.draw.rect(wso, c, (x, y, s, s))


#Function name: move_cycle
#Parameters: cycle_dir is cycle location; move_cycle is Movement keys for cycle
#Description: Takes in the parameters and determines the movement and direction for the cycle,
def move_cycle(cycle_dir, keys):            
    if cycle_dir[1] == 0:                       #Checks if the cycle is moving horizontally
        if (event.key == keys[0]):              #Movement up key
            cycle_dir[1] = step
            cycle_dir[0] = 0
        elif (event.key == keys[1]):            #Movement down key
            cycle_dir[1] = -1 * step
            cycle_dir[0] = 0
    if cycle_dir[0] == 0:                       #Checks if the cycle is moving vertically
        if (event.key == keys[2]):              #Movement right key
            cycle_dir[0] = -1 * step 
            cycle_dir[1] = 0
        elif (event.key == keys[3]):            #Movement left key
            cycle_dir[0] = step
            cycle_dir[1] = 0

    return cycle_dir

#Function name: self_collision
#Parameters: cycle is the coordinates of the cycle; cycle_dir is the direction of the cycle
#Description: Checks if cycle has collided with itself, determining if new coordinates of cycle
#             is the same as previous coordinates of the cycle
def self_collision(cycle, cycle_dir):
    new_x = cycle[-1][0] + cycle_dir[0]
    new_y = cycle[-1][1] + cycle_dir[1]

    for i in range(len(cycle)):
        if cycle[i][0] == new_x and cycle[i][1] == new_y:   #Checks if previous locations of cycles correspond with new locations
            return True
    return False

#Function name: wall_collision
#Parameters: cycle is the coordinates of the cycle
#Description: Checks if the cycle passes the boundaries of the window 
def wall_collision(cycle):
    if cycle[-1][0] >= w - step:    #Checks right boundary
        return True 
    elif cycle[-1][0] < step:       #Checks left boundary
        return True
    elif cycle[-1][1] >= h - step:  #Checks bottom boundary
        return True
    elif cycle[-1][1] < step:       #Checks top boundary
        return True

#Function name: cycle_collision
#Parameters: cycle1 is the coordinates of the first cycle, cycle 2 is the coordinates for the
#            second cycle. cycle_dir is the direction 
#Description: Checks if the cycles collide with each other
def cycle_collision(cycle1, cycle2, cycle_dir):
    new_x = cycle1[-1][0] + cycle_dir[0]
    new_y = cycle1[-1][1] + cycle_dir[1]
    
    for i in range(len(cycle2)):
        if cycle2[i][0] == new_x and cycle2[i][1] == new_y:     #Checks if there is collision by comparing coordinates
            return True
    return False

#Function name: extend_cycle
#Parameters: cycle is cycle coordinates; cycle_dir is the direction of the cycle
#Description: It extends the cycle every time the screen updates
def extend_cycle(cycle, cycle_dir):
    cycle.append([cycle[-1][0] + cycle_dir[0], cycle[-1][1] + cycle_dir[1]])

#Function name: text
#Parameters: message is the text that will be displayed; centerx is the center x coordinate of text
#            centery is the center y coordinate of the text; s is font size; c is colour
#Description: Takes in the parameters and displays the text 
def text(message, centerx, centery,s,c):
    font = pygame.font.SysFont("ubuntu", s)     #Takes in font type and size
    text = font.render(message, 1, c)           #Creates message
    textpos = text.get_rect(centerx=centerx, centery=centery)   #Determines the position of the text
    wso.blit(text, textpos)                     #Displays the text 

wso.fill(colourBlack)

text("Light Cycle", w/2,150, 150, colourWhite)      #Title

text("Press Space to Start Game", w/2, h/2, 50, colourWhite)    #Instructions on what to do next
text("Press ESC to quit", w / 2, h/2 + 50, 35, colourWhite) 

#The following is the text for the controls for both player
text("Player 2 Controls:", w / 5, h/2 + 100, 45, colourCyan), text("Player 1 Controls:", w / 5 * 4, h/2 + 100, 45, colourOrange)  
text("Up = W Key", w / 5 + 7, h/2 + 130, 35, colourCyan) , text("Up = Up Arrow Key", w / 5 * 4, h/2 + 130, 35, colourOrange)
text("Down = S Key", w / 5 - 13, h/2 + 160, 35, colourCyan) ,text("Down = Down Arrow Key", w / 5 * 4, h/2 + 160, 35, colourOrange)
text("Left = A Key", w / 5 - 1, h/2 + 190, 35, colourCyan) ,text("Left = Left Arrow Key", w / 5 * 4, h/2 + 190, 35, colourOrange)
text("Right = D Key", w / 5 - 8, h/2 + 220, 35, colourCyan) ,text("Right = Right Arrow Key", w / 5 * 4, h/2 + 220, 35, colourOrange)

#The following is the text for how to play
text("How To Play:", w/2, h/2 + 150, 45, colourWhite)
text("Avoid The Walls", w/2, h/2 + 180, 35, colourWhite)
text("Avoid The Light Paths", w/2, h/2 + 210, 35, colourWhite)
text("Stay Alive Longest", w/2, h/2 + 240, 35, colourWhite)
text("Have Fun!", w/2, h/2 + 270, 35, colourWhite)

done = False
start_game = False
game_over = False

#Loop that will run while done is False
while not done:
    for event in pygame.event.get():
        if (event.type == KEYDOWN):
            if event.key == K_SPACE and game_over:      #If Space is pressed in game over screen, game restarts
                cycle = [[w*0.9, h / 2]]                #Resetting the location of the cycle
                cycle2 = [[w*0.1, h / 2]]
                cycle_dir = [step, 0]
                cycle2_dir = [-step, 0]
                start_game = True
                wso.fill(colourBlack)
                game_over = False
            elif event.key == K_ESCAPE:     #If ESC key is pressed in game over screen, game quits
                wso.fill(colourBlack)
                text("Light Cycle", w/2,150, 150, colourWhite)
                text("Thanks For Playing!",w/2,h/2, 50, colourWhite)
                pygame.display.update()                 #Update display to show exit screen
                done = True
    while not game_over:                                #Loop that will run when not on the game over screen
        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):             #If ESC key is pressed during the game, or intro screen, the game quits, showing exit screen
                    done = True
                    game_over = True
                    start_game = False
                    wso.fill(colourBlack)
                    text("Light Cycle", w/2,150, 150, colourWhite)
                    text("Thanks For Playing!",w/2,h/2, 50, colourWhite)
                elif event.key == K_SPACE and not start_game:     #If Space bar is pressed during intro screen, the game starts
                    wso.fill(colourBlack)
                    start_game = True
                    
                cycle_dir = move_cycle(cycle_dir, keys)             #Movement and direction of Player 1
                cycle2_dir = move_cycle(cycle2_dir, keys_cycle2)    #Movement and direction of Player 2

        if start_game:
            #Check if cycles loses by calling the functions and returning True or False
            cycleLose = self_collision(cycle, cycle_dir) or wall_collision(cycle) or cycle_collision(cycle, cycle2, cycle_dir)
            cycle2Lose = self_collision(cycle2, cycle2_dir) or wall_collision(cycle2) or cycle_collision(cycle2, cycle, cycle2_dir)
            game_over = cycleLose or cycle2Lose
            if not cycleLose and not cycle2Lose:    #If no one loses, game continues
                extend_cycle(cycle, cycle_dir)
                extend_cycle(cycle2, cycle2_dir)
                drawBox (wso, cycle[-1][0], cycle[-1][1], 4, colourOrange)
                drawBox (wso, cycle2[-1][0], cycle2[-1][1], 4, colourCyan)
            elif cycleLose and cycle2Lose:          #If both cycles loses, game over and tie game
                wso.fill(colourBlack)
                text("A Tie!", w / 2, h/2 - 115, 50, colourWhite)
            elif cycleLose:                         #If Player 1 loses, game over and Player 2 wins
                wso.fill(colourBlack)
                P2_Wins += 1
                text("Player 2 Wins!", w/ 2, h/2 - 115, 50, colourCyan)
            else:                                   #If Player 2 loses, game over and Player 1 wins
                wso.fill(colourBlack)
                P1_Wins += 1
                text("Player 1 Wins!", w / 2, h/2 - 115, 50, colourOrange)
            if game_over:                           #Gameover screen
                text("Light Cycle", w/2, 150, 150, colourWhite)
                text("Player 1 Wins: " + str(P1_Wins), w / 2, h/2 + 250, 35, colourOrange)
                text("Player 2 Wins: " + str(P2_Wins), w / 2, h/2 + 300, 35, colourCyan)               
                text("Restart?", w / 2, h/2, 50, colourWhite)
                text("Press Space to play again", w / 2, h/2 + 50, 45, colourWhite)
                text("Press ESC to quit", w / 2, h/2 + 100, 35, colourWhite)

        # window is not drawn until the update command is called
        pygame.display.update()
        fpsClock.tick(75)
        
time.sleep(1) 
sys.exit(0)