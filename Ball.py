import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
surface = pygame.display.set_mode((300, 400))
pygame.display.set_caption('Ball')

current_y = 100
current_x = 150
vy = 2
vx = 2
clock = pygame.time.Clock()

def drawBall():
    pygame.draw.circle(surface, (0,255,0), (int(current_x),int(current_y)), 12)

def quitGame():
    pygame.quit()
    sys.exit()
    
while True:
    surface.fill((0,0,0))
    current_y += vy
    current_x += vx
    drawBall()

    
    if current_y > 390 or current_y < 10:
        vy *= -1
    if current_x > 290 or current_x < 10:
        vx *= -1
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()
                
        if event.type == GAME_GLOBALS.QUIT:
            quitGame()
    clock.tick(30)
    pygame.display.update()
