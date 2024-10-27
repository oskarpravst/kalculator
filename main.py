import pygame
from pygame import *

# SETUP
pygame.init()
gameDisplay = pygame.display.set_mode((1000, 300))
pygame.display.set_caption('Kalculator')
clock = pygame.time.Clock()

# IMAGES
character_img = pygame.image.load("nurek.png")
spike_img = pygame.image.load("Spike_Pixel.png")
floor_img = pygame.image.load("tileplanks.png")

# FUNCTIONS
def character(x, y):
    gameDisplay.blit(character_img, (x, y))

def spike(x1, y1):
    gameDisplay.blit(spike_img, (x1, y1))
    gameDisplay.blit(spike_img, (x1+30, y1))

def floor(x2, y2):
    gameDisplay.blit(floor_img, (x2, y2))

        

# MASKS
character_mask = pygame.mask.from_surface(character_img)
mask_img = character_mask.to_surface()

spike_mask = pygame.mask.from_surface(spike_img)


# VARIABLES
running = True
x = 100
y = 150
x1 = 1000
y1 = 140
y2 = 172
x2 = 1
ground_y = 150

back = (46, 46, 46)

jumping = False
velocity = 0
jump_strength = 10 # Set a fixed jump strength

while running:
    gameDisplay.fill(back)
    floor(x2, y2)
    character(x, y)
    
    spike(x1, y1)
    # gameDisplay.blit(mask_img, (100, 150))

    if character_mask.overlap(spike_mask, (x1 - x, y1 - y)): # subtract coordinates of the spike and the charater
        print("dead")
        
    
    
    
    x1 -= 7
    if x1 < 0:
        x1 = 1000

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
