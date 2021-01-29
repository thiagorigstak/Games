import pygame
import Menu

def game():
    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Jogo da Cobrinha por Thiago Rto.Stk')
    Menu.menu(tela)

game()
quit()
