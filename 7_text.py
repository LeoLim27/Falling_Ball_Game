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
character_x_pos = (screen_width -character_width)/2# x position
character_y_pos = screen_height-character_height #bottom of the screen

#moving position
to_x =0
to_y =0

#spped of the character
character_speed= 0.5

# enemy character
enemy = pygame.image.load("/Users/user/Desktop/VS_code/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width-enemy_width)/2
enemy_y_pos = (screen_height-enemy_height)/2

#font
game_font = pygame.font.Font(None, 40) # font object generation

# total time
total_time =30

#start time
start_ticks = pygame.time.get_ticks()

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
    
    #collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("collided")
        running = False

    #clear the screen and draw the background
    screen.blit(background, (0,0)) #blit takes the source surface and(,) a destiantio point

    screen.blit(character, (character_x_pos, character_y_pos))
    
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    #timer
    # miliseconds to seconds == divide by 1000
    elapsed_time = (pygame.time.get_ticks() - start_ticks) /1000

    #render function(time, antialias, color, background = None)
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))

    screen.blit(timer, (10,10))

    if total_time - elapsed_time <=0:
        print("Time Out")
        runnint =False
    
    
    pygame.display.update()

#waiting
pygame.time.delay(1000)

# Quit pygame
pygame.quit()