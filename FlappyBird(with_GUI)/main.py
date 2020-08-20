import pygame,sys
import random

# Initialising the modules in pygame
pygame.init()
pygame.font.init()
pygame.display.init()

SCREEN = pygame.display.set_mode((500,750)) #Setting the display

#background
BACKGROUND_IMAGE=pygame.image.load('flappybg.jpg')

#BIRD
BIRD_IMAGE = pygame.image.load('bird2.png')
bird_x = 50
bird_y = 300
bird_y_change = 0

def display_bird(x,y):
    SCREEN.blit(BIRD_IMAGE, (x,y))

# OBSTACLES
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150,450) #obstacle height only for the first iteration
OBSTACLE_COLOR = (211, 253, 117)
OBSTACLE_X_CHANGE = -4
obstacle_x = 500

def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_obstacle_height = 601 - height - 150
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 601, OBSTACLE_WIDTH, -bottom_obstacle_height))

#COLLISION DETECTION
def collision_detection(obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <=(50+80):
        if bird_y <= obstacle_height or bird_y >= (bottom_obstacle_height - 80):
            return True
    return False

#SCORE
score = 0
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)

def score_display(score):
    display = SCORE_FONT.render(f"Score: {score}", True, (255,255,255))
    SCREEN.blit(display, (10,10))

#START SCREEN
startFont = pygame.font.Font('freesansbold.ttf', 32)
def start():
    #displays: message
    display = startFont.render(f"PRESS SPACE BAR TO START", True, (255, 255, 255))
    SCREEN.blit(display, (20, 200))
    pygame.display.update()

#GAME OVER SCREEN
#This holds list of all the scores
score_list = [0]

game_over_font1 = pygame.font.Font('freesansbold.ttf', 64)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 32)

def game_over():
    #check for the max score
    maximum = max(score_list)
    display1 = game_over_font1.render(f"GAME OVER", True, (200, 35, 35))
    SCREEN.blit(display1, (50, 300))
    #shows your current and max score
    display2 = game_over_font2.render(f"SCORE: {score} MAX SCORE: {maximum}", True, (255, 255, 255))
    SCREEN.blit(display2, (50, 400))
    #if new score = max score then new high score
    if score == maximum:
        display3 = game_over_font2.render(f"NEW HIGH SCORE!", True, (200, 35, 35))
        SCREEN.blit(display3, (50,100))

running = True
#waiting is going to refer to our start and end screen
waiting = True
#set collision to false in the beginning so that we only see the start screen in the beginning
collision = False
while running:
    SCREEN.fill((0,0,0))

    #display the background image
    SCREEN.blit(BACKGROUND_IMAGE, (0,0))
    #blit basically draws what you have give it at location here (0,0)

    #we will be sent into this while loop at the beginning and end of each game
    while waiting:
        if collision:
            #if collision is True (from second time onwards) we will see both the end and the start screen
            game_over()
            start()
        else:
            #this refers to the first time the player is starting the game
            start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                running = False
            # if you press EXIT (or the cross button) then you will exit out of the game

        #Below two if statements tell the program what to do when we press the space
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                #if we press the space bar we will exit out of the waiting while loop and start to play the game
                #we will be reseting the variables such as the score and bird's y position and obstacle starting position
                    score = 0
                    bird_y = 300
                    obstacle_x = 500
                    waiting = False #exiting out of whaile loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 3

    bird_y += bird_y_change

    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 535:
        bird_y = 535

    # Moving the obstacle
    obstacle_x += OBSTACLE_X_CHANGE

    #COLLISION
    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, bird_y, OBSTACLE_HEIGHT +150) #for the last argument, +150 means we're going down

    if collision:
        score_list.append(score)
        waiting = True

    # generating new obstacles
    if obstacle_x <= -10:
        obstacle_x = 500  # starts again at the leftmost edge of the window
        OBSTACLE_HEIGHT = random.randint(150, 450)
        score += 1
    # displaying the obstacle
    display_obstacle(OBSTACLE_HEIGHT)

    #displaying the bird
    display_bird(bird_x, bird_y)

    #display the score
    score_display(score)

    # Update the display after each iteration of the while loop
    pygame.display.update()

# Quit the program
pygame.quit()