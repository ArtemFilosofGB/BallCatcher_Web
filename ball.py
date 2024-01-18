import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self,x, speed_fall, surf,score, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (100, 100))
        #self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed_fall
        self.score = score
        self.add(group)


    def update(self,*args):
        if self.rect.y < args[0]-20:
            self.rect.y+=self.speed
        else:
            self.kill()
        # Вращение мяча


