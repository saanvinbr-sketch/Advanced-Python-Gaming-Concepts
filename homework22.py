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

font=pygame.font.Font(None, 36)

while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    
    screen.fill("black")

    pygame.draw.line(screen, "white", (0,60), (1200,60), 4)
    pygame.draw.line(screen, "white", (0, 600), (1200,600), 4)

    Score_text=font.render("Score: " +str(paddle_ball.score), True, "white")
    score_rect=Score_text.get_rect(center=(600,50))
    screen.blit(Score_text, score_rect)

    Lives_text=font.render("Lives: "+str(paddle_ball.lives), True, "white")
    lives_rect=Lives_text.get_rect(center=(1100,50))
    screen.blit(Lives_text, lives_rect)

    # if pygame.sprite.groupcollide(paddle_ball_group, bricks_group, True, True):
    #     bricks_group.remove()
    #     paddle_ball.score=paddle_ball.score + 10
    #     paddle_ball.speed_y *= -1

    if pygame.sprite.spritecollide(paddle_ball, bricks_group, True):
        bricks_group.remove()
        paddle_ball.score=paddle_ball.score + 10
        paddle_ball.speed_y *= -1
    
    if pygame.sprite.spritecollide(paddle_ball, paddle_group, False):
        paddle_ball.speed_y *= -1


    paddle_ball_group.update()
    paddle_ball_group.draw(screen)

    paddle_group.update(event)
    paddle_group.draw(screen)

    bricks_group.update()
    bricks_group.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()