import pygame
from sys import exit


pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Hurdle Race')
type_display = 0
clock = pygame.time.Clock();
dude_gravity = 0
start_time = 0
score = 0
road_speed = 5

#? Sky images
sky1 = pygame.image.load('games/Hurdle Race/sky1.png').convert_alpha()
sky2 = pygame.image.load('games/Hurdle Race/sky2.png').convert_alpha()
sky1_rect = sky1.get_rect(topleft = (0,0))
sky2_rect = sky2.get_rect(topleft = (0,0))

#? Ground images
trees = pygame.image.load('games/Hurdle Race/trees.png').convert_alpha()
road = pygame.image.load('games/Hurdle Race/road.png').convert_alpha()
hurdle = pygame.image.load('games/Hurdle Race/hurdle.png').convert_alpha()
trees_rect = trees.get_rect(topleft = (0,40))
road_rect = road.get_rect(topleft = (0,0))
hurdle_rect = hurdle.get_rect(bottomleft = (800, 392))

#? Title
title = pygame.image.load('games/Hurdle Race/title.png').convert_alpha()
title_rect = title.get_rect(center = (400, 100))

#? Start
start = pygame.image.load('games/Hurdle Race/start.png').convert_alpha()
start_rect = start.get_rect(center = (400,250))
start1 = pygame.image.load('games/Hurdle Race/start1.png').convert_alpha()
start1_rect = start1.get_rect(center = (400,250))

#? Dude
dude = pygame.image.load('games/Hurdle Race/dude.png').convert_alpha()
dude_rect = dude.get_rect(bottomleft = (10, 375))

#? Text
text1_font = pygame.font.Font('games/Hurdle Race/Pixeled.ttf', 50)
text2_font = pygame.font.Font('games/Hurdle Race/Pixeled.ttf', 25)
gameOver = text1_font.render('Game Over', False, 'black')
gameOver_rect = gameOver.get_rect(center = (400,40))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and dude_rect.bottom == 375:
            dude_gravity = -20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and type_display == 2:
            type_display = 0
        if type_display == 0:
            start_time = int(pygame.time.get_ticks()/1000)
            road_speed = 5
        

        
        
    if type_display == 0 or type_display == 1:

        screen.fill('0x94d2bd')
        screen.blit(sky1, sky1_rect)
        screen.blit(sky2, sky2_rect)
        screen.blit(trees, trees_rect)
        screen.blit(road, road_rect)
        screen.blit(title, title_rect)
        
        if start_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(start1, start1_rect)
            if pygame.mouse.get_pressed() == (1,0,0):
                type_display = 1
        else:
            screen.blit(start, start_rect)
        sky1_rect.x -= 2
        sky2_rect.x -= 1
        trees_rect.x -= 3
        road_rect.x -= road_speed
        
        
        if sky1_rect.centerx <= 1: sky1_rect.left = 0
        if sky2_rect.centerx <= 1: sky2_rect.left = 0
        if trees_rect.centerx <= 1: trees_rect.left = 0
        if road_rect.centerx <= 1: road_rect.left = 0
        

    if type_display == 1:

        title_rect.left = 800
        start1_rect.left = 800
        start_rect.left = 800
        screen.blit(hurdle, hurdle_rect)
        screen.blit(dude, dude_rect)
        hurdle_rect.x -= road_speed

        current_time = int(pygame.time.get_ticks() / 1000) - start_time;
        score_surf = text1_font.render(f'{current_time}', True, 'black')
        score_rect = score_surf.get_rect(center = (400,50))
        

        if hurdle_rect.right <= 0: hurdle_rect.left = 800

        dude_gravity += 1
        dude_rect.y += dude_gravity

        if dude_rect.bottom >= 375: dude_rect.bottom = 375

        if dude_rect.colliderect(hurdle_rect):
            score = int(pygame.time.get_ticks() / 1000) - start_time;
            type_display = 2
            title_rect.centerx = 400
            start1_rect.centerx = 400
            start_rect.centerx = 400
            hurdle_rect.left = 800
            score_rect.left = 800

        if (pygame.time.get_ticks()%1000) <10:
            road_speed += 1
            

        screen.blit(score_surf, score_rect)

    if type_display == 2:

        score_label = text2_font.render('Score: '+ f'{score}', False, 'black')
        score_rectangle = score_label.get_rect(center = (400,100))
        screen.blit(score_label, score_rectangle)
        screen.blit(gameOver, gameOver_rect)




    pygame.display.update()
    clock.tick(60)