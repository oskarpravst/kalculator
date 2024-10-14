import pygame
from pygame import *


pygame.init()
back = (46, 46, 46)
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Kalculator')
gameDisplay.fill(back)
clock = pygame.time.Clock()
running = True

charater_img = pygame.image.load("nurek.png")

def charater(x, y):
    gameDisplay.blit(charater_img, (x, y))

x = 100
y = 400

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(60)
    charater(x, y)
    x += 1
    
    
    
    

pygame.quit()
quit()
            