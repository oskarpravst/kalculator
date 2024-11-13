import pygame
import random
from pygame import *

font_main = "minecraft_font.ttf"

# SETUP
pygame.init()
gameDisplay = pygame.display.set_mode((1000, 300))
pygame.display.set_caption('Jump - Space')
clock = pygame.time.Clock()

# IMAGES
character_img = pygame.image.load("nurek.png")
spike_img = [pygame.image.load("rock1.png"),
             pygame.image.load("rock2.png"),
             pygame.image.load("rock3.png"),
             pygame.image.load("rock4.png")]
floor_img = pygame.image.load("tileplanks.png")

# FUNCTIONS
def character(charater_x, charater_y):
    gameDisplay.blit(character_img, (charater_x, charater_y))

def update_spikes(spike_x_list):

    for i in range(len(spike_x_list)):
        spike_x_list[i] -= spike_speed
        if spike_x_list[i] > -100:
            temp_list.append(spike_x_list[i])

    spike_x_list = []


def spike(spike_x, j):
    j = round(j)
    for i in range(len(spike_x)):
        gameDisplay.blit(spike_img[j], (spike_x[i], 140))
        
        
            

        # if spike_x_list[i] < 0:
        #     del spike_x_list[i]


def floor(floor_x, floor_y, floor_level):
    gameDisplay.blit(floor_img, (floor_x, floor_y))
    for i in range(8):
        gameDisplay.blit(floor_img, (floor_x, floor_y + floor_level))
        floor_level+=16

def text(string, text_x, text_y, font_size):
    font = pygame.font.Font(font_main, font_size)
    text = font.render(string, True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (text_x, text_y)
    return(text, text_rect)


        

# MASKS
character_mask = pygame.mask.from_surface(character_img)
mask_img = character_mask.to_surface()

spike_mask = pygame.mask.from_surface(spike_img[0])


# VARIABLES
running = True
game = False
start_text = text("CLICK R TO RUN ", 500, 100, 50)
gameDisplay.blit(start_text[0], start_text[1])
pygame.display.update()

while running:
    animation = 0
    

    
    charater_x = 100
    charater_y = 150
    floor_y = 172
    floor_x = 0
    ground_y = 150
    floor_level = 0
    random_spawn_spike = random.randint(0, 2)
    spike_speed = 10
    death_text = text("YOU DIED, TOTAL SCORE: ", 500, 100, 50)
    
    score = 0
    score_text = text(str(score), 500, 100, 50)
    back = (46, 46, 46)
    jumping = False
    velocity = 0 
    jump_strength = 8 # Set a fixed jump strength
    spike_x_list = []
    temp_list = []
    timer = 0
    sigma = 20
    while game:
        
        animation += 0.25
        if animation >= 3.5:
            animation  = 0
        
        
    
        if timer > sigma:
            
            spike_x_list.append(1000)
            timer = 0
            sigma = random.randint(15, 40)

        temp_list = []
        
        update_spikes(spike_x_list)
        spike_x_list = temp_list
        

        gameDisplay.fill(back)
        floor(floor_x, floor_y, floor_level)
        character(charater_x, charater_y)
        
        
        # rock = spike_img[animation]
        spike(spike_x_list, animation)
        if score == 10:
            spike_speed = 11
        if score == 20:
            spike_speed = 12
        if score == 30:
            spike_speed = 14
        
        # gameDisplay.blit(mask_img, (100, 150))

        for i in range(len(spike_x_list)):
            if character_mask.overlap(spike_mask, (spike_x_list[i] - charater_x, 140 - charater_y)): # subtract coordinates of the spike and the charater
                gameDisplay.blit(death_text[0], death_text[1])
                score_text = text(str(score), 900, 100, 50)
                gameDisplay.blit(score_text[0], score_text[1])
                pygame.display.update()
                game = False
                
        
        for i in range(len(spike_x_list)):
            if -11<spike_x_list[i]<0 :
                score += 1
                score_text = text(str(score), 500, 100, 50)
                
            

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
        timer += 1
        
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
   
    
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_r]:
        

        game = True

    

