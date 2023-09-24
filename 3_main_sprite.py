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

#Load the character(Sprite)
character = pygame.image.load("/Users/user/Desktop/VS_code/pygame_basic/character.png")
#character size
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
#Python draw the things afte the start point(from start point to the right and down)
character_x_pos = screen_width / 2 -35# x position
character_y_pos = screen_height-70 #bottom of the screen


#Game loop
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
    
    #clear the screen and draw the background
    screen.blit(background, (0,0)) #blit takes the source surface and(,) a destiantio point

    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()



# Quit pygame
pygame.quit()