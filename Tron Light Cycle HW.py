import pygame

pygame.init()

# Declaring Constants
WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tron Light Cycle HW")

# Declaring Variables
FPS=10
clock=pygame.time.Clock()

# Game Variables
cell_size=20

start_x=300
start_y=300

trail_width=20

rider_x=start_x
rider_y=start_y

rider_dx=0
rider_dy=0

score=0
speed=10

font=pygame.font.SysFont("Comic Sans MS", 25)
st=font.render("Score="+str(score),True,"black")
sr=st.get_rect()
sr.topleft=(50,50)

font1=pygame.font.SysFont("Comic Sans MS", 50)
gt=font.render("GAME OVER",True,"red")
gr=gt.get_rect()
gr.center=(400,300)

# Define CSS
trail_color="yellow"
rider_color="red"
bg_color="black"

screen.fill(bg_color)

gameloop=True

trail = set()
# Handle Player Input for Movement
while gameloop:  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False

    trail.add((rider_x, rider_y, trail_width, trail_width))
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            rider_dx=1*speed
            rider_dy=0
        if event.key==pygame.K_LEFT:
            rider_dx=-1*speed
            rider_dy=0
        if event.key==pygame.K_UP:
            rider_dx=0
            rider_dy=-1*speed
        if event.key==pygame.K_DOWN:
            rider_dx=0
            rider_dy=1*speed
# Update the player's position and trail
    rider_x = rider_x + rider_dx
    rider_y = rider_y + rider_dy

    rider=pygame.draw.rect(screen, rider_color, (rider_x, rider_y, trail_width, trail_width))
    for point in trail:
        tp = pygame.draw.rect(screen, "yellow", point)
        if rider.colliderect(tp):
            screen.fill("black")
            screen.blit(gt,gr)
            pygame.display.update()
            pygame.time.delay(2000)
            gameloop=False

    pygame.display.flip()
    clock.tick(FPS)

    

pygame.quit()