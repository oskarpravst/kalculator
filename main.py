import pygame
import random
from pygame import *

# SETUP
pygame.init()
gameDisplay = pygame.display.set_mode((1000, 300))
pygame.display.set_caption('Jump - Space')
clock = pygame.time.Clock()

# IMAGES
character_img = pygame.image.load("nurek.png")
spike_img = pygame.image.load("Spike_Pixel.png")
floor_img = pygame.image.load("tileplanks.png")

# FUNCTIONS
def character(charater_x, charater_y):
    gameDisplay.blit(character_img, (charater_x, charater_y))

def update_spikes(spike_x_list):
    for i in range(len(spike_x_list)):
        print(spike_x_list[i])
        spike_x_list[i] -= 10
        



def spike(spike_x):
    for i in range(len(spike_x)):
        gameDisplay.blit(spike_img, (spike_x[i], 140))
        gameDisplay.blit(spike_img, (spike_x[i]+30, 140))
        # if spike_x_list[i] < 0:
        #     del spike_x_list[i]


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
spike_x_list = []
timer = 0
sigma = 20

while running:
    
    
    if timer > sigma:
        
        spike_x_list.append(1000)
        timer = 0
        sigma = random.randint(18, 50)
    update_spikes(spike_x_list)

    gameDisplay.fill(back)
    floor(floor_x, floor_y, floor_level)
    character(charater_x, charater_y)
    
    spike(spike_x_list)
    # gameDisplay.blit(mask_img, (100, 150))

    for i in range(len(spike_x_list)):
        if character_mask.overlap(spike_mask, (spike_x_list[i] - charater_x, 140 - charater_y)): # subtract coordinates of the spike and the charater
            gameDisplay.blit(death_text[0], death_text[1])
            pygame.display.update()
            pygame.time.delay(2000)
            running = False
    

        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys_pressed = pygame.key.get_pressed()
        
    if not jumping:
        if keys_pressed[pygame.K_SPACE]:
            jumping = True
            velocity = jump_strength  
     
    if jumping:
        charater_y -= velocity  
        velocity -= 1 
       
        if charater_y >= ground_y:
            charater_y = ground_y  
            jumping = False  
            velocity = 0 

    gameDisplay.blit(score_text[0], score_text[1])
    pygame.display.update()
    clock.tick(60)
    print(spike_x_list)
    timer += 1
    print(timer)

pygame.quit()
