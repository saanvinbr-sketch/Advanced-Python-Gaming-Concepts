import pygame
from Paddle import Paddle
from Ball import Paddle_Ball
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

FPS=30
clock=pygame.time.Clock()
gameloop=True

while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    
    screen.fill("black")

    paddle_ball_group.update()
    paddle_ball_group.draw(screen)

    paddle_group.update(event)

    paddle_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()