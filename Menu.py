import pygame
import Game
#rest = 800 600


def menu(tela):
    x_init = 400
    y_init = 300
    eixo_x = 0
    eixo_y = 0
    snake_lst = []
    tam = 1

    font = pygame.font.SysFont('Monospace',35)
    sair = font.render('Sair', True, (255,255,255))
    jogar = font.render('Jogar', True, (255,255,255))
    SNK = font.render('Cobrinha', True, (255,255,255))
    BY = font.render('By Thiago Rigotto Stachuk', True, (255,255,255))

    tela.fill((0,0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 <= mouse[0] <= 440 and 400 <= mouse[1] <= 440:
                    pygame.quit()
                    quit()
                if 300 <= mouse[0] <= 440 and 300 <= mouse[1] <= 340:
                    Game.mov(tela,x_init,y_init,eixo_x,eixo_y, snake_lst, tam)
        pygame.draw.rect(tela,(170,170,170),[300,400,140,40])
        pygame.draw.rect(tela,(170,170,170),[300,300,140,40])
        tela.blit(sair, [320, 400])
        tela.blit(jogar, [320, 300])
        tela.blit(SNK, [300, 100])
        tela.blit(BY, [150, 150])
        mouse = pygame.mouse.get_pos()
        pygame.display.update()
        
