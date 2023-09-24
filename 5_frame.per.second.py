import pygame

pygame.init() #initializing (necessary)

#Screeb size
screen_width =470 #width
screen_height =640 #height
screen = pygame.display.set_mode((screen_width, screen_height))

#Set the title for pygame
pygame.display.set_caption("Crashing") #게임이름

#FPS
clock = pygame.time.Clock()

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

#moving position
to_x =0
to_y =0

#spped of the character
character_speed= 0.5

#Game loop
running = True 
while running:
    dt = clock.tick(60) #FPS setting
    #if it moves 100 per 1 sec,
    #10 fps means it moves 10 at one time
    #50 fps means it moves 2 at one time (frame means the amount of slices)

    for event in pygame.event.get(): #getting event input
        if event.type == pygame.QUIT:
            running = False  

        #moving character events
        if event.type == pygame.KEYDOWN: #KEYDOWN for checking key is pressed
            if event.key == pygame.K_LEFT:
                to_x -=character_speed
            elif event.key == pygame.K_RIGHT:
                to_x+=character_speed
            elif event.key == pygame.K_UP:
                to_y -=character_speed
            elif event.key == pygame.K_DOWN:
                to_y +=character_speed

        if event.type == pygame.KEYUP: #KEYUP for checking user is not pressing key
            if event.key ==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                to_x =0
            elif event.key ==pygame.K_UP or event.key ==pygame.K_DOWN:
                to_y=0
    
    #to fix the game speed
    character_x_pos +=to_x *dt
    character_y_pos +=to_y *dt

    # width border line
    if character_x_pos<0:
        character_x_pos =0
    elif character_x_pos> screen_width-character_width:
        character_x_pos = screen_width-character_width
    # height border line
    if character_y_pos<0:
        character_y_pos =0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height
    

    #clear the screen and draw the background
    screen.blit(background, (0,0)) #blit takes the source surface and(,) a destiantio point

    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()



# Quit pygame
pygame.quit()