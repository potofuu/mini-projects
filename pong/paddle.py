import pygame

blackc = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(blackc)
        self.image.set_colorkey(blackc)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect