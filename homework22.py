import pygame
from Paddle import Paddle
from Ball import Paddle_Ball
from bricks import Bricks
pygame.init()

WIDTH=1200
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Brick Smash")

paddle_ball_group=pygame.sprite.Group()
paddle_ball=Paddle_Ball(600,350,paddle_ball_group)
paddle_ball_group.add(paddle_ball)

paddle_group=pygame.sprite.Group()
paddle=Paddle()
paddle_group.add(paddle)

bricks_group=pygame.sprite.Group()

FPS=30
clock=pygame.time.Clock()
gameloop=True

total_rows = 7
total_columns = 7

start_x=200
start_y=20

x_space=100
y_space=40

for r in range(0,total_rows):
    for c in range(0,total_columns):
        x = start_x + (c * x_space)
        y = start_y + (r * y_space)
        b = Bricks(x,y,bricks_group)
        bricks_group.add(b)

while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    
    screen.fill("black")

    paddle_ball_group.update()
    paddle_ball_group.draw(screen)

    paddle_group.update(event)
    paddle_group.draw(screen)

    bricks_group.update()
    bricks_group.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()