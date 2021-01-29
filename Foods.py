import random
import pygame

def Food(tela):
    blue = (0,0,255)#0, 1p
    red = (255,0,0)#1, 5p
    purple = (255,0,255)#2, 10p
    cx = round(random.randrange(0, 795) / 10) * 10
    cy = round(random.randrange(0, 595) / 10) * 10
    rng = random.randint(0,10)
    #print(rng)
    if rng > 2:
        pygame.draw.rect(tela,red,[cx,cy, 10, 10])
        return rng,cx,cy,red
    elif rng >= 1 and rng <= 2:
        pygame.draw.rect(tela,blue,[cx,cy, 10, 10])
        return rng,cx,cy,blue
    else:
        pygame.draw.rect(tela,purple,[cx,cy, 10, 10])
        return rng,cx,cy,purple