import pygame
import random

pygame.init()

screen_width =480 
screen_height =640 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Falling ball") 

game_result = "Game Over"

#FPS
clock = pygame.time.Clock()

# initializing

# 1. game intialization (background, game image, coordination, moving speed, font, collision...)
background = pygame.image.load("/Users/user/Desktop/VS_code/pygame/pygame_basic/real_backgroun.png")

character = pygame.image.load("/Users/user/Desktop/VS_code/pygame/pygame_basic/real_character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = (screen_height - character_height)
character_speed = 7

to_x =0
to_y =0

ball = pygame.image.load("/Users/user/Desktop/VS_code/pygame/pygame_basic/real_ball.png")
ball_size = ball.get_rect().size
ball_width = ball_size[0]
ball_height = ball_size[1]

ball2 = pygame.image.load("/Users/user/Desktop/VS_code/pygame/pygame_basic/real_ball.png")
ball2_size = ball2.get_rect().size
ball2_width = ball2_size[0]
ball2_height = ball2_size[1]

ball3 = pygame.image.load("/Users/user/Desktop/VS_code/pygame/pygame_basic/real_ball.png")
ball3_size = ball3.get_rect().size
ball3_width = ball3_size[0]
ball3_height = ball3_size[1]

ball_x_pos = random.randint(0, (screen_width-ball_width-ball2_width-ball3_width))
ball_y_pos = 0
ball_speed = 16

ball2_x_pos = random.randint(ball_x_pos, screen_width-ball2_width-ball3_width)
ball2_y_pos =0
ball2_speed = 12

ball3_x_pos = random.randint(ball2_x_pos, screen_width-ball3_width)
ball3_y_pos =0
ball3_speed = 14

game_font = pygame.font.Font(None, 40)

#Game loop
running = True
while running:
    dt = clock.tick(60)
    #if it moves 100 per 1 sec,
    #10 fps means it moves 10 at one time
    #50 fps means it moves 2 at one time (frame means the amount of slices)

#2. processing event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x +=character_speed

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0

#3. moving character events
    character_x_pos += to_x
    
    if character_x_pos<0:
        character_x_pos =0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    ball_y_pos += ball_speed

    if ball_y_pos > screen_height:
        ball_y_pos =0
        ball_x_pos = random.randint(0, (screen_width-ball_width-ball2_width-ball3_width))

    ball2_y_pos += ball2_speed

    if ball2_y_pos > screen_height:
        ball2_y_pos =0
        ball2_x_pos = random.randint(ball_x_pos, screen_width-ball2_width)

    ball3_y_pos += ball3_speed

    if ball3_y_pos > screen_height:
        ball3_y_pos =0
        ball3_x_pos = random.randint(ball2_x_pos, screen_width-ball3_width)        

#4. collision processing
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ball_rect = ball.get_rect()
    ball_rect.left = ball_x_pos
    ball_rect.top = ball_y_pos

    ball2_rect = ball2.get_rect()
    ball2_rect.left = ball2_x_pos
    ball2_rect.top = ball2_y_pos

    ball3_rect = ball3.get_rect()
    ball3_rect.left = ball3_x_pos
    ball3_rect.top = ball3_y_pos

    if character_rect.colliderect(ball_rect) or character_rect.colliderect(ball2_rect) or character_rect.colliderect(ball3_rect):
        print("Game Over")
        running = False
    
    time = pygame.time.get_ticks()/1000

    record = game_font.render(str(int(time)), True, (0,0,0))

#5. representing all things on the screen
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ball, (ball_x_pos, ball_y_pos))
    screen.blit(ball2, (ball2_x_pos, ball2_y_pos))
    screen.blit(ball3, (ball3_x_pos, ball3_y_pos))
    screen.blit(record, (10,10))

    if running == False:
        msg = game_font.render(game_result,True,(0,0,0))
        msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
        screen.blit(msg, msg_rect)
        result = "Record : {}".format(str(int(pygame.time.get_ticks()/1000)))
        msg2 = game_font.render(result, True, (0,0,0))
        msg2_rect = msg.get_rect(center=(int(screen_width/2-5), int(screen_height/2+25)))
        screen.blit(msg2, msg2_rect)

    pygame.display.update()
pygame.time.delay(2200)

pygame.quit()
