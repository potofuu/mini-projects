import pygame
from paddle import Paddle
from ball import Ball
 
pygame.init()
 
colorb = (0,0,0)
colorw = (255,255,255)
 
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
 
paddleA = Paddle(colorw, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(colorw, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(colorw, 10, 10)
ball.rect.x = 345
ball.rect.y = 195
 
sprites_list = pygame.sprite.Group()
 
sprites_list.add(paddleA)
sprites_list.add(paddleB)
sprites_list.add(ball)
 
carryOn = True
 
clock = pygame.time.Clock()
 
aScore = 0
bScore = 0

while carryOn:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     carryOn=False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)    
 
    sprites_list.update()
 
    if ball.rect.x >= 690:
        aScore += 1
        ball.velocity[0] = -ball.velocity[0]
        
    if ball.rect.x <= 0:
        bScore += 1
        ball.velocity[0] = -ball.velocity[0]

    if ball.rect.x >= 690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1] 

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()

    screen.fill(colorb)
    pygame.draw.line(screen, colorw, [349, 0], [349, 500], 5)
    sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(aScore), 1, colorw)
    screen.blit(text, (250,10))
    text = font.render(str(bScore), 1, colorw)
    screen.blit(text, (420,10))

    pygame.display.flip()
     
    clock.tick(60)
 
pygame.quit()