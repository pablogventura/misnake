import pygame
from pygame.locals import *
 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
 
HEIGHT = 480
WIDTH = 640
ACC = 0.5
FRIC = -0.12
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

class Segmento(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__() 
        self.x = x
        self.y = y
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(topleft=(x*30, y*30))

 

snake = [Segmento(x,10) for x in range(8,18)]

all_sprites = pygame.sprite.Group()
for s in snake:
    all_sprites.add(s)

 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake = [Segmento(snake[0].x,snake[0].y-1)] + snake
                all_sprites.add(snake[0])
                all_sprites.remove(snake.pop(-1))
            elif event.key == pygame.K_DOWN:
                snake = [Segmento(snake[0].x,snake[0].y+1)] + snake
                all_sprites.add(snake[0])
                all_sprites.remove(snake.pop(-1))
            elif event.key == pygame.K_RIGHT:
                snake = [Segmento(snake[0].x+1,snake[0].y)] + snake
                all_sprites.add(snake[0])
                all_sprites.remove(snake.pop(-1))
            elif event.key == pygame.K_LEFT:
                snake = [Segmento(snake[0].x-1,snake[0].y)] + snake
                all_sprites.add(snake[0])
                all_sprites.remove(snake.pop(-1))
     
    displaysurface.fill((0,0,0))
 
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
 
    pygame.display.update()
    FramePerSec.tick(FPS)
    
    
    
    
    
    
    
    
    
    
