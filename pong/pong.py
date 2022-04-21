import black
import pygame;
pygame.init()

from paddle import Paddle

blackc = (0, 0, 0)
whitec = (0, 0, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(whitec, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
paddleB = Paddle(whitec, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

sprites_list = pygame.sprite.Group()
sprites_list.add(paddleA)
sprites_list.add(paddleB)

time = pygame.time.Clock()
playing = true

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = false

    sprites_list.update()

    screen.fill(blackc)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    sprites_list.draw(screen)
    
    pygame.display.flip()
    time.tick(60)



pygame.quit
