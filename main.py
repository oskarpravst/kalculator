import pygame
from pygame import *

# SETUP
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Kalculator')
clock = pygame.time.Clock()

# IMAGES

charater_img = pygame.image.load("nurek.png")

# FUNCITONS
def charater(x, y):
    gameDisplay.blit(charater_img, (x, y))

# VARIABLES
running = True
x = 100
y = 400

back = (46, 46, 46)

jumping = False

y_gravity = 1
jump_height = 20
y_velocity = jump_height




while running:

    gameDisplay.fill(back)
    
    charater(x, y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         x -= 5
        #     if event.key == pygame.K_RIGHT:
        #         x += 5
        
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE]:
            jumping = True
        if jumping:
            y -= y_velocity
            y_velocity -= y_gravity
            if  y_velocity < -jump_height:
                jumping == True
                y_velocity = jump_height
            
    

    
    pygame.display.update()
    clock.tick(60)   
pygame.quit()
quit()
            