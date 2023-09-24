import pygame
import os

#initializing (necessary)
pygame.init()

#Screeb size
screen_width =470 #width
screen_height =640 #height
screen = pygame.display.set_mode((screen_width, screen_height))

#Set the title for pygame
pygame.display.set_caption("Crashing") 

#FPS
clock = pygame.time.Clock()
#-------------------------------------------------------------------#

# initializing (user's own)

# 1. game intialization (background, game image, coordination, moving speed, font, collision...)


#Game loop
running = True 
while running:
    dt = clock.tick(60) #FPS setting
    #if it moves 100 per 1 sec,
    #10 fps means it moves 10 at one time
    #50 fps means it moves 2 at one time (frame means the amount of slices)

#2. processing event
    for event in pygame.event.get(): #getting event input
        if event.type == pygame.QUIT:
            running = False  

#3. moving character events

#4. collision processing

#5. representing all things on the screen
    
    pygame.display.update()

pygame.quit()