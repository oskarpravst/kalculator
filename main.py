import pygame
import random
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
def character(charater_x, charater_y):
    gameDisplay.blit(character_img, (charater_x, charater_y))

def spike(spike_x, spike_y):
    gameDisplay.blit(spike_img, (spike_x, spike_y))
    gameDisplay.blit(spike_img, (spike_x+30, spike_y))


def floor(floor_x, floor_y, floor_level):
    gameDisplay.blit(floor_img, (floor_x, floor_y))
    for i in range(8):
        gameDisplay.blit(floor_img, (floor_x, floor_y + floor_level))
        floor_level+=16

def text(string, text_x, text_y, font_size):
    font = pygame.font.Font("minecraft_font.ttf", font_size)
    text = font.render(string, True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (text_x, text_y)
    return(text, text_rect)


        

# MASKS
character_mask = pygame.mask.from_surface(character_img)
mask_img = character_mask.to_surface()

spike_mask = pygame.mask.from_surface(spike_img)


# VARIABLES
running = True
charater_x = 100
charater_y = 150
spike_x = 1000
spike_y = 140
floor_y = 172
floor_x = 0
ground_y = 150
floor_level = 0
random_spawn_spike = random.randint(0, 2)
spike_speed = random.randint(6, 12)
death_text = text("YOU DIED", 500, 100, 50)
score = 0
score_text = text(str(score), 500, 100, 50)



back = (46, 46, 46)

jumping = False
velocity = 0
jump_strength = 10 # Set a fixed jump strength

while running:
    gameDisplay.fill(back)
    floor(floor_x, floor_y, floor_level)
    character(charater_x, charater_y)
    
    spike(spike_x, spike_y)
    # gameDisplay.blit(mask_img, (100, 150))

    if character_mask.overlap(spike_mask, (spike_x - charater_x, spike_y - charater_y)): # subtract coordinates of the spike and the charater
        gameDisplay.blit(death_text[0], death_text[1])
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
        
        
    
    
    spike_x -= spike_speed
    if spike_x < 0:
        spike_speed = random.randint(6, 12)
        spike_x = 1000

    if 50 < spike_x < 150:
        score +=1
        pygame.display.update()
        
    
        

        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys_pressed = pygame.key.get_pressed()
        
    if not jumping:
        if keys_pressed[pygame.K_SPACE]:
            jumping = True
            velocity = jump_strength  # Set the initial jump velocity
    if jumping:
        charater_y -= velocity  # Move the character up
        velocity -= 1  # Decrease the velocity

        # If the character has fallen back to the ground
        if charater_y >= ground_y:
            charater_y = ground_y  # Reset to ground level
            jumping = False  # Reset jumping state
            velocity = 0  # Reset velocity
    gameDisplay.blit(score_text[0], score_text[1])
    pygame.display.update()
    clock.tick(60)

pygame.quit()
