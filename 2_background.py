import pygame

pygame.init() #initializing (necessary)

#Screeb size
screen_width =470 #width
screen_height =640 #height
screen = pygame.display.set_mode((screen_width, screen_height))

#Set the title for pygame
pygame.display.set_caption("Crashing") #게임이름

#Load the background
background = pygame.image.load("/Users/user/Desktop/VS_code/pygame_basic/background.png")

#Game loop
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
    
    #clear the screen and draw the background
    screen.blit(background, (0,0)) #blit takes the source surface and(,) a destiantio point
    pygame.display.update()



# Quit pygame
pygame.quit()