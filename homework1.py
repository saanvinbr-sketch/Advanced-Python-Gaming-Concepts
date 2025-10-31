import pygame
import random
pygame.init()

WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The Great Escape")

FPS=20
clock=pygame.time.Clock()

small_rect_x=400
small_rect_y=300

small_rect_dx=0
small_rect_dy=0

# wall1=pygame.draw.rect(screen, "red", (50,50,150,20))
# wall2=pygame.draw.rect(screen, "orange", (21,23,432,293))
# wall3=pygame.draw.rect(screen, "yellow", (57,65,75,56))
# wall4=pygame.draw.rect(screen, "green", (89,38,570,387))
# wall5=pygame.draw.rect(screen, "blue", (43,43,94,59))
# wall6=pygame.draw.rect(screen, "purple", (42,42,54,244))
# wall7=pygame.draw.rect(screen, "hotpink", (24,24,94,298))
# wall8=pygame.draw.rect(screen, "turquoise", (43,43,21,432))
# wall9=pygame.draw.rect(screen, "red", (34,43,43,223))
# wall10=pygame.draw.rect(screen, "orange", (96,72,58,742))
# wall11=pygame.draw.rect(screen, "yellow", (42,65,67,87))
# wall12=pygame.draw.rect(screen, "green", (23,34,45,56))
# wall13=pygame.draw.rect(screen, "blue", (65,67,787,344))
# wall14=pygame.draw.rect(screen, "purple", (32,43,56,67))
# wall15=pygame.draw.rect(screen, "hotpink", (23,21,90,76))
# wall16=pygame.draw.rect(screen, "turquoise", (89,87,76,65))
# wall17=pygame.draw.rect(screen, "red", (98,87,76,65))
# wall18=pygame.draw.rect(screen, "orange", (76,67,76,76))
# wall19=pygame.draw.rect(screen, "yellow", (6,56,56,65))
# wall20=pygame.draw.rect(screen, "green", (76,45,493,232))
# wall21=pygame.draw.rect(screen, "blue", (21,67,87,98))
# wall22=pygame.draw.rect(screen, "purple", (53,65,87,98))
# wall23=pygame.draw.rect(screen, "hotpink", (1,2,3,4))
# wall24=pygame.draw.rect(screen, "turquoise", (11,22,33,44))
# wall25=pygame.draw.rect(screen, "turquoise", (55,66,77,88))
person=pygame.draw.rect(screen, "white", (400,300,40,40))

speed=10
gameloop=True

while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            small_rect_dx=1*speed
            small_rect_dy=0
        
        if event.key==pygame.K_LEFT:
            small_rect_dx=-1*speed
            small_rect_dy=0

        if event.key==pygame.K_UP:
            small_rect_dx=0
            small_rect_dy=-1*speed

        if event.key==pygame.K_DOWN:
            small_rect_dx=0
            small_rect_dy=1*speed
    small_rect_x=small_rect_x+small_rect_dx
    small_rect_y=small_rect_y+small_rect_dy

    screen.fill("black")
    # pygame.display.flip()
    wall1 = pygame.draw.rect(screen, "red", (50, 50, 150, 20))
    wall2 = pygame.draw.rect(screen, "orange", (10, 100, 150, 20))
    wall3 = pygame.draw.rect(screen, "yellow", (150, 200, 20, 150))
    wall4 = pygame.draw.rect(screen, "GREEN", (300, 70, 20, 150))
    wall5 = pygame.draw.rect(screen, "BLUE", (340, 200, 20, 150))
    wall6 = pygame.draw.rect(screen, "INDIGO", (20, 150, 140, 20))
    wall7 = pygame.draw.rect(screen, "VIOLET", (200, 310, 150, 20))
    wall8 = pygame.draw.rect(screen, "RED", (350, 350, 150, 20))
    wall9 = pygame.draw.rect(screen, "ORANGE", (50, 500, 150, 20))
    wall10 = pygame.draw.rect(screen, "YELLOW", (150, 450, 20, 150))
    wall11 = pygame.draw.rect(screen, "GREEN", (300, 500, 150, 20))
    wall12 = pygame.draw.rect(screen, "BLUE", (450, 450, 20, 150))
    wall13 = pygame.draw.rect(screen, "INDIGO", (500, 350, 150, 20))
    wall14 = pygame.draw.rect(screen, "VIOLET", (650, 380, 20, 150))
    wall15 = pygame.draw.rect(screen, "RED", (700, 200, 150, 20))
    wall16 = pygame.draw.rect(screen, "ORANGE", (600, 100, 20, 150))
    wall17 = pygame.draw.rect(screen, "YELLOW", (500, 50, 150, 20))
    wall18 = pygame.draw.rect(screen, "GREEN", (400, 100, 20, 150))
    wall19 = pygame.draw.rect(screen, "BLUE", (350, 200, 150, 20))
    wall20 = pygame.draw.rect(screen, "INDIGO", (250, 380, 20, 150))
    wall21 = pygame.draw.rect(screen, "VIOLET", (50, 390, 150, 20))
    wall22 = pygame.draw.rect(screen, "RED", (100, 200, 20, 150))
    wall23 = pygame.draw.rect(screen, "ORANGE", (200, 100, 150, 20))
    wall24 = pygame.draw.rect(screen, "YELLOW", (300, 400, 20, 150))
    wall25 = pygame.draw.rect(screen, "GREEN", (600, 500, 150, 20))
    person=pygame.draw.rect(screen, "white", (small_rect_x,small_rect_y,40,40))

    if person.colliderect(wall1):
        gameloop=False
    if person.colliderect(wall2):
        gameloop=False
    if person.colliderect(wall3):
        gameloop=False
    if person.colliderect(wall4):
        gameloop=False
    if person.colliderect(wall5):
        gameloop=False
    if person.colliderect(wall6):
        gameloop=False
    if person.colliderect(wall7):
        gameloop=False
    if person.colliderect(wall8):
        gameloop=False
    if person.colliderect(wall9):
        gameloop=False
    if person.colliderect(wall10):
        gameloop=False
    if person.colliderect(wall11):
        gameloop=False
    if person.colliderect(wall12):
        gameloop=False
    if person.colliderect(wall13):
        gameloop=False
    if person.colliderect(wall14):
        gameloop=False
    if person.colliderect(wall15):
        gameloop=False
    if person.colliderect(wall16):
        gameloop=False
    if person.colliderect(wall17):
        gameloop=False
    if person.colliderect(wall18):
        gameloop=False
    if person.colliderect(wall19):
        gameloop=False
    if person.colliderect(wall20):
        gameloop=False
    if person.colliderect(wall21):
        gameloop=False
    if person.colliderect(wall22):
        gameloop=False
    if person.colliderect(wall23):
        gameloop=False
    if person.colliderect(wall24):
        gameloop=False
    if person.colliderect(wall25):
        gameloop=False

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()