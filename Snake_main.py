import pygame
import time
import random
import Foods
import Game

def game():
    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    x_init = 400
    y_init = 300
    eixo_x = 0
    eixo_y = 0
    snake_lst = []
    tam = 1
    pygame.display.set_caption('Jogo da Cobrinha por Thiago Rto.Stk')
    Game.mov(tela,x_init,y_init,eixo_x,eixo_y, snake_lst, tam)

game()
quit()