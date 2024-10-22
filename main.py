import pygame
from pygame import *

# SETUP
pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Kalculator')
clock = pygame.time.Clock()

# IMAGES
character_img = pygame.image.load("nurek.png")

# FUNCTIONS
def character(x, y):
    gameDisplay.blit(character_img, (x, y))

# VARIABLES
running = True
x = 100
y = 400
ground_y = 400

back = (46, 46, 46)

jumping = False
velocity = 0
jump_strength = 15  # Set a fixed jump strength

while running:
    gameDisplay.fill(back)
    
    character(x, y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys_pressed = pygame.key.get_pressed()
        
    if not jumping:
        if keys_pressed[pygame.K_SPACE]:
            jumping = True
            velocity = jump_strength  # Set the initial jump velocity
    
    if jumping:
        y -= velocity  # Move the character up
        velocity -= 1  # Decrease the velocity

        # If the character has fallen back to the ground
        if y >= ground_y:
            y = ground_y  # Reset to ground level
            jumping = False  # Reset jumping state
            velocity = 0  # Reset velocity

    pygame.display.update()
    clock.tick(60)

pygame.quit()
